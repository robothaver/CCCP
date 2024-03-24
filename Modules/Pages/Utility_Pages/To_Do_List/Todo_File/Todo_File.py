import json
import os.path

TODO_File = "To_Do_List.json"


class TodoFile:
    def __init__(self):
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
        if os.path.exists(TODO_File):
            # If json file already exists, load it in
            with open(TODO_File) as jsonfile:
                data = json.load(jsonfile)
                self.titles = data['title']
                self.descriptions = data['description']
                self.is_done = data['is_done']
        else:
            # Generate To_Do_List.json
            json_data = json.dumps(data, indent=3)
            with open(TODO_File) as file:
                file.write(json_data)

    def add_new_todo(self, title, description, is_done=0):
        self.titles.append(title)
        self.descriptions.append(description)
        self.is_done.append(is_done)

    def remove_todo(self, title):
        index = self.titles.index(title)
        del self.titles[index]
        del self.descriptions[index]
        del self.is_done[index]
