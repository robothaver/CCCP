import os
import json
from Assets import Assets


class Configfile:
    def __init__(self):
        # This function generates and loads in the configfile

        # Define variables
        self.theme = ""
        self.clock_mode = ""
        self.class_numbers = []
        self.starting_page = 0
        self.end_of_lesson_reminder = 0
        self.top_theme_selector = 1
        self.top_end_of_lesson_timer = 1
        self.top_lesson_number = 1
        self.current_page = 0
        self.browser = ""
        self.show_files_being_copied_in_cmd = 1
        self.image_locations = []
        self.program_locations = []
        self.program_names = []
        self.file_output_locations = []
        self.break_pattern = []
        self.file_backup_names = []
        self.file_backup_locations = []
        self.preset_name = []
        self.preset_input = []
        self.preset_output = []
        self.preset_application_location = []

        # Define default variables
        self.data = {
            "theme": "",
            "clock_mode": "",
            "starting_page": 0,
            "class_numbers": [],
            "end_of_lesson_reminder": 1,
            "top_theme_selector": 1,
            "top_end_of_lesson_timer": 1,
            "top_lesson_number": 1,
            "current_page": 0,
            "browser": "google",
            "show_files_being_copied_in_cmd": 1,
            "image_locations": [],
            "program_locations": [],
            "program_names": [],
            "file_output_locations": [],
            "file_backup_names": [],
            "file_backup_locations": [],
            "preset_name": [],
            "preset_input": [],
            "preset_output": [],
            "preset_application_location": [],
        }
        self.check_if_icons_folder_exists()
        self.check_if_config_exists()

    def check_if_icons_folder_exists(self):
        # Create Icons folder if it doesn't exist
        if not os.path.exists("./Icons"):
            os.makedirs("./Icons")

    def check_if_config_exists(self):
        if os.path.exists("./Config.json"):
            # If the configfile exists
            self.load_config()
        else:
            # Create Config.json if it doesn't exist
            self.generate_config_file()

    def load_config(self):
        # This function runs if the configfile already exists,
        # And loads in all the data from the json file
        with open("Config.json", "r") as jsonFile:
            file = json.load(jsonFile)
            self.theme = file['theme']
            self.clock_mode = file['clock_mode']
            self.class_numbers = file['class_numbers']
            self.starting_page = file['starting_page']
            self.end_of_lesson_reminder = file['end_of_lesson_reminder']
            self.top_theme_selector = file['top_theme_selector']
            self.top_end_of_lesson_timer = file['top_end_of_lesson_timer']
            self.top_lesson_number = file['top_lesson_number']
            self.current_page = file['current_page']
            self.browser = file['browser']
            self.show_files_being_copied_in_cmd = file['show_files_being_copied_in_cmd']
            self.image_locations = file["image_locations"]
            self.program_locations = file["program_locations"]
            self.program_names = file["program_names"]
            self.file_output_locations = file["file_output_locations"]
            self.file_backup_names = file["file_backup_names"]
            self.file_backup_locations = file["file_backup_locations"]
            self.preset_name = file["preset_name"]
            self.preset_input = file["preset_input"]
            self.preset_output = file["preset_output"]
            self.preset_application_location = file["preset_application_location"]
        self.set_clock_mode()

    def generate_config_file(self):
        # This function runs if the configfile doesn't exist
        # The function generates Config.json with default values
        for x, value in enumerate(range(13)):
            self.data["theme"] = "darkly"
            self.data["clock_mode"] = "45_10"
            self.data["image_locations"].append(Assets.default_image_locations)
            self.data["program_locations"].append("default")
            self.data["program_names"].append(f"Button_{x}")
        datas = json.dumps(self.data, indent=3)
        with open("Config.json", "w") as jsonFile:
            jsonFile.write(datas)
        self.load_config()

    def set_clock_mode(self):
        # This function runs whenever the config gets loaded
        if self.clock_mode == "45_10":
            self.break_pattern = Assets.break_pattern_45_10
        elif self.clock_mode == "35_10":
            self.break_pattern = Assets.break_pattern_35_10
        elif self.clock_mode == "40_10":
            self.break_pattern = Assets.break_pattern_40_10
        else:
            self.break_pattern = Assets.break_pattern_35_05
