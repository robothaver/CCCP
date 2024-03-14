import os
import json
from Assets import Assets
from datetime import datetime
from Modules.Configfile.Config_Data import config_data


class Configfile:
    def __init__(self):
        # This function generates and loads in the configfile

        self.data = config_data

        # Define variables
        self.theme = ""
        self.custom_themes = True
        self.clock_mode = ""
        self.number_of_lessons = []
        self.reminder_activation = 0
        self.number_of_lessons_today = 0
        self.starting_page = 0
        self.end_of_lesson_reminder = True
        self.enable_top_theme_selector = True
        self.enable_primary_notifier = True
        self.enable_secondary_notifier = True
        self.enable_progress_bar = True
        self.current_page = 0
        self.browser = ""
        self.image_locations = []
        self.program_locations = []
        self.program_names = []
        self.project_output_locations = []
        self.project_names = []
        self.break_pattern = []
        self.file_backup_names = []
        self.file_backup_locations = []
        self.preset_name = []
        self.preset_input = []
        self.preset_output = []
        self.preset_application_location = []

        # Define default variables
        self.check_if_icons_folder_exists()
        self.check_if_config_exists()

    @staticmethod
    def check_if_icons_folder_exists():
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
            self.custom_themes = file['custom_themes']
            self.clock_mode = file['clock_mode']
            self.reminder_activation = file['reminder_activation']
            self.starting_page = file['starting_page']
            self.end_of_lesson_reminder = file['end_of_lesson_reminder']
            self.enable_top_theme_selector = file['enable_top_theme_selector']
            self.enable_primary_notifier = file['enable_primary_notifier']
            self.enable_secondary_notifier = file['enable_secondary_notifier']
            self.enable_progress_bar = file['enable_progress_bar']
            self.current_page = file['current_page']
            self.browser = file['browser']
            self.number_of_lessons = file['number_of_lessons']
            self.image_locations = file["image_locations"]
            self.program_locations = file["program_locations"]
            self.program_names = file["program_names"]
            self.project_output_locations = file["project_output_locations"]
            self.project_names = file["project_names"]
            self.file_backup_names = file["file_backup_names"]
            self.file_backup_locations = file["file_backup_locations"]
            self.preset_name = file["preset_name"]
            self.preset_input = file["preset_input"]
            self.preset_output = file["preset_output"]
            self.preset_application_location = file["preset_application_location"]
        self.get_clock_mode()
        self.get_number_of_lessons_today()

    def get_number_of_lessons_today(self):
        try:
            self.number_of_lessons_today = self.number_of_lessons[datetime.today().weekday()]
        except IndexError:
            self.number_of_lessons_today = self.number_of_lessons[4]

    def generate_config_file(self):
        # This function runs if the configfile doesn't exist
        # The function generates Config.json with default values
        self.data["theme"] = "darkly"
        self.data["clock_mode"] = "45_10"
        self.data["number_of_lessons"] = Assets.default_number_of_lessons
        for x, value in enumerate(range(13)):
            self.data["image_locations"].append(Assets.default_image_locations)
            self.data["program_locations"].append("default")
            self.data["program_names"].append(f"Button_{x}")
        datas = json.dumps(self.data, indent=3)
        with open("Config.json", "w") as jsonFile:
            jsonFile.write(datas)
        self.load_config()

    def get_clock_mode(self):
        # This function runs whenever the config gets loaded
        if self.clock_mode == "45_10":
            self.break_pattern = Assets.break_pattern_45_10
        elif self.clock_mode == "35_10":
            self.break_pattern = Assets.break_pattern_35_10
        elif self.clock_mode == "40_10":
            self.break_pattern = Assets.break_pattern_40_10
        else:
            self.break_pattern = Assets.break_pattern_35_05
