from argparse import Namespace
import argparse

class Cli:
    def setup(self) -> Namespace:
        parser = argparse.ArgumentParser(prog="opfo", description="opfo is an advanced file organizer implemented in python")
        parser.add_argument("-V", "--version", action="version",version=f"%(prog)s 0.1.0")
        parser.add_argument("-c", "--check", action="store_true", help="check if the current config file is valid")
        
        return parser.parse_args()