# -*- coding: utf-8 -*-
import sys
import logging
import json
from requests_oauthlib import OAuth1Session


class TwitterApi():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret, logging_level):
        self.oauth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

        log_handler = logging.StreamHandler(sys.stdout)
        log_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(log_handler)
    
    def retrieve_user_timeline(self, screen_name, count):
        params = {"screen_name":screen_name, "count":count}
        response = self.oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=params)

        if "X-Rate-Limit-Remaining" in response.headers:
            if response.headers["X-Rate-Limit-Remaining"] == "0":
                # TODO: write the processing to wait for api restrictions to be lifted
                self.logger.warning("wait %s sec" % 9999)

        if "status" in response.headers:
            if response.headers["status"] != "200 OK":
                self.logger.error("status: %s" % response.headers["status"])
                return None

        json_dict = json.loads(response.text)
        if "errors" in json_dict:
            for error in json_dict["errors"]:
                self.logger.error("message: %s, code: %d" % (error["message"], error["code"]))
            return None

        return json_dict

    def retrieve_favorites(self, screen_name, count):
        params = {"screen_name":screen_name, "count":count}
        response = self.oauth.get("https://api.twitter.com/1.1/favorites/list.json", params=params)

        if "X-Rate-Limit-Remaining" in response.headers:
            if response.headers["X-Rate-Limit-Remaining"] == "0":
                # TODO: write the processing to wait for api restrictions to be lifted
                self.logger.warning("wait %s sec" % 9999)

        if "status" in response.headers:
            if response.headers["status"] != "200 OK":
                self.logger.error("status: %s" % response.headers["status"])
                return None

        json_dict = json.loads(response.text)
        if "errors" in json_dict:
            for error in json_dict["errors"]:
                self.logger.error("message: %s, code: %d" % (error["message"], error["code"]))
            return None

        return json_dict

