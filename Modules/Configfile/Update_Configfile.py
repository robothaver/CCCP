import json


class UpdateConfigfile:
    # This class updates the Config.json
    def __init__(self, key, value):
        with open("Config.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data[key] = value
        with open("Config.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=3)
