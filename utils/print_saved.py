import json

def print_saved():
    with open('passwords_data.json', 'r') as fp:
        data = json.load(fp)
        print(data)
