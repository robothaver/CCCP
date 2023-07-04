import json
import os.path


class GenerateToDoFile:
    def __init__(self):
        # This class gets called by the ToDoFile class, and it generates and loads in the json file
        # Define variables
        self.titles = []
        self.descriptions = []
        self.is_done = []
        # Create default data
        data = {
            "title": [],
            "description": [],
            "is_done": []
        }
        if os.path.exists("To_Do_List.json"):
            # If json file already exists, load it in
            with open("To_Do_List.json", "r") as jsonfile:
                data = json.load(jsonfile)
                self.titles = data['title']
                self.descriptions = data['description']
                self.is_done = data['is_done']
        else:
            # Generate To_Do_List.json
            json_data = json.dumps(data, indent=3)
            with open("To_Do_List.json", "w") as file:
                file.write(json_data)
