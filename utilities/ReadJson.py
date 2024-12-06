import json


def read_json(json_file_path):
    with open(json_file_path) as f:
        json_file = json.load(f)
    return json_file
