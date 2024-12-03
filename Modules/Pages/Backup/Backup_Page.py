from Modules.Configfile.Config import Configfile
from Modules.Dialogs.Change_Backup_Locations.Change_Backup_Locations import ChangeBackupLocations
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime, timedelta
import os
import shutil
import threading
import time
import ttkbootstrap as ttk

from Modules.Dialogs.Backup_Finished import BackupFinished
from Modules.Pages.Backup.UI.Backup_UI import BackupUI


class BackupPage(BackupUI):
    def __init__(self, master, config):
        super().__init__(master)
        # Define variables
        self.config = config
        self.master = master
        self.thread = threading.Thread
        self.error = None
        self.start_time = None
        self.end_time = None

        self.progress = 0
        self.files_to_backup = []
        self.backup_names = []

        # Check buttons
        self.check_button_variables = []
        self.not_found = []

        self.generate_widgets()

        # Pack files to include frame
        if len(config.file_backup_locations) != 0:
            self.right_container.grid(row=0, column=1, sticky="nsew", padx=15)

        self.add_new_option_button.config(command=self.change_backup_options)
        self.back_files_up_button.config(command=self.start_backup)
        self.select_all_btn.config(command=self.select_all)

    def select_all(self):
        state = 0 if self.check_button_variables[0].get() == 1 else 1
        for var in self.check_button_variables:
            var.set(state)

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
        self.progress_bar.configure(amountused=0)
        if len(self.config.file_backup_locations) != 0:
            self.right_container.grid(row=0, column=1, sticky="nsew", padx=15)
        else:
            self.right_container.grid_forget()

    def work(self):
        save_folder_name = time.strftime("%Y-%m-%d %H-%M-%S")
        progress = 0
        self.generate_backup_folders(save_folder_name)
        output_path = f"Backups/{save_folder_name}"
        for i in range(len(self.files_to_backup)):
            progress += 1
            progress_bar_value = round((progress / len(self.files_to_backup)) * 100, 2)
            if not os.path.isdir(self.files_to_backup[i]):
                os.mkdir(f"{output_path}/{self.backup_names[i]}")
            self.try_copy_file(self.files_to_backup[i], f"{output_path}/{self.backup_names[i]}/")
            self.progress_bar.configure(amountused=progress_bar_value)
            if self.error is not None:
                exit()

    def try_copy_file(self, file, destination):
        file = file.replace("[HOME]", os.path.expanduser("~"))
        if os.path.exists(file):
            try:
                if not os.path.isdir(file):
                    file_name = file.split("/")[-1]
                    shutil.copyfile(file, f"{destination}/{file_name}")
                else:
                    shutil.copytree(file, destination)
            except Exception as ex:
                self.error = ex.args
        else:
            self.not_found.append(file)

    def check_thread_state(self):
        if not self.thread.is_alive():
            self.end_time = datetime.now()
            if self.error is not None:
                Messagebox.show_error(title="Error", message=str(self.error))
            self.back_files_up_button.config(state="enabled")
            BackupFinished(self.master, self.get_finished_time(), self.not_found, len(self.files_to_backup))
        else:
            self.master.after(1000, self.check_thread_state)

    def reset_backup_state(self):
        self.error = None
        self.not_found.clear()
        self.files_to_backup.clear()
        self.backup_names.clear()
        self.progress_bar.configure(amountused=0)

    def start_backup(self):
        self.reset_backup_state()
        self.get_files_to_backup()
        if len(self.files_to_backup) != 0:
            self.start_thread()
        else:
            Messagebox.show_warning(title="Warning", message="You must select the files to backup!")

    def start_thread(self):
        self.back_files_up_button.config(state="disabled")
        self.start_time = datetime.now()
        self.thread = threading.Thread(target=self.work, daemon=True)
        self.thread.start()
        self.check_thread_state()

    def get_files_to_backup(self):
        for i, var in enumerate(self.check_button_variables):
            if var.get() == 1:
                self.files_to_backup.append(self.config.file_backup_locations[i])
                self.backup_names.append(self.config.file_backup_names[i])

    def get_finished_time(self):
        return timedelta(seconds=(self.end_time - self.start_time).seconds)

    @staticmethod
    def generate_backup_folders(save_folder_name):
        if not os.path.exists("Backups"):
            os.mkdir("Backups")
        else:
            if not os.path.exists(f"Backups/{save_folder_name}"):
                os.mkdir(f"Backups/{save_folder_name}")
