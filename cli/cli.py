from argparse import Namespace
import argparse
import sys

from .check import check_config

class Cli:
    def setup(self) -> Namespace:
        parser = argparse.ArgumentParser(prog="opfo", description="opfo is an advanced file organizer implemented in python")
        parser.add_argument("-V", "--version", action="version",version=f"%(prog)s 0.1.0")
        parser.add_argument("-c", "--check", action="store_true", help="check if the current config file is valid")
        
        return parser.parse_args()


    def route_options(self, args: Namespace, config_file: str) -> None:
        if args.check:
            is_ok = check_config(config_file=config_file)
            if not is_ok:
                sys.exit(1)
            print("All Good!")