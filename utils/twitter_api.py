# -*- coding: utf-8 -*-
import logging
from requests_oauthlib import OAuth1Session

logger = logging.getLogger(__name__)

class TwitterApi():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        self.twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
        logger.debug(self.twitter)
    
    def retrieve_user_timeline(self, screen_name, count):
        # TODO: write here
        pass

    def retrieve_favorite(self, screen_name, count):   
        # TODO: write here
        pass

