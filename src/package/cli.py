import argparse
import logging

from package import say_hello

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parses arguments passed at the command line"""

    parser = argparse.ArgumentParser(prog="package", description="Example cli")
    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    say_parser = subparsers.add_parser("say", help="Say various greatings")
    say_subparsers = say_parser.add_subparsers(title="subcommands", dest="resource")

    hello_parser = say_subparsers.add_parser("hello", help="Say hello to someone")
    hello_parser.add_argument("name", help="The name to welcome")

    bye_parser = say_subparsers.add_parser("bye", help="Say bye to someone")
    bye_parser.add_argument("name", help="The name to say bye to")

    return parser.parse_args()


def cli():
    """Executes command from parser"""

    args = parse_args()
    if args.command == "say":
        if args.resource == "hello":
            say_hello(args.name)
        elif args.reouce == "bye":
            logger.error("Unimplemented")
        else:
            logger.error("Unknown 'say' subcommand")
    else:
        logger.error("Unknown subcommand")
