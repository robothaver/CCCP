import json


class UpdateToDoList:
    def __init__(self, key, index, value):
        # This class updates the To_Do_List.json
        with open("To_Do_List.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data[key][index] = value
        with open("To_Do_List.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=3)
