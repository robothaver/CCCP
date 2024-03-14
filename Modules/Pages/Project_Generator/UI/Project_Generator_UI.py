import tkinter as tk

import ttkbootstrap as ttk


class ProjectGeneratorUI:
    def __init__(self, master):
        self.master_container = ttk.Frame(master)
        self.default_location_message = "Select project output location"

        # Load images
        self.python_file_img = tk.PhotoImage(file="Assets/Images/Python_File_Icon.png")
        self.html_file_img = tk.PhotoImage(file="Assets/Images/HTML_File_Icon.png")
        self.open_project_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")

        # Create file output changer
        # self.file_outputs = self.config.file_output_locations
        self.file_output_var = tk.StringVar()
        self.file_output_changer = ttk.OptionMenu(
            self.master_container,
            self.file_output_var,
            self.default_location_message)
        self.file_output_changer.pack(pady=15)

        # Create button frame
        button_frame = ttk.Frame(self.master_container)
        button_frame.rowconfigure(0, weight=1)

        # Configure button frame row and column settings
        for x in range(2):
            button_frame.columnconfigure(x, weight=1)

        # Create python file generator button
        self.python_project_generator_btn = ttk.Button(master=button_frame, text="Python project",
                                                       image=self.python_file_img,
                                                       compound="top", style="secondary")
        self.python_project_generator_btn.grid(row=0, column=0, padx=25, pady=5, sticky="nsew")
        # Create HTML file generator button
        self.web_project_generator_btn = ttk.Button(master=button_frame, text="Web project",
                                                    image=self.html_file_img,
                                                    compound="top", style="secondary")
        self.web_project_generator_btn.grid(row=0, column=1, padx=25, pady=5, sticky="nsew")

        # Pack button frame
        self.empty_project_img = tk.PhotoImage(file="Assets/Images/File_Generator_Icon_Selected.png")
        self.empty_project_generator_btn = ttk.Button(master=button_frame, text="Empty project", compound="left",
                                                      image=self.empty_project_img, style="secondary")
        self.empty_project_generator_btn.grid(row=1, padx=25, pady=(10, 10), sticky="nsew", columnspan=2)

        button_frame.pack(pady=15, padx=15, fill="both", expand=True)

        self.open_project_btn = ttk.Button(master=self.master_container, text="Open project folder", width=30,
                                           style="success", image=self.open_project_icon, compound="left")
        self.open_project_btn.pack(ipady=5)

        bottom_button_frame = ttk.Frame(self.master_container)

        self.manage_output_locations_button = ttk.Button(master=bottom_button_frame,
                                                         text="Manage output location",
                                                         width=30)
        self.manage_output_locations_button.pack(side="left", pady=(20, 0), padx=15, fill="x", expand=True)

        self.manage_project_names_btn = ttk.Button(master=bottom_button_frame,
                                                   text="Manage project names",
                                                   width=30)
        self.manage_project_names_btn.pack(side="left", pady=(20, 0), padx=15, fill="x", expand=True)

        bottom_button_frame.pack(fill="x", padx=15, pady=15, side="bottom")
