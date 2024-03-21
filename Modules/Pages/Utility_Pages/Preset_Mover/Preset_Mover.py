import os
import shutil
import subprocess
import threading

from ttkbootstrap.dialogs import Messagebox

from Modules.Configfile.Config import Configfile
from Modules.Dialogs.Change_Preset_Settings.Change_Preset_Settings import ChangePresetSettings
from Modules.Pages.Utility_Pages.Preset_Mover.UI.Preset_Mover_UI import PresetMoverUI


class PresetMover(PresetMoverUI):
    def __init__(self, master, show_dashboard, config):
        # Define variables
        super().__init__(master)
        self.thread = None
        self.master = master
        self.config = config

        self.back_button.config(command=show_dashboard)
        self.launch_application_button.config(command=self.launch_application)
        self.copy_to_computer_button.config(command=self.copy_save_to_pc)
        self.copy_from_computer_button.config(command=self.copy_save_from_pc)
        self.change_preset_settings.config(command=lambda: ChangePresetSettings(self.master, self.update_page))
        self.preset_selector_var.trace("w", self.load_preset)
        self.preset_selector.set_menu(None, *self.config.preset_name)

    def update_page(self):
        self.config = Configfile()
        self.preset_selector.set_menu(None, *self.config.preset_name)

    def load_preset(self, *args):
        index = self.config.preset_name.index(self.preset_selector_var.get())
        if self.config.preset_application_location[index] != "":
            self.launch_application_button.config(state="active")
        else:
            self.launch_application_button.config(state="disabled")

    @staticmethod
    def get_destination(source, destination):
        if os.path.exists(destination):
            if os.path.isfile(destination):
                des_path = destination.split("/")
                folder_name = "".join(des_path[-1].split(".")[0])
                del des_path[-1]
                destination = f'{"/".join(des_path)}/{folder_name}'
            else:
                destination = f"{destination}/{source.split('/')[-1]}"
        return destination

    def copy_files(self, source, destination):
        source = source.replace("[HOME]", os.path.expanduser("~"))
        try:
            if os.path.isdir(source):
                destination = self.get_destination(source, destination)
                os.mkdir(destination) if not os.path.exists(destination) else None
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy(src=source, dst=destination)
        except Exception as ex:
            Messagebox.show_error(title="Error", message=str(ex.args))

    def check_thread_state(self):
        if not self.thread.is_alive():
            self.set_button_state("active")
            Messagebox.show_info(title="Copying finished", message="Copying finished")
        else:
            self.master.after(1000, self.check_thread_state)

    def set_button_state(self, is_enabled):
        self.copy_to_computer_button.config(state=is_enabled)
        self.copy_from_computer_button.config(state=is_enabled)
        self.launch_application_button.config(state=is_enabled)

    def start_thread(self, source, destination):
        print(f"Copying {source} to {destination}")
        if os.path.exists(source):
            self.set_button_state("disabled")
            self.thread = threading.Thread(target=self.copy_files, daemon=True, args=[source, destination])
            self.thread.start()
            self.check_thread_state()
        else:
            Messagebox.show_error(title="Error", message="File not found!")

    def copy_save_to_pc(self):
        # This function gets called whenever the "copy save to pc" button is pressed
        if self.preset_selector_var.get() != "Select preset":
            index = self.config.preset_name.index(self.preset_selector_var.get())
            source = self.config.preset_source[index]
            destination = self.config.preset_destination[index]
            self.start_thread(source, destination)
        else:
            Messagebox.show_warning(title="Warning", message="You must select a preset first!")

    def copy_save_from_pc(self):
        if self.preset_selector_var.get() != "Select preset":
            index = self.config.preset_name.index(self.preset_selector_var.get())
            destination = self.config.preset_source[index]
            source = self.config.preset_destination[index]
            self.start_thread(source, destination)
        else:
            Messagebox.show_warning(title="Warning", message="You must select a preset first!")

    def launch_application(self):
        # This function gets called whenever the launch application button is pressed
        index = self.config.preset_name.index(self.preset_selector_var.get())
        try:
            os.startfile(self.config.preset_application_location[index])
        except FileNotFoundError:
            Messagebox.show_error(title="Error", message="Program not found!")
