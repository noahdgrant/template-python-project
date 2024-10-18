import argparse
import logging
import logging.config
import os

import dotenv
import yaml

from package import say_hello

dotenv.load_dotenv()
LOGGER = os.getenv("LOGGER", "production")

with open("logging.yaml", "r") as file:
    config = yaml.safe_load(file.read())

logging.config.dictConfig(config)

# Change this to any of the 'loggers' options in logging.yaml
logger = logging.getLogger(LOGGER)
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
    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    # These options will be available to all subcommands they are passed to.
    # Doing it this way reduces to duplication needed to add these options to all
    # the the subparsers and lets the CLI API be...
    # cli-tool get logs --device AAAA
    # instead of...
    # cli-tool --device AAAA get logs
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument(
        "--log",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
    )

    say_parser = subparsers.add_parser("say", help="Say various greatings")
    say_subparsers = say_parser.add_subparsers(title="subcommands", dest="resource")

    hello_parser = say_subparsers.add_parser(
        "hello", parents=[common_parser], help="Say hello to someone"
    )
    hello_parser.add_argument("name", help="The name to welcome")

    bye_parser = say_subparsers.add_parser(
        "bye", parents=[common_parser], help="Say bye to someone"
    )
    bye_parser.add_argument("name", help="The name to say bye to")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        exit(1)

    if args.resource is None:
        subparsers.choices[args.command].print_help()
        exit(1)

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
