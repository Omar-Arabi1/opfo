import os
import json
import shutil

def organize_files(config_file: str) -> None:
    with open(config_file, 'r', encoding='utf-8') as file:
        paths: dict = json.load(file)

    current_working_dir = os.getcwd()
    for file in os.listdir(current_working_dir):
        _, file_ext = os.path.splitext(file)
        path_to_ext = paths.get(file_ext)
        if path_to_ext is not None:
            shutil.move(file, path_to_ext)