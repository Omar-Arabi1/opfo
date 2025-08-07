import os

def is_hidden(file: str) -> bool:
    file_name = os.path.basename(file)
    if not file_name.startswith('.'):
        return False
    return True