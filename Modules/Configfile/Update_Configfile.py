import json


class UpdateConfigfile:
    # This class updates the Config.json
    def __init__(self, key, value, index=None):
        with open("Config.json", "r") as jsonFile:
            data = json.load(jsonFile)
        if index is not None:
            data[key][index] = value
        else:
            data[key] = value
        with open("Config.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=3)
