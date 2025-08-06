import json
import os

from custom_exceptions.config_exceptions import InvalidExtention, DefaultPathIsFile, DefaultPathDoesNotExist

def check_config(config_file: str) -> None:
    with open(config_file, 'r', encoding='utf-8') as file:
        config: dict = json.load(file)

    for extension, ext_dir in config.items():
        if extension[0] != ".":
            raise InvalidExtention(message="the extension does not start with .")
        
        if os.path.isfile(ext_dir):
            raise DefaultPathIsFile(message="the default path to the extension is a file, hint: make it a dir")
        
        if not os.path.exists(ext_dir):
            raise DefaultPathDoesNotExist(message="teh default path to the extension does not exist")
