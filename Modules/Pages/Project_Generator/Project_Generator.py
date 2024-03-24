from ttkbootstrap.dialogs.dialogs import Messagebox
from Modules.Utilities import Assets
import os
import time


class ProjectGenerator:
    def __init__(self, output_location):
        self.output_location = output_location
        self.path_to_project = ""
        self.is_path_destination_valid = False

    def generate_empty_project(self, subfolder):
        if self.is_path_valid():
            folder_name = time.strftime("%Y-%m-%d")
            if subfolder == "No subfolder":
                self.path_to_project = f"{self.output_location}/{folder_name}"
                self.generate_project_folder(self.path_to_project)
            else:
                self.path_to_project = f"{self.output_location}/{subfolder}/{folder_name}"
                self.generate_project_folder(f"{self.output_location}/{subfolder}")
                self.generate_project_folder(self.path_to_project)

    @staticmethod
    def generate_project_folder(path_to_project):
        if not os.path.exists(path_to_project):
            os.mkdir(path_to_project)

    @staticmethod
    def create_current_folder(path_to_project, folder_name):
        current_folder_path = f"{path_to_project}/{folder_name}"
        exists = False
        if not os.path.exists(current_folder_path):
            os.mkdir(current_folder_path)
        else:
            choice = Messagebox.yesno(title="Project already exists",
                                      message="Project already exists. Would you like to over write?")
            if choice == "Yes":
                exists = False
            else:
                exists = True
        return exists

    def is_path_valid(self):
        if not os.path.exists(self.output_location):
            Messagebox.show_error(title="Error", message="Path does not exists!")
            return False
        self.is_path_destination_valid = True
        return True

    def generate_web_project(self):
        if self.is_path_valid():
            folder_name = time.strftime("%Y-%m-%d")
            self.path_to_project = f"{self.output_location}/Web Projects"
            self.generate_project_folder(self.path_to_project)
            if not self.create_current_folder(self.path_to_project, folder_name):
                # Create html file
                with open(f"{self.path_to_project}/{folder_name}/index.html", "w") as html_file:
                    html_file.write(Assets.html_boilerplate)
                # Create CSS folder and file
                if not os.path.exists(f"{self.path_to_project}/{folder_name}/CSS"):
                    os.mkdir(f"{self.path_to_project}/{folder_name}/CSS")
                css_file = open(f"{self.path_to_project}/{folder_name}/CSS/styles.css", "w")
                css_file.close()
                # Create js file
                js_file = open(f"{self.path_to_project}/{folder_name}/index.js", "w")
                js_file.close()

    def generate_python_project(self):
        if self.is_path_valid():
            folder_name = time.strftime("%Y-%m-%d")
            self.path_to_project = f"{self.output_location}/Python Projects"
            self.generate_project_folder(self.path_to_project)
            if not self.create_current_folder(self.path_to_project, folder_name):
                file = open(f"{self.path_to_project}/{folder_name}/main.py", "w")
                file.close()
