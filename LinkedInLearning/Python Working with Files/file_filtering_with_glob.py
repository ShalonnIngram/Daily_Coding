import glob
def display_pngs():
    png_files = glob.glob('*.png')
    print(png_files)

# return files with 'screenshot' in the name
def find_files():
    filtered_items = glob.glob("*screenshot")
    print(filtered_items)

# find files with keyword to look in directory and subdirectory
def find_files():
    for file in glob.iglob('*screenshot*',recursive=True):
        print(file)


if __name__ == "__main__":
    display_pngs("/Users/cianikaingram/Desktop")
