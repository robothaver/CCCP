import json
import os
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from Assets import Assets
from Modules.Utilities.Create_Icons import CreateIcon
from Modules.Utilities.Get_Relative_Path import GetRelativePath
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Utilities.Locate_File import LocateFile


class ChangeButtonSettings:
    def __init__(self, master, index, config, update_button):
        # This function gest called by the ApplicationLauncherGui class

        # Define variables
        self.index = index
        self.is_accepted = False
        self.update_button = update_button
        self.config = config

        # Create top level
        self.top_level = ttk.Toplevel(master=master, title=f"Change the settings for button_{index}")
        self.top_level.minsize(width=600, height=220)
        self.top_level.transient(master)
        self.top_level.grab_set()

        # Create title
        title = ttk.Label(master=self.top_level, text=f"Change the settings for button_{self.index}", font=15)
        title.pack(pady=10)

        # Create name entry frame
        name_entry_frame = ttk.Frame(master=self.top_level)

        # Create program name widgets
        program_name = self.config.program_names[index]
        program_name_label = ttk.Label(master=name_entry_frame, text="Set the name of the button", width=25)
        program_name_label.pack(side="left", padx=(10, 15))
        self.program_name_entry_var = tk.StringVar(value=program_name)
        program_name_entry = ttk.Entry(master=name_entry_frame, textvariable=self.program_name_entry_var)
        program_name_entry.pack(side="left", fill="x", padx=(5, 10), expand=1)

        # Create icon entry widgets
        icon_entry_frame = ttk.Frame(master=self.top_level)
        icon_location_label = ttk.Label(master=icon_entry_frame, text="Set the icon location", width=25)
        icon_location_label.pack(side="left", padx=(10, 15))
        icon_location = config.image_locations[index] if config.image_locations[index] != Assets.default_image_locations else "Enter icon location here"
        self.program_icon_entry_var = tk.StringVar(value=icon_location)
        program_icon_entry = ttk.Entry(master=icon_entry_frame, textvariable=self.program_icon_entry_var)
        program_icon_entry.pack(side="left", fill="x", padx=5, expand=1)
        locate_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")
        locate_icon_button = ttk.Button(master=icon_entry_frame,
                                        command=lambda: self.get_absolute_path(1), image=locate_icon)
        locate_icon_button.pack(side="left", padx=(5, 10))
        locate_icon_button.image = locate_icon

        # Create program entry widgets
        program_entry_frame = ttk.Frame(master=self.top_level)
        program_location = config.program_locations[index] if config.program_locations[index] != "default" else "Enter program location here"
        program_location_label = ttk.Label(master=program_entry_frame, text="Set the program location", width=25)
        program_location_label.pack(side="left", padx=(10, 15))
        self.program_location_entry_var = tk.StringVar(value=program_location)
        program_location_entry = ttk.Entry(master=program_entry_frame, textvariable=self.program_location_entry_var)
        program_location_entry.pack(side="left", fill="x", padx=5, expand=1)

        locate_absolute_path_btn = ttk.Button(master=program_entry_frame, image=locate_icon,
                                              command=lambda: self.get_absolute_path(0))
        locate_absolute_path_btn.pack(side="left", padx=(5, 0))
        locate_absolute_path_btn.image = locate_icon
        relative_path_icon = tk.PhotoImage(file="Assets/Images/Find_Relative_Path.png")
        locate_relative_path_btn = ttk.Button(master=program_entry_frame, image=relative_path_icon,
                                              command=self.get_relative_path)
        locate_relative_path_btn.pack(side="left", padx=(5, 10))
        locate_relative_path_btn.image = relative_path_icon

        # Pack frames
        name_entry_frame.pack(fill="x", pady=5)
        icon_entry_frame.pack(fill="x", pady=5)
        program_entry_frame.pack(fill="x", pady=(5, 0))

        # Create option frame
        option_frame = ttk.Frame(master=self.top_level)

        reset_button = ttk.Button(master=option_frame, text="Reset button", style="warning",
                                  command=self.reset_button)

        # Create cancel button
        cancel_button = ttk.Button(master=option_frame, text="Cancel", style="danger", width=10,
                                   command=self.close_pop_up)
        # Create accept button
        accept_button = ttk.Button(master=option_frame, text="Accept", style="success", width=10,
                                   command=self.change_settings)
        # Create message label
        self.message_label_var = tk.StringVar()
        self.message_label = ttk.Label(master=option_frame, textvariable=self.message_label_var, bootstyle="danger",
                                       font=11)
        # Pack buttons
        reset_button.pack(side="left", padx=(10, 5), pady=(10, 5))
        accept_button.pack(side="right", padx=(5, 10), pady=(10, 5))
        cancel_button.pack(side="right", padx=(5, 10), pady=(10, 5))
        option_frame.pack(side="bottom", fill="x", pady=(0, 2))

    def reset_button(self):
        UpdateConfigfile("program_names", f"Button_{self.index}", self.index)
        UpdateConfigfile("image_locations", Assets.default_image_locations, self.index)
        UpdateConfigfile("program_locations", "default", self.index)
        self.update_button(self.index)
        self.close_pop_up()

    def get_absolute_path(self, index):
        path = LocateFile().get_absolute_path()
        if path is not None:
            if index == 0:
                self.program_location_entry_var.set(value=path)
            else:
                self.program_icon_entry_var.set(value=path)

    def get_relative_path(self):
        path = LocateFile().get_relative_path()
        if path is not None:
            self.program_location_entry_var.set(value=path)

    def close_pop_up(self):
        # This function gets called whenever the "cancel" or "accept" button is pressed
        self.top_level.grab_release()
        self.top_level.destroy()

    def change_settings(self):
        # This function gets called whenever the "accept" button is pressed
        if self.program_icon_entry_var.get() == "" or self.program_icon_entry_var.get() == "Enter icon location here":
            # If the input is empty or default
            self.message_label_var.set("Invalid icon location!")
            self.message_label.pack(side="left", padx=10, pady=(10, 5))
        elif self.program_location_entry_var.get() == "" \
                or self.program_location_entry_var.get() == "Enter program location here":
            # If the input is empty or default
            self.message_label_var.set("Invalid program location!")
            self.message_label.pack(side="left", padx=10, pady=(10, 5))
        elif self.program_name_entry_var.get() == "":
            self.message_label_var.set("Invalid program name!")
            self.message_label.pack(side="left", padx=10, pady=(10, 5))
        else:
            # Call CreateIcon class to create the correct resolution image and save it to the Icons folder
            CreateIcon(self.program_icon_entry_var.get(), self.index)
            # Update Configfile
            UpdateConfigfile("program_names", self.program_name_entry_var.get(), self.index)
            UpdateConfigfile("image_locations", f"Icons/button{self.index}_icon.png", self.index)
            UpdateConfigfile("program_locations", self.program_location_entry_var.get(), self.index)
            self.update_button(self.index)
            self.close_pop_up()