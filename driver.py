#!usr/bin/env python

"""
driver.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"


import logging
import os

from datetime import datetime

FILE_CONFIG = "config.json"

# Constants
# Logging format for entries
LOGGING_FORMAT = "%(name)-32s %(asctime)s %(levelname)-8s %(message)s"
# Logging format for times
LOGGING_TIME_FORMAT = "%H:%M:%S"
# Default logging level
DEFAULT_LOGGING_LEVEL = logging.DEBUG
LOG_NAME = "driver"
start_time = datetime.now()

# Global variables
log = logging.getLogger(LOG_NAME)
config = {"log_dir": "logs/", "log_ext": ".txt"}


def main():
    initialize_log()
    print("Hello World!")


def initialize_log():
    global start_time
    if not os.path.exists(config["log_dir"]):
        os.makedirs(config["log_dir"])
        log.warning("Creating log directory")
    file_name = f"{config['log_dir']}{start_time.strftime('%Y_%m_%d_%H_%M_%S')}{config['log_ext']}"
    logging.basicConfig(filename=file_name, level=DEFAULT_LOGGING_LEVEL, format=LOGGING_FORMAT,
                        datefmt=LOGGING_TIME_FORMAT)


if __name__ == "__main__":
    main()
