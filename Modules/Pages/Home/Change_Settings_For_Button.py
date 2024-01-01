from Modules.Pages.Home import Application_Launcher_Gui
import ttkbootstrap as ttk
from Modules.Utilities.Create_Icons import CreateIcon
import tkinter as tk
from tkinter import filedialog
import json


class ChangeButtonSettings:
    def __init__(self, index, middle_frame):
        # This function gest called by the ApplicationLauncherGui class

        # Define variables
        self.middle_frame = middle_frame
        self.index = index

        # Create top level
        self.top_level = ttk.Toplevel(title=f"Change the settings for button{index}")
        self.top_level.minsize(width=600, height=220)
        self.top_level.grab_set()

        # Create title
        title = ttk.Label(master=self.top_level, text=f"Change the settings for button{self.index}", font=15)
        title.pack(pady=10)

        # Create name entry frame
        name_entry_frame = ttk.Frame(master=self.top_level)

        # Create program name widgets
        program_name_label = ttk.Label(master=name_entry_frame, text="Set the name of the button", width=25)
        program_name_label.pack(side="left", padx=(10, 15))
        self.program_name_entry_var = tk.StringVar(value="Enter name here")
        program_name_entry = ttk.Entry(master=name_entry_frame, textvariable=self.program_name_entry_var)
        program_name_entry.pack(side="left", fill="x", padx=(5, 10), expand=1)

        # Create icon entry widgets
        icon_entry_frame = ttk.Frame(master=self.top_level)
        icon_location_label = ttk.Label(master=icon_entry_frame, text="Set the icon location", width=25)
        icon_location_label.pack(side="left", padx=(10, 15))
        self.program_icon_entry_var = tk.StringVar(value="Enter icon location here")
        program_icon_entry = ttk.Entry(master=icon_entry_frame, textvariable=self.program_icon_entry_var)
        program_icon_entry.pack(side="left", fill="x", padx=5, expand=1)
        locate_icon_button = ttk.Button(master=icon_entry_frame, text="Locate icon", width=13,
                                        command=lambda: self.locate_file(0))
        locate_icon_button.pack(side="left", padx=(5, 10))

        # Create program entry widgets
        program_entry_frame = ttk.Frame(master=self.top_level)
        program_location_label = ttk.Label(master=program_entry_frame, text="Set the program location", width=25)
        program_location_label.pack(side="left", padx=(10, 15))
        self.program_location_entry_var = tk.StringVar(value="Enter program location here")
        program_location_entry = ttk.Entry(master=program_entry_frame, textvariable=self.program_location_entry_var)
        program_location_entry.pack(side="left", fill="x", padx=5, expand=1)
        program_location_entry_button = ttk.Button(master=program_entry_frame, text="Locate program", width=13,
                                                   command=lambda: self.locate_file(1))
        program_location_entry_button.pack(side="left", padx=(5, 10))

        # Pack frames
        name_entry_frame.pack(fill="x", pady=5)
        icon_entry_frame.pack(fill="x", pady=5)
        program_entry_frame.pack(fill="x", pady=(5, 0))

        # Create option frame
        option_frame = ttk.Frame(master=self.top_level)

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
        accept_button.pack(side="right", padx=(5, 10), pady=(10, 5))
        cancel_button.pack(side="right", padx=(5, 10), pady=(10, 5))
        option_frame.pack(side="bottom", fill="x", pady=(0, 2))
        self.top_level.mainloop()

    def locate_file(self, index):
        # This function gets called whenever one of the "locate" buttons is pressed
        file = filedialog.askopenfilename()
        if file != ():
            if file != "":
                # If the filedialog is not empty
                if index == 0:
                    try:
                        self.program_icon_entry_var.set(file)
                    except TypeError:
                        pass
                elif index == 1:
                    try:
                        self.program_location_entry_var.set(file)
                    except TypeError:
                        pass

    def close_pop_up(self):
        # This function gets called whenever the "cancel" or "accept" button is pressed
        for widget in self.middle_frame.winfo_children():
            widget.destroy()
        self.top_level.destroy()
        self.top_level.grab_release()
        Application_Launcher_Gui.ApplicationLauncher(self.middle_frame)

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
        else:
            # Call CreateIcon class to create the correct resolution image and save it to the Icons folder
            CreateIcon(self.program_icon_entry_var.get(), self.index)
            # Update Configfile
            with open("Config.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data["program_names"][self.index] = self.program_name_entry_var.get()
            data["image_locations"][self.index] = f"Icons/button{self.index}_icon.png"
            data["program_locations"][self.index] = self.program_location_entry_var.get()
            with open("Config.json", "w") as jsonFile:
                json.dump(data, jsonFile, indent=3)
            self.close_pop_up()
