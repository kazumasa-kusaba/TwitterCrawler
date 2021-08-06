# -*- coding: utf-8 -*-
import sys
import logging
import json
import time
from requests_oauthlib import OAuth1Session


class TwitterApi():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret, logging_level):
        self.oauth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

        log_handler = logging.StreamHandler(sys.stdout)
        log_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging_level)
    
    def retrieve_user_timeline(self, screen_name, count):
        params = {"screen_name":screen_name, "count":count}
        response = self.oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=params)

        if "X-Rate-Limit-Remaining" in response.headers:
            rate_limit_remaining = response.headers["X-Rate-Limit-Remaining"]
            self.logger.debug("rate_limit_remaining: %s" % rate_limit_remaining)
            if rate_limit_remaining == "0":
                self.logger.warning("twitter api rate-limit error occured. wait %s seconds for rate-limit be lifted. " % rate_limit_remaining)
                time.sleep(rate_limit_remaining)

        if "status" in response.headers:
            if response.headers["status"] != "200 OK":
                self.logger.error("status: %s" % response.headers["status"])
                return None

        json_dict = json.loads(response.text)
        if "errors" in json_dict:
            for error in json_dict["errors"]:
                self.logger.critical("message: %s, code: %d" % (error["message"], error["code"]))
            self.logger.critical("check if the access_token infomartion in config.json is correct")
            sys.exit(1)

        return json_dict

    def retrieve_favorites(self, screen_name, count):
        params = {"screen_name":screen_name, "count":count}
        response = self.oauth.get("https://api.twitter.com/1.1/favorites/list.json", params=params)

        if "X-Rate-Limit-Remaining" in response.headers:
            rate_limit_remaining = response.headers["X-Rate-Limit-Remaining"]
            self.logger.debug("rate_limit_remaining: %s" % rate_limit_remaining)
            if rate_limit_remaining == "0":
                self.logger.warning("twitter api rate-limit error occured. wait %s seconds for rate-limit be lifted. " % rate_limit_remaining)
                time.sleep(rate_limit_remaining)

        if "status" in response.headers:
            if response.headers["status"] != "200 OK":
                self.logger.error("status: %s" % response.headers["status"])
                return None

        json_dict = json.loads(response.text)
        if "errors" in json_dict:
            for error in json_dict["errors"]:
                self.logger.critical("message: %s, code: %d" % (error["message"], error["code"]))
            self.logger.critical("check if the access_token infomartion in config.json is correct")
            sys.exit(1)

        return json_dict

