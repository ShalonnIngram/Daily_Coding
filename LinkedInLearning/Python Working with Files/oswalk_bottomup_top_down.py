# os.walk(path) can be used to generate the file names in a directory tree by walking either top down or bottom up
# bottom up will return files in finds in sub folder first
import os

# returns current directory path - dirpath, directory names - dirnames & files it contains
def top_down_walk():
    for dirpath, dirnames, files in os.walk('/Users/cianikaingram/Documents'):
        print("Directory:", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        for filename in files:
            print("Includes these files:")
        print()


def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('/Users/cianikaingram/Documents', ):
        print("Directory:", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        for filename in files:
            print("Includes these files:")
        print()

if __name__ == "__main__":
    bottom_up_walk()
