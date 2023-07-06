import os
import time
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from Assets import Assets
from Config import Configfile
from Edit_File_Output_Locations import EditFileOutputLocations
from Update_Configfile import UpdateConfigfile


class FileGenerator:
    def __init__(self, master):
        UpdateConfigfile("current_page", 2)

        # Define variables
        self.master = master
        configfile = Configfile()

        # Load images
        self.python_file_img = tk.PhotoImage(file="Assets/Images/Python_File_Icon.png")
        self.html_file_img = tk.PhotoImage(file="Assets/Images/HTML_File_Icon.png")

        # Create file output changer
        self.file_outputs = configfile.file_output_locations
        self.file_output_var = tk.StringVar()
        self.file_output_changer = ttk.OptionMenu(
            master,
            self.file_output_var,
            "Select file output location",
            *self.file_outputs)
        self.file_output_changer.pack(pady=15)

        # Create button frame
        button_frame = ttk.Frame(master)
        button_frame.rowconfigure(0, weight=1)

        # Configure button frame row and column settings
        for x in range(2):
            button_frame.columnconfigure(x, weight=1)

        # Create python file generator button
        self.python_file_generator_button = ttk.Button(master=button_frame, text="Python file",
                                                       image=self.python_file_img,
                                                       compound="top", style="secondary",
                                                       command=lambda: self.generate_file(0))
        self.python_file_generator_button.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        # Create HTML file generator button
        self.html_file_generator_button2 = ttk.Button(master=button_frame, text="HTML file",
                                                      image=self.html_file_img,
                                                      compound="top", style="secondary",
                                                      command=lambda: self.generate_file(1))
        self.html_file_generator_button2.grid(row=0, column=1, padx=25, pady=25, sticky="nsew")

        # Pack button frame
        button_frame.pack(pady=15, padx=15, fill="both", expand=True)

        # Create add output location button
        self.add_output_location_button = ttk.Button(master=master, text="Add output location",
                                                     command=self.add_output_location, width=30)
        self.add_output_location_button.pack(side="bottom", pady=(20, 90))

    def add_output_location(self):
        EditFileOutputLocations(self.master)

    def generate_file(self, file_type):
        # This function runs whenever one of the generate buttons is pressed
        file_output_location = self.file_output_var.get()
        if file_output_location == "Select file output location":
            # If the file_output_location is not selceted
            tk.messagebox.showwarning(title="Warning", message="You must set the location for the file output!")
        else:
            if file_type == 0:
                # If file_type is python, create project folder in the selected directory
                if not os.path.exists(f"{self.file_output_var.get()}/Python"):
                    os.makedirs(f"{self.file_output_var.get()}/Python")
                folder_name = time.strftime("%Y-%m-%d")
                if not os.path.exists(f"{self.file_output_var.get()}/Python/{folder_name}"):
                    os.makedirs(f"{self.file_output_var.get()}/Python/{folder_name}")
                with open(f"{self.file_output_var.get()}/Python/{folder_name}/main.py", "w"):
                    pass
                # Open project file in vs code
                os.system(f'code "{self.file_output_var.get()}/Python/{folder_name}"')
            else:
                # If file_type is HTML, create project folder in the selected directory
                if not os.path.exists(f"{self.file_output_var.get()}/HTML"):
                    os.makedirs(f"{self.file_output_var.get()}/HTML")
                folder_name = time.strftime("%Y-%m-%d")
                if not os.path.exists(f"{self.file_output_var.get()}/HTML/{folder_name}"):
                    os.makedirs(f"{self.file_output_var.get()}/HTML/{folder_name}")
                # Write boilerplate into index.html
                with open(f"{self.file_output_var.get()}/HTMl/{folder_name}/index.html", "w") as html_file:
                    html_file.write(Assets.html_boilerplate)
                # Open project file in vs code
                os.system(f'code "{self.file_output_var.get()}/HTMl/{folder_name}"')
                