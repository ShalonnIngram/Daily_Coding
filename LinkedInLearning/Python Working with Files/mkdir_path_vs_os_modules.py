import os
from pathlib import Path

# will create directory wherever this file is ran
def make_logs_dir():
    try:
        os.mkdir('directory_path')
    except FileExistsError as ex:
        print("logs directory already exists")

# creates directory & prevents errors and duplicates - more cleaner
def make_output_dir():
    dir_path = Path("path")
    dir_path.mkdir(exist_ok=True)


if __name__ == "__main__":
