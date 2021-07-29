# -*- coding: utf-8 -*-
import argparse
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "utils")
from utils.twitter_api import TwitterApi
from utils.file_manager import FileManager

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG) # TODO: change the log level before releasing this software

def retrieve_user_timelines(args):
    screen_names = args.target_screen_name
    logger.debug(screen_names)

    file_manager = FileManager()
    json_dicts = file_manager.get_json_dicts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(json_dicts)

    twitter_api = TwitterApi(json_dicts["twitter_api"]["access_token"], \
                             json_dicts["twitter_api"]["access_token_secret"], \
                             json_dicts["twitter_api"]["consumer_key"], \
                             json_dicts["twitter_api"]["consumer_secret"])

    for screen_name in screen_names:
        logger.debug(screen_name)
        # TODO: handle an exception properly
        twitter_api.retrieve_user_timeline(screen_name, 200)

def retrieve_favorites(args):
    screen_names = args.target_screen_name
    logger.debug(screen_names)

    file_manager = FileManager()
    json_dicts = file_manager.get_json_dicts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(json_dicts)

    twitter_api = TwitterApi(json_dicts["twitter_api"]["access_token"], \
                             json_dicts["twitter_api"]["access_token_secret"], \
                             json_dicts["twitter_api"]["consumer_key"], \
                             json_dicts["twitter_api"]["consumer_secret"])

    # TODO: handle an exception properly
    for screen_name in screen_names:
        logger.debug(screen_name)
        # TODO: handle an exception properly
        twitter_api.retrieve_favorite(screen_name, 200)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("command", help="the command you want to run")
    arg_parser.add_argument("target_screen_name", nargs="*", help="screen name of the target name")
    arg_parser.add_argument("-q", "--quiet", required=False, action="store_true", help="do not output log")
    args = arg_parser.parse_args()

    if args.command == "retrieve_user_timelines":
        retrieve_user_timelines(args)
    elif args.command == "retrieve_favorites":
        retrieve_favorites(args)
    else:
        logger.error("error: %s is invalid command!!" % args.command)
        sys.exit(1)

