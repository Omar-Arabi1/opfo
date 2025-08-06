import os
import json
import shutil

from util.get_logger import get_logger
from util.is_hidden import is_hidden

def organize_files(config_file: str, verbose: bool) -> None:
    logger = get_logger()
    with open(config_file, 'r', encoding='utf-8') as file:
        paths: dict = json.load(file)

    current_working_dir = os.getcwd()
    for file in os.listdir(current_working_dir):
        if os.path.isdir(file):
            continue
        if is_hidden(file=file):
            continue
        _, file_ext = os.path.splitext(file)
        path_to_ext = paths.get(file_ext)
        if path_to_ext is not None and verbose:
            shutil.move(file, path_to_ext)
            logger.info(f"{file} moved to {path_to_ext} dir")
        elif path_to_ext is not None:
            shutil.move(file, path_to_ext)
        elif path_to_ext is None and verbose:
            logger.warning(f"extension {file_ext} is not supported in the config")