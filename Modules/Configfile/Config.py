import os
import json
from datetime import datetime

from Modules.Configfile.App_Preferences_Data import app_preferences_data
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
        self.current_break_pattern = []
        self.break_patterns = []
        self.file_backup_names = []
        self.file_backup_locations = []
        self.preset_name = []
        self.preset_source = []
        self.preset_destination = []
        self.preset_application_location = []

        self.pattern_options = []

        # Define default variables
        self.try_create_folder("Icons")
        self.check_if_config_exists()

    def check_if_config_exists(self):
        if os.path.exists("User config/Config.json"):
            # If the configfile exists
            self.load_config()
        else:
            # Create Config.json if it doesn't exist
            self.generate_config_file()

    def load_app_preferences(self):
        if not os.path.exists("User config/App_preferences.json"):
            self.create_project_preferences_file()
        self.get_break_pattern()
        self.get_pattern_options()

    def load_config(self):
        # This function runs if the configfile already exists,
        # And loads in all the data from the json file
        with open("User config/Config.json", "r") as jsonFile:
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
            self.preset_source = file["preset_source"]
            self.preset_destination = file["preset_destination"]
            self.preset_application_location = file["preset_application_location"]
        self.get_number_of_lessons_today()
        self.load_app_preferences()

    def get_number_of_lessons_today(self):
        try:
            self.number_of_lessons_today = self.number_of_lessons[datetime.today().weekday()]
        except IndexError:
            self.number_of_lessons_today = self.number_of_lessons[4]

    def generate_config_file(self):
        # This function runs if the configfile doesn't exist
        # The function generates Config.json with default values
        self.try_create_folder("User config")
        self.create_project_preferences_file()
        with open("User config/Config.json", "w") as jsonFile:
            jsonFile.write(json.dumps(self.data, indent=3))
        self.load_config()

    def get_break_pattern(self):
        with open("User config/App_preferences.json") as file:
            data = json.loads(file.read())
            break_patterns = {}
            for i, pattern in enumerate(data["break_patterns"]):
                break_pattern = data["break_patterns"][i][1]
                combined_break_patterns = [(pattern[0], pattern[1]) for pattern in break_pattern]
                break_patterns[pattern[0]] = combined_break_patterns
            self.break_patterns = break_patterns
            self.current_break_pattern = break_patterns[self.clock_mode]

    def get_pattern_options(self):
        with open("User config/App_preferences.json") as file:
            data = json.loads(file.read())
            for i, pattern in enumerate(data["break_patterns"]):
                self.pattern_options.append(pattern[0])

    @staticmethod
    def create_project_preferences_file():
        file = "User config/App_preferences.json"
        if not os.path.exists(file):
            with open(file, "w") as app_preferences:
                app_preferences.write(json.dumps(app_preferences_data, indent=2))

    @staticmethod
    def try_create_folder(path):
        # Create Icons folder if it doesn't exist
        if not os.path.exists(path):
            os.makedirs(path)
