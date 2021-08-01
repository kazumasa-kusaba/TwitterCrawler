# -*- coding: utf-8 -*-
import json

class FileManager():
    def __init__(self):
        pass
    
    def get_json_dicts(self, json_file_path):
        with open(json_file_path, "r", encoding="utf8") as f:
            data = f.read()
            json_dicts = json.loads(data)
            return json_dicts
    
    def assemble_datetime_file_name(self, datetime):
        """
        Parameters
        ----------
        datetime_str : str
            datetime string before assembly
            ex) "Sun Sep 23 10:37:54 +0000 2018"
        
        Returns
        -------
        datetime_file_name : str
            assembled datetime file name
            ex) 2018_09_23_10_37_54
        """
        # split datetime into date and time
        splited_datetime = datetime.split(" ")
        splited_time = splited_datetime[3].split(":")

        # get each element
        year   = splited_datetime[5]
        month  = self.__trans_english_month_to_number_string(splited_datetime[1])
        day    = splited_datetime[2]
        hour   = splited_time[0]
        minute = splited_time[1]
        second = splited_time[2]

        ret = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second + ".json"
        return ret

    def __trans_english_month_to_number_string(self, english_month):
        if english_month == "Jan":
            return "01"
        elif english_month == "Feb":
            return "02"
        elif english_month == "Mar":
            return "03"
        elif english_month == "Apr":
            return "04"
        elif english_month == "May":
            return "05"
        elif english_month == "Jun":
            return "06"
        elif english_month == "Jul":
            return "07"
        elif english_month == "Aug":
            return "08"
        elif english_month == "Sep":
            return "09"
        elif english_month == "Oct":
            return "10"
        elif english_month == "Nov":
            return "11"
        elif english_month == "Dec":
            return "12"
        else:
            return "XX"

