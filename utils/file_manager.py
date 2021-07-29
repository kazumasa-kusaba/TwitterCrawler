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

