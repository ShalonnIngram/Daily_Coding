# read text files

def print_file_content_one_line_at_a_time():
    with open('file.text', 'r') as f:
        line = f.readline()
        while line != '':
            print(line, end='')
            line = f.readline()# read text files

