#!usr/bin/env python

"""
driver.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"


import logging
import os
import json
from board import Board
from agent import Agent

from datetime import datetime

FILE_CONFIG = "config.json"

# Constants
# Logging format for entries
LOGGING_FORMAT = "%(name)-32s %(asctime)s %(levelname)-8s %(message)s"
LOGGING_TIME_FORMAT = "%H:%M:%S"
DEFAULT_LOGGING_LEVEL = logging.DEBUG
LOG_NAME = "driver"


# Global variables
log = logging.getLogger(LOG_NAME)
start_time = datetime.now()
config = {"log_dir": "logs/", "log_ext": ".txt"}
boards = {}


def main():
    initialize_log()
    b = Board()
    a = Agent(agent_type=Agent.TYPE_PLAYER)
    a.take_turn()
    print("Hello World!")


def create_boards():
    global boards


def initialize_log():
    global start_time
    if not os.path.exists(config["log_dir"]):
        os.makedirs(config["log_dir"])
        log.warning("Creating log directory")
    file_name = f"{config['log_dir']}{start_time.strftime('%Y_%m_%d_%H_%M_%S')}{config['log_ext']}"
    logging.basicConfig(filename=file_name, level=DEFAULT_LOGGING_LEVEL, format=LOGGING_FORMAT,
                        datefmt=LOGGING_TIME_FORMAT)


def load_config():
    """
    Loads config options from the config file
    :return: None
    """
    log.debug(f"Attempting to load {FILE_CONFIG!r}")
    with open(FILE_CONFIG, "r") as json_file:
        data = json.load(json_file)
    for data_key in data.keys():
        config[data_key] = data[data_key]
        log.debug(f"Loaded config field {data_key!r} with value {data[data_key]!r}")
    log.debug(f"{FILE_CONFIG!r} loaded, {len(data)} config options loaded")


if __name__ == "__main__":
    main()
