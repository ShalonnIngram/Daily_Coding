# create a script that counts the number of files in your Desktop directory & subdirectories, do not include folders
# find /Users/cianikaingram/Desktop -type f | wc -l
import os
from pathlib import Path

def count_files_with_os(path):
    total = 0
    for base, subdirs, files in os.walk(path):
        for file in files:
            total += 1
        return total

# does not search through subdirectories
def count_files_with_scandir(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += count_files_with_scandir(entry)
    return total


# like scandir, will only list items in the direct directory
# you will need to recursively search thru the sub directories to get everything
def count_files_with_pathlib(path):
    total = 0
    for entry in Path(path).iterdir():
        if entry.is_file():
            total += 1
        else:
            total += count_files_with_pathlib(entry)
    return total
