import argparse
import logging
import logging.config

import yaml

with open("logging.yaml", "r") as file:
    config = yaml.safe_load(file.read())

logging.config.dictConfig(config)

# Change this to any of the 'loggers' options in logging.yaml
logger = logging.getLogger("development")
root_logger = logging.getLogger()
# Configure the root logger to be the same the logger we select
# This way logs from other modules will behave the same as logs from this file
root_logger.setLevel(logger.level)
for handler in logger.handlers:
    root_logger.addHandler(handler)
root_logger.propagate = logger.propagate


def parse_args() -> argparse.Namespace:
    """Parses arguments passed at the command line"""

    parser = argparse.ArgumentParser(prog="cli-tool", description="Example cli")
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
    common_parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        default=False,
        help="Run on test environment",
    )
    common_group = common_parser.add_mutually_exclusive_group(required=True)
    common_group.add_argument("-s", "--serial", help="Device serial number")
    common_group.add_argument("-i", "--hardware", help="Device hardware ID")

    # Create the parser for the "get" command
    parser_get = subparsers.add_parser("get", help="Get resources from the device")
    get_subparsers = parser_get.add_subparsers(title="subcommands", dest="resource")

    # Create subcommands for "get"
    parser_get_logs = get_subparsers.add_parser(
        "logs", parents=[common_parser], help="Get logs from the device"
    )
    parser_get_logs.add_argument("from", help="Beginning date")
    parser_get_logs.add_argument("to", help="End date")

    get_subparsers.add_parser(
        "status", parents=[common_parser], help="Get status of the device"
    )

    # Create the parser for the "set" command
    parser_set = subparsers.add_parser("set", help="Set resources on the device")
    set_subparsers = parser_set.add_subparsers(title="subcommands", dest="resource")

    # Create subcommands for "set"
    parser_set_firmware = set_subparsers.add_parser(
        "firmware", parents=[common_parser], help="Set firmware on the device"
    )
    parser_set_firmware.add_argument("version", help="The version to set")

    parser_set_config = set_subparsers.add_parser(
        "config", parents=[common_parser], help="Set configuration on the device"
    )
    parser_set_config.add_argument("settings", help="The setting to configure")

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
    if args.command == "get":
        if args.resource == "logs":
            logger.info(
                f"Getting logs for device with serial: {args.serial} or hardware ID: {args.hardware}"
            )
        elif args.resource == "status":
            logger.info(
                f"Getting status for device with serial: {args.serial} or hardware ID: {args.hardware}"
            )
    elif args.command == "set":
        if args.resource == "firmware":
            logger.info(
                f"Setting firmware for device with serial: {args.serial} or hardware ID: {args.hardware}"
            )
        elif args.resource == "config":
            logger.info(
                f"Setting configuration for device with serial: {args.serial} or hardware ID: {args.hardware}"
            )
