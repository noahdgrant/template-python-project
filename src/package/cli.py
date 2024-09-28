import argparse
import logging
import logging.config

import yaml

from package import say_hello

with open("logging.yaml", "r") as file:
    config = yaml.safe_load(file.read())

logging.config.dictConfig(config)

# Change this to any of the 'loggers' options in logging.yaml
logger = logging.getLogger("staging")
root_logger = logging.getLogger()
# Configure the root logger to be the same the logger we select
# This way logs from other modules will behave the same as logs from this file
root_logger.setLevel(logger.level)
for handler in logger.handlers:
    root_logger.addHandler(handler)
root_logger.propagate = logger.propagate


def parse_args() -> argparse.Namespace:
    """Parses arguments passed at the command line"""

    parser = argparse.ArgumentParser(prog="package", description="Example cli")
    parser.add_argument(
        "--log",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
    )

    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    say_parser = subparsers.add_parser("say", help="Say various greatings")
    say_subparsers = say_parser.add_subparsers(title="subcommands", dest="resource")

    hello_parser = say_subparsers.add_parser("hello", help="Say hello to someone")
    hello_parser.add_argument("name", help="The name to welcome")

    bye_parser = say_subparsers.add_parser("bye", help="Say bye to someone")
    bye_parser.add_argument("name", help="The name to say bye to")

    args = parser.parse_args()

    if args.log:
        numeric_level = getattr(logging, args.log.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError("Invalid log level: %s" % args.log)
        logger.setLevel(numeric_level)
        root_logger.setLevel(numeric_level)

    return args


def cli():
    """Executes command from parser"""
    args = parse_args()
    if args.command == "say":
        if args.resource == "hello":
            say_hello(args.name)
        elif args.resource == "bye":
            logger.error("Unimplemented")
        else:
            logger.error("Unknown 'say' subcommand")
    else:
        logger.error("Unknown subcommand")
