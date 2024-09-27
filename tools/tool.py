#!/bin/python3

import logging

from package.module import hello_world

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    hello_world()
    logger.info("end")


if __name__ == "__main__":
    main()
