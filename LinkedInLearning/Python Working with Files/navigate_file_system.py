import os

def display_cwd():
    cwd = os.getcwd()
    print("Current working directory:", cwd)

def up_one_directory_level():
    os.chdir("../")

# use the iterator scandir (more performant & retrieves more information) or can listdir
def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)

if __name__ == "__main__":
