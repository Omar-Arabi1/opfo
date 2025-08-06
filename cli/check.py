import json
import os
import logging
import sys

def check_config(config_file: str) -> bool:
    is_ok = True
    with open(config_file, 'r', encoding='utf-8') as file:
        try:
            config: dict = json.load(file)
        except json.decoder.JSONDecodeError as e:
            logging.fatal(f" {e}")
            sys.exit(1)

    for extension, ext_dir in config.items():
        if extension[0] != ".":
            logging.error(f" extension {extension} does not start with .")
            is_ok = False
        
        if os.path.isfile(ext_dir):
            logging.error(f" the default path {ext_dir} to the extension {extension} is a file, hint: make it a dir")
            is_ok = False
        
        if not os.path.exists(ext_dir):
            logging.error(f" the default path {ext_dir} to the extension {extension} does not exist")
            is_ok = False
    

    return is_ok