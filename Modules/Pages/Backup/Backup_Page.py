from Modules.Configfile.Config import Configfile
from Modules.Dialogs.Change_Backup_Locations.Change_Backup_Locations import ChangeBackupLocations
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
import os
import shutil
import threading
import time
import ttkbootstrap as ttk

from Modules.Pages.Backup.UI.Backup_UI import BackupUI


class BackupPage(BackupUI):
    def __init__(self, master, config):
        super().__init__(master)
        # Define variables
        self.config = config
        self.master = master
        self.start_time = datetime
        self.end_time = datetime
        self.thread = threading.Thread
        self.error = None

        self.progress = 0
        self.files_to_backup = []
        self.backup_names = []

        # Check buttons
        self.check_button_variables = []
        self.not_found = []

        # Generate check button widgets
        self.generate_widgets()

        # Pack files to include frame
        if len(config.file_backup_locations) != 0:
            self.files_to_include_frame.pack(pady=15)

        self.add_new_option_button.config(command=self.change_backup_options)
        self.back_files_up_button.config(command=self.start_backup)


    def change_backup_options(self):
        ChangeBackupLocations(self.master, self.update_page)

    def clear_widgets(self):
        for widget in self.location_container.winfo_children():
            widget.destroy()

    def generate_widgets(self):
        self.check_button_variables.clear()
        for i, file_backup_name in enumerate(self.config.file_backup_names):
            # Create new check button
            new_variable = ttk.IntVar(value=1)
            new_button = ttk.Checkbutton(master=self.location_container, text=file_backup_name,
                                         style="Checkbutton", variable=new_variable)
            # Append button
            new_button.pack(padx=10, pady=5, anchor="w")
            self.check_button_variables.append(new_variable)

    def update_page(self):
        self.config = Configfile()
        self.clear_widgets()
        self.generate_widgets()
        if len(self.config.file_backup_locations) != 0:
            self.files_to_include_frame.pack(pady=15)
        else:
            self.files_to_include_frame.pack_forget()

    def work(self):
        save_folder_name = time.strftime("%Y-%m-%d %H-%M-%S")
        progress = 0
        self.generate_backup_folders(save_folder_name)
        output_path = f"Backups/{save_folder_name}"
        for i in range(len(self.files_to_backup)):
            progress += 1
            progress_bar_value = round((progress / len(self.files_to_backup)) * 100, 2)
            self.try_copy_file(self.files_to_backup[i], f"{output_path}/{self.backup_names[i]}")
            # self.progress_bar.configure(amountused=progress_bar_value)
            if self.error is not None:
                exit()

    def try_copy_file(self, file, destination):
        file = file.replace("[HOME]", os.path.expanduser("~"))
        if os.path.exists(file):
            try:
                shutil.copytree(file, destination, dirs_exist_ok=True)
            except Exception as ex:
                self.error = ex.args
        else:
            self.not_found.append(file)

    def check_thread_state(self):
        if not self.thread.is_alive():
            print("finished")
            print(self.not_found)
            if self.error is not None:
                Messagebox.show_error(title="Error", message=str(self.error))
            if len(self.not_found) != 0:
                files_not_found = "\n".join(self.not_found)
                Messagebox.show_error(title="Files not found", message=f"Files not found:\n{files_not_found}")
            self.back_files_up_button.config(state="enabled")
        else:
            print("RUNNING")
            self.master.after(1000, self.check_thread_state)

    def start_backup(self):
        self.get_files_to_backup()
        if len(self.files_to_backup) != 0:
            self.start_thread()
        else:
            Messagebox.show_warning(title="Warning", message="You must set the files to backup!")

    def start_thread(self):
        self.error = None
        self.not_found.clear()
        self.files_to_backup.clear()
        self.backup_names.clear()

        # self.progress_bar.configure(amountused=0)
        self.get_files_to_backup()

        self.back_files_up_button.config(state="disabled")
        self.thread = threading.Thread(target=self.work, daemon=True)
        self.thread.start()
        self.check_thread_state()

    def get_files_to_backup(self):
        for i, var in enumerate(self.check_button_variables):
            if var.get() == 1:
                self.files_to_backup.append(self.config.file_backup_locations[i])
                self.backup_names.append(self.config.file_backup_names[i])

    def show_copy_finished_time(self):
        delta = self.end_time - self.start_time
        Messagebox.show_info(title="Copying finished", message=f"Copying finished in {delta}")

    @staticmethod
    def generate_backup_folders(save_folder_name):
        if not os.path.exists("Backups"):
            os.mkdir("Backups")
        else:
            if not os.path.exists(f"Backups/{save_folder_name}"):
                os.mkdir(f"Backups/{save_folder_name}")
