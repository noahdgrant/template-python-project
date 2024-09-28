#!/bin/python3

import logging

from package import say_hello

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    say_hello("Alice")
    logger.info("end")


if __name__ == "__main__":
    main()
