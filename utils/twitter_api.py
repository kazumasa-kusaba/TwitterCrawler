# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

class TwitterApi():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        self.twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
    
    def retrieve_user_timeline(self, screen_name, count):
        # TODO: write here
        pass

    def retrieve_favorite(self, screen_name, count):   
        # TODO: write here
        pass

