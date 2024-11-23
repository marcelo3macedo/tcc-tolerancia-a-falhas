import json

def loadFileFromJson(file_path):
    with open(file_path, "r") as file:
        return json.load(file)