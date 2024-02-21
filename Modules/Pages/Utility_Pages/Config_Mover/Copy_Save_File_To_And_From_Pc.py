import os
import subprocess
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from Modules.Pages.Dashboard import Application_Dashboard
from Modules.Dialogs.Change_Preset_Settings import ChangePresetSettings
from Modules.Configfile.Config import Configfile
import shutil


class CopySaveFileToAndFromPc:
    def __init__(self, master, show_dashboard, config):
        # Define variables
        self.master = master
        self.config = config

        # Create back button
        self.master_container = ttk.Frame(master)
        back_frame = ttk.Frame(self.master_container)
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        back_button = ttk.Button(back_frame, text="Back", command=show_dashboard,
                                 image=self.back_button_icon, compound="left")
        back_button.pack(side="left", padx=10, pady=5)
        back_frame.pack(fill="x")

        # Create preset selector
        self.preset_selector_var = tk.StringVar()
        options = self.config.preset_name
        preset_selector = ttk.OptionMenu(self.master_container, self.preset_selector_var, "Select preset", *options,
                                         style="info outline", command=lambda preset: self.load_preset(preset))
        preset_selector.pack(pady=10)

        # Load icons
        self.copy_to_computer_icon = tk.PhotoImage(file="Assets/Images/Copy_Save_To_Computer_Icon.png")
        self.copy_from_computer_icon = tk.PhotoImage(file="Assets/Images/Copy_Save_From_Computer_Icon.png")

        # Create button frame
        button_frame = ttk.Frame(self.master_container)
        button_frame.rowconfigure(0, weight=1)

        # Configure button frame row and column settings
        for x in range(2):
            button_frame.columnconfigure(x, weight=1)

        # Create copy to computer button
        self.copy_to_computer_button = ttk.Button(master=button_frame, text="Copy save to computer",
                                                  image=self.copy_to_computer_icon,
                                                  compound="top", style="secondary",
                                                  command=self.copy_save_to_pc)
        self.copy_to_computer_button.grid(row=0, column=0, padx=25, pady=0, sticky="nsew")

        # Create copy from computer button
        self.copy_from_computer_button = ttk.Button(master=button_frame, text="Copy save from computer",
                                                    image=self.copy_from_computer_icon,
                                                    compound="top", style="secondary",
                                                    command=self.copy_save_from_pc)
        self.copy_from_computer_button.grid(row=0, column=1, padx=25, pady=0, sticky="nsew")

        # Pack button frame
        button_frame.pack(pady=15, padx=15, fill="both", expand=True)

        # Create change preset settings button
        self.change_preset_settings = ttk.Button(master=self.master_container, text="Change preset settings",
                                                 width=30, command=lambda: ChangePresetSettings(master))
        self.change_preset_settings.pack(side="bottom", pady=(10, 40))

        # Create launch application button
        self.launch_application_button = ttk.Button(master=self.master_container, text="Launch application",
                                                    width=30, style="secondary", state="disabled",
                                                    command=self.launch_application)
        self.launch_application_button.pack(side="bottom", pady=10)

    def load_preset(self, preset):
        # This function runs whenever the constructor gets called
        if preset != "Select preset":
            # If the preset is not default value
            index = self.config.preset_name.index(preset)
            # Update label variables
            if self.config.preset_application_location[index] != "":
                self.launch_application_button.config(bootstyle="success", state="normal")

    def copy_save_to_pc(self):
        # This function gets called whenever the "copy save to pc" button is pressed
        if self.preset_selector_var.get() != "Select preset":
            try:
                # If the preset selector is not "default"
                # Get index
                index = self.config.preset_name.index(self.preset_selector_var.get())
                # Create file name
                file_name = self.config.preset_input[index].replace(" ", "_").replace("/", " ").split()
                file_name = file_name[-1].replace("_", " ")
                # Create destination
                destination = subprocess.getoutput(f"echo {self.config.preset_output[index]}")
                # Copy save
                try:
                    shutil.copytree(src=self.config.preset_input[index], dst=destination, dirs_exist_ok=True)
                except FileNotFoundError:
                    Messagebox.show_error(title="Error", message="File not found!")
                Messagebox.ok(message=f"Copying finished to: {destination}")
            except FileNotFoundError:
                Messagebox.show_error(title="Error", message="File not found!")
        else:
            Messagebox.show_warning(title="Warning", message="You must select a preset first!")

    def copy_save_from_pc(self):
        if self.preset_selector_var.get() != "Select preset":
            try:
                # If the preset selector is not "default"
                # Get index
                index = self.config.preset_name.index(self.preset_selector_var.get())
                # Create file name
                file_name = self.config.preset_input[index].replace(" ", "_").replace("/", " ").split()
                file_name = file_name[-1].replace("_", " ")
                # Create destination and source
                destination = self.config.preset_input[index]
                print(destination)
                source = subprocess.getoutput(f"echo {self.config.preset_output[index]}")
                print(source)
                print(destination)
                # Copy save
                try:
                    shutil.copytree(src=source, dst=destination, dirs_exist_ok=True)
                except FileNotFoundError:
                    Messagebox.show_error("Erro", message="File not found!")
                Messagebox.ok(message=f"Copying finished to: {destination}")
            except FileNotFoundError:
                Messagebox.show_error(title="Error", message="File not found!")
        else:
            Messagebox.show_warning(title="Warning", message="You must select a preset first!")

    def launch_application(self):
        # This function gets called whenever the launch application button is pressed
        index = self.config.preset_name.index(self.preset_selector_var.get())
        try:
            os.startfile(self.config.preset_application_location[index])
        except FileNotFoundError:
            Messagebox.show_error(title="Error", message="Program not found!")
