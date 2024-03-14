import tkinter as tk

import ttkbootstrap as ttk

from Modules.Configfile.Config import Configfile


class GenerateEmptyProject:
    def __init__(self, master, generate_empty_project):
        self.top_level = ttk.Toplevel(title="Generate empty project")
        self.top_level.minsize(width=300, height=140)
        self.top_level.maxsize(width=350, height=150)
        self.top_level.transient(master)
        self.top_level.grab_set()

        self.generate_empty_project = generate_empty_project
        self.config = Configfile()

        frame = ttk.Frame(self.top_level)
        title = ttk.Label(frame, text="Select the location for the empty project folder")

        self.project_name_var = tk.StringVar(value="No subfolder")
        self.project_name_menu = ttk.OptionMenu(
            frame,
            self.project_name_var,
            self.project_name_var.get(),
            style="info outline",
        )
        title.pack(padx=15, pady=15)
        button_frame = ttk.Frame(frame)
        cancel_button = ttk.Button(button_frame, text="Cancel", style="danger", command=self.top_level.destroy)
        accept_button = ttk.Button(button_frame, text="Generate", style="success", command=self.generate_project)
        cancel_button.pack(side="left", padx=5, fill="x", expand=True)
        accept_button.pack(side="left", padx=5, fill="x", expand=True)
        button_frame.pack(pady=15, fill="x", side="bottom")

        self.project_name_menu.set_menu(None, *self.config.project_names)
        self.project_name_menu.pack()
        frame.pack(fill="both", expand=True)
        self.top_level.mainloop()

    def generate_project(self):
        self.top_level.destroy()
        self.generate_empty_project(self.project_name_var.get())
