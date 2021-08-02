# -*- coding: utf-8 -*-
import argparse
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "utils")
from utils.twitter_api import TwitterApi
from utils.file_manager import FileManager

log_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)

def retrieve_user_timelines(args, logging_level):
    screen_names = args.target_screen_name
    logger.debug(screen_names)

    file_manager = FileManager(logging_level)
    json_dicts = file_manager.get_json_dicts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(json_dicts)

    twitter_api = TwitterApi(json_dicts["twitter_api"]["access_token"], \
                             json_dicts["twitter_api"]["access_token_secret"], \
                             json_dicts["twitter_api"]["consumer_key"], \
                             json_dicts["twitter_api"]["consumer_secret"], \
                             logging_level)

    for screen_name in screen_names:
        logger.debug(screen_name)
        tweets = twitter_api.retrieve_user_timeline(screen_name, 200)
        if tweets is None:
            continue
        for tweet in tweets:
            file_name = file_manager.assemble_datetime_file_name(tweet["created_at"])
            directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "tweets", screen_name)
            # skip saving tweets if already got
            if file_manager.exists_file(directory_path, file_name):
                logger.debug("already exists")
                break
            file_manager.save_json_dict_as_json_format(directory_path, file_name, tweet)

def retrieve_favorites(args, logging_level):
    screen_names = args.target_screen_name
    logger.debug(screen_names)

    file_manager = FileManager(logging_level)
    json_dicts = file_manager.get_json_dicts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(json_dicts)

    twitter_api = TwitterApi(json_dicts["twitter_api"]["access_token"], \
                             json_dicts["twitter_api"]["access_token_secret"], \
                             json_dicts["twitter_api"]["consumer_key"], \
                             json_dicts["twitter_api"]["consumer_secret"], \
                             logging_level)

    for screen_name in screen_names:
        logger.debug(screen_name)
        favorites = twitter_api.retrieve_favorites(screen_name, 200)
        if favorites is None:
            continue
        for favorite in favorites:
            file_name = file_manager.assemble_datetime_file_name(favorite["created_at"])
            directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "favorites", screen_name)
            # skip saving favorites if already got
            if file_manager.exists_file(directory_path, file_name):
                logger.debug("already exists")
                break
            file_manager.save_json_dict_as_json_format(directory_path, file_name, favorite)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("command", help="the command you want to run")
    arg_parser.add_argument("target_screen_name", nargs="*", help="screen name of the target name")
    arg_parser.add_argument("-q", "--quiet", required=False, action="store_true", help="do not output log")
    args = arg_parser.parse_args()

    # set logging configuration
    logging_level = logging.DEBUG
    logger.setLevel(logging_level)
    if args.quiet == True:
        logging_level = logging.NOSET
        logger.setLevel(logging_level)

    if args.command == "retrieve_user_timelines":
        retrieve_user_timelines(args, logging_level)
    elif args.command == "retrieve_favorites":
        retrieve_favorites(args, logging_level)
    else:
        logger.critical("critical: %s is invalid command!!" % args.command)
        sys.exit(1)

