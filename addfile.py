import os
import shutil


def add_file(filepath):
    if os.path.exists(filepath) and os.path.isfile(filepath):
        shutil.copy(filepath, '.\\texts\\')
        return True
    else:
        return False
