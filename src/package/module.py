import logging

logger = logging.getLogger(__name__)


def say_hello(name: str):
    logger.debug(f"Got: {name}")
    print(f"Hello {name}")
