from pathlib import Path
import os
import json

class Config:
    def create_config_file(self) -> str:
        home_dir = Path.home()
        config_file_path = os.path.join(home_dir, '.opfo', "opfo.json")
        config_dir_name = os.path.dirname(config_file_path)
        if not os.path.exists(config_file_path):
            os.makedirs(config_dir_name)
        return config_file_path


    def generate_default_config(self, file_path: str) -> None:
        default_config = {}
        extensions = ['.png', '.jpg', '.txt', '.mp4']
        ext_dirs = ['Pictures', 'Pictures', 'Documents', 'Videos']
        home_dir = Path.home()

        for extention, ext_dir in zip(extensions, ext_dirs):
            ext_dir_full_path = os.path.join(home_dir, ext_dir)
            if not os.path.exists(ext_dir_full_path):
                continue
            default_config.update({extention: ext_dir_full_path})

        if os.path.exists(file_path):
            return
        with open(file_path, 'w', encoding='utf-8') as config_file:
            json.dump(default_config, config_file, indent=4)