# pathlib module represents file paths as objects instead of strings
# provide object oriented interface to the file system
# more efficient, more data per operation

from pathlib import Path

# returns name, parent, parents parents, name without extension, extension only
def print_directory_contents():
    entries = Path.cwd()

    # we can specify a specific directory
    # entries = Path('')
    # entries = Path.home()

    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())

if __name__ == "__main__":
    print_directory_contents()
