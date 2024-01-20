import subprocess
import tkinter as tk
import ttkbootstrap as ttk
import os
import time
from ttkbootstrap.dialogs import Messagebox
from Modules.Dialogs.Change_Backup_Locations import ChangeBackupLocations
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from datetime import datetime


class BackupPage:
    def __init__(self, master, window, config):
        # Define variables
        self.window = window
        self.config = config
        self.start_time = datetime
        self.end_time = datetime

        self.backup_page = ttk.Frame(master)

        # Creating files to include frame
        files_to_include_frame = ttk.LabelFrame(master=self.backup_page, style="info", text="Files to include")

        # Check buttons
        self.check_button_variables = []
        self.check_buttons = []
        self.backup_output_locations = []
        self.backup_output_names = []

        # Configuring frame row settings
        for x in range(len(self.config.file_backup_names)):
            files_to_include_frame.rowconfigure(x, weight=1)

        # Generate check button widgets
        if not len(self.config.file_backup_names) == 0:
            # If backup options are not empty
            for i, file_backup_name in enumerate(self.config.file_backup_names):
                # Create new check button
                new_variable = ttk.IntVar(value=1)
                new_button = ttk.Checkbutton(master=files_to_include_frame, text=file_backup_name,
                                             style="Checkbutton", variable=new_variable)
                # Append button
                self.backup_output_locations.append(self.config.file_backup_locations[i])
                self.check_button_variables.append(new_variable)
                self.check_buttons.append(new_button)
                self.backup_output_names.append(self.config.file_backup_names[i])

            # Separating left and right side buttons
            left_buttons = []
            right_buttons = []
            for i, button in enumerate(self.check_buttons):
                if i % 2 == 0:
                    left_buttons.append(button)
                else:
                    right_buttons.append(button)

            # Packing buttons
            for i, button in enumerate(left_buttons):
                button.grid(column=0, row=i, padx=25, pady=10, sticky="w")
            for i, button in enumerate(right_buttons):
                button.grid(column=1, row=i, padx=25, pady=10, sticky="w")

            # Pack files to include frame
            files_to_include_frame.pack(pady=15)

        # Create progress meter
        # self.progress_meter = ttk.Meter(
        #     master=self.backup_page,
        #     metersize=200,
        #     padding=5,
        #     amountused=0,
        #     amounttotal=100,
        #     subtext="Done",
        #     style="info",
        #     textright="%")
        # self.progress_meter.pack(pady=15, padx=15)

        # Create show current files in cmd checkbutton
        self.show_current_files_in_cmd_var = tk.IntVar(value=self.config.show_files_being_copied_in_cmd)
        show_current_files_in_cmd_checkbutton = ttk.Checkbutton(self.backup_page, text="Show files being copied in cmd",
                                                                style="info round-toggle",
                                                                variable=self.show_current_files_in_cmd_var,
                                                                command=lambda: UpdateConfigfile(
                                                                    "show_files_being_copied_in_cmd",
                                                                    self.show_current_files_in_cmd_var.get()))
        show_current_files_in_cmd_checkbutton.pack(pady=10)

        # Create back files up button
        self.back_files_up_button = ttk.Button(
            master=self.backup_page,
            text="Start backup",
            width=25, style="info",
            command=self.backup)
        self.back_files_up_button.pack(pady=15)

        # Create add new option button
        self.add_new_option_button = ttk.Button(
            master=self.backup_page,
            text="Add new backup option",
            width=25, style="warning",
            command=lambda: ChangeBackupLocations(master))
        self.add_new_option_button.pack(pady=15)
        self.backup_page.pack(fill="both")

    def backup(self):
        # This function runs whenever the backup button is pressed, and it starts the backup process
        if not len(self.config.file_backup_names) == 0:
            # If backup options are not empty
            for x in self.backup_output_names:
                if x == "default":
                    Messagebox.show_warning(title="Warning", message="You must set what to backup first!")
            # Find files to include
            selected_directory_names = []
            selected_directories_to_backup = []
            for i, x in enumerate(self.check_button_variables):
                # If check button variable is 1 (checked)
                if x.get() == 1:
                    selected_directories_to_backup.append(self.backup_output_locations[i])
                    selected_directory_names.append(self.backup_output_names[i])

            # Create save folder (skip if already exists)
            if os.path.exists("./Save"):
                pass
            else:
                os.makedirs("./Save")

            # Create save folder with current date
            save_folder_name = time.strftime("%Y-%m-%d_%H-%M-%S")
            os.makedirs(f"./Save/{save_folder_name}")
            # Save from source to destination and update progress meter with the correct value

            meter = 0
            # Divide 100 by the number of selected options
            meter_update_var = 100 / len(selected_directories_to_backup)

            # Get errors
            files_not_found = []
            # Check if selected files exist
            existing_directory_names = []
            existing_directories = []
            self.start_time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            for i, directory in enumerate(selected_directories_to_backup):
                if subprocess.getoutput(f'if exist "{directory}" echo exists') == "exists":
                    existing_directories.append(directory)
                    existing_directory_names.append(selected_directory_names[i])
                else:
                    files_not_found.append(directory)
            for i, directory in enumerate(existing_directories):
                meter += meter_update_var
                destination_path = f"./Save/{save_folder_name}/{existing_directory_names[i]}/"
                path = subprocess.getoutput(f"echo {directory}")
                if self.show_current_files_in_cmd_var.get() == 1:
                    subprocess.call(f'xcopy "{path}" "{destination_path}" /e /i')
                else:
                    subprocess.call(f'xcopy "{path}" "{destination_path}" /e /i', stdout=subprocess.DEVNULL)
                # https: // stackoverflow.com / questions / 1996518 / retrieving - the - output - of - subprocess - call
                self.progress_meter.configure(amountused=round(meter, 2))
                self.window.update()
            self.progress_meter.configure(amountused=round(100, 2))
            self.end_time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            if len(files_not_found) != 0:
                # If there is any file not found errors
                message = ""
                for file in files_not_found:
                    message += file
                    message += "\n"
                Messagebox.show_error(title="Error", message=f"Files not found: \n{message}")
                self.show_copy_finished_time()
        else:
            Messagebox.show_warning(title="Warning", message=f"You must set the files to backup!")

    def show_copy_finished_time(self):
        delta = self.end_time - self.start_time
        Messagebox.show_info(title="Copying finished", message=f"Copying finished in {delta}")
