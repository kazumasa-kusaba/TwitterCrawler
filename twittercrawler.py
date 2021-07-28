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

    # TODO: replace "XXX" with the each appropriate variables
    twitter_api = TwitterApi("XXX", "XXX", "XXX", "XXX")

    # TODO: replace "XXX" with the appropriate variable
    file_manager = FileManager("XXX")

    for screen_name in screen_names:
        logger.debug(screen_name)
        # TODO: handle an exception properly
        twitter_api.retrieve_user_timeline(screen_name, 200)

def retrieve_favorites(args):
    screen_names = args.target_screen_name
    logger.debug(screen_names)

    # TODO: replace "XXX" with the each appropriate variables
    twitter_api = TwitterApi("XXX", "XXX", "XXX", "XXX")

    # TODO: replace "XXX" with the appropriate variable
    file_manager = FileManager("XXX")

    # TODO: handle an exception properly
    for screen_name in screen_names:
        logger.debug(screen_name)
        # TODO: handle an exception properly
        twitter_api.retrieve_favorite(screen_name, 200)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--command", required=True, help="the command you want to run")
    arg_parser.add_argument("--target-screen-name", nargs="*", required=True, help="screen name of the target name")
    arg_parser.add_argument("--quite", required=False, help="do not output log")
    args = arg_parser.parse_args()

    if args.command == "retrieve_user_timelines":
        retrieve_user_timelines(args)
    elif args.command == "retrieve_favorites":
        retrieve_favorites(args)
    else:
        logger.error("error: %s is invalid command!!" % args.command)
        sys.exit(1)

