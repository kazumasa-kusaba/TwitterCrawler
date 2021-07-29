# -*- coding: utf-8 -*-
import sys
import logging
import json
from requests_oauthlib import OAuth1Session

log_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG) # TODO: change the log level before releasing this software

class TwitterApi():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        self.oauth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
    
    def retrieve_user_timeline(self, screen_name, count):
        params = {"screen_name":screen_name, "count":count}
        response = self.oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=params)

        if "X-Rate-Limit-Remaining" in response.headers:
            if response.headers["X-Rate-Limit-Remaining"] == "0":
                # TODO: write the processing to wait for api restrictions to be lifted
                logging.warning("warning: wait %s sec" % 9999)

        if "status" in response.headers:
            if response.headers["status"] != "200 OK":
                logging.error("error: %s" % response.headers["status"])
                return None

        json_dict = json.loads(response.text)
        if "errors" in json_dict:
            for error in json_dict["errors"]:
                logger.error("error: %s (code: %d)" % (error["message"], error["code"]))
            return None

        return json_dict

    def retrieve_favorite(self, screen_name, count):   
        # TODO: write here
        pass

