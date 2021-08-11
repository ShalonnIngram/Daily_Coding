import json

def display_json():
    with open('file.json') as f:
        content_json = json.load(f)
        print(content_json)

def display_name_from_json():
    with open('file.txt') as f:
        content_json = json.load()
        print("this is the value from the key", content_json['artist'])

   
if __name__ == "__main__":
