from Modules.Configfile.Config import Configfile
from Modules.Dialogs.Create_Empty_Project.Generate_Empty_Project import GenerateEmptyProject
from Modules.Dialogs.Manage_Project_Output_Locations import ManageProjectOutputLocations
from Modules.Dialogs.Project_Generated_Dialog.Project_Generated_Dialog import ProjectGeneratedDialog
from Modules.Dialogs.Change_Project_Names.Change_Project_Names import ChangeProjectNames
from Modules.Pages.Project_Generator.Project_Generator import ProjectGenerator
from Modules.Pages.Project_Generator.UI.Project_Generator_UI import ProjectGeneratorUI
from Modules.Utilities.Open_Path_In_Explorer import open_path_in_explorer


class ProjectGeneratorPage(ProjectGeneratorUI):
    def __init__(self, master, config):
        super().__init__(master)
        # Define variables
        self.config = config

        self.web_project_generator_btn.config(command=self.generate_web_project)
        self.python_project_generator_btn.config(command=self.generate_python_project)
        self.empty_project_generator_btn.config(command=self.open_empty_project_dialog)

        self.open_project_btn.config(command=self.open_project_location)
        self.manage_output_locations_button.config(command=self.add_output_location)
        self.manage_project_names_btn.config(command=self.change_project_names)

        self.file_output_changer.config(textvariable=self.file_output_var)
        self.file_output_changer.set_menu(None, *self.config.project_output_locations)

        self.file_output_var.trace("w", self.change_page_state)

        self.set_button_states("disabled")

    def open_project_location(self):
        open_path_in_explorer(self.file_output_var.get())

    def update_menu(self):
        self.config = Configfile()
        self.file_output_changer.set_menu(None, *self.config.project_output_locations)
        if len(self.config.project_output_locations) == 0 or self.file_output_var.get() \
                not in self.config.project_output_locations:
            self.file_output_var.set("Select project output location")

    def change_project_names(self):
        ChangeProjectNames(self.master_container)

    def change_page_state(self, *args):
        if self.file_output_var.get() != self.default_location_message:
            self.set_button_states("enabled")
        else:
            self.set_button_states("disabled")

    def generate_web_project(self):
        file = ProjectGenerator(self.file_output_var.get())
        file.generate_web_project()
        if file.is_path_valid():
            ProjectGeneratedDialog(self.master_container, file.path_to_project)

    def generate_python_project(self):
        file = ProjectGenerator(self.file_output_var.get())
        file.generate_python_project()
        if file.is_path_destination_valid:
            ProjectGeneratedDialog(self.master_container, file.path_to_project)

    def generate_empty_project(self, project_subfolder):
        file = ProjectGenerator(self.file_output_var.get())
        file.generate_empty_project(project_subfolder)
        if file.is_path_destination_valid:
            ProjectGeneratedDialog(self.master_container, file.path_to_project)

    def open_empty_project_dialog(self):
        GenerateEmptyProject(self.master_container, self.generate_empty_project)

    def set_button_states(self, state):
        self.python_project_generator_btn.config(state=state)
        self.web_project_generator_btn.config(state=state)
        self.empty_project_generator_btn.config(state=state)
        self.open_project_btn.config(state=state)

    def add_output_location(self):
        ManageProjectOutputLocations(self.master_container, self.update_menu)
