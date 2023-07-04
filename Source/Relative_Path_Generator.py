import os
import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.dialogs

import Application_Dashboard
from tkinter import filedialog


class RelativePathGenerator:
    def __init__(self, master):
        # Define variables
        self.master = master

        # Create back button
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=self.back)
        back_button.pack(side="left", padx=10, pady=5)
        back_frame.pack(fill="x")

        # Create title label
        title_label = ttk.Label(master, text="Relative path finder", font=('Aril', '16', 'bold'), style="info")
        title_label.pack(pady=10)

        # Create the main container
        main_container = ttk.LabelFrame(master, text="Path settings", style="info")

        # Create frames
        path_entry_frame = ttk.Frame(main_container)
        use_default_path_frame = ttk.Frame(main_container)

        # Create use default path widgets
        self.use_default_path_var = ttk.IntVar(value=1)
        use_default_path_check_button = ttk.Checkbutton(use_default_path_frame,
                                                        text="Use current location as starting path",
                                                        style="info round-toggle", command=self.update_widgets,
                                                        variable=self.use_default_path_var)
        # Packing
        use_default_path_check_button.pack(side="left", padx=5)
        use_default_path_frame.pack(fill="x", padx=5, pady=(5, 0))

        # Create starting path widgets
        self.starting_path_entry_label = ttk.Label(path_entry_frame, text="Starting path:", style="secondary", width=14)
        self.starting_path_entry_var = ttk.StringVar()
        self.starting_path_entry = ttk.Entry(path_entry_frame, textvariable=self.starting_path_entry_var,
                                             style="secondary", state="disabled")
        self.starting_path_entry_locate_button = ttk.Button(master=path_entry_frame, text="locate",
                                                            command=lambda: self.locate_file(0), bootstyle="secondary",
                                                            state="disabled")
        # Packing
        self.starting_path_entry_label.pack(side="left", padx=5)
        self.starting_path_entry.pack(fill="x", expand=1, padx=5, side="left")
        self.starting_path_entry_locate_button.pack(padx=5, side="left")
        path_entry_frame.pack(fill="x", padx=5, pady=5)

        # Create directory checkbutton
        is_directory_checkbutton_frame = ttk.Frame(main_container)
        self.is_directory_checkbutton_var = tk.IntVar(value=0)
        is_directory_checkbutton = ttk.Checkbutton(is_directory_checkbutton_frame,
                                                   text="Use directory",
                                                   variable=self.is_directory_checkbutton_var,
                                                   style="info round-toggle")
        is_directory_checkbutton.pack(side="left", padx=5)
        is_directory_checkbutton_frame.pack(fill="x", padx=5, pady=5)

        # Create path destination widgets
        path_destination_frame = ttk.Frame(main_container)
        path_destination_entry_label = ttk.Label(path_destination_frame, text="Path destination:",
                                                 style="info", width=14)
        self.path_destination_entry_var = ttk.StringVar()
        path_destination_entry = ttk.Entry(path_destination_frame, textvariable=self.path_destination_entry_var,
                                           style="secondary")
        path_destination_entry_locate_button = ttk.Button(master=path_destination_frame, text="locate",
                                                          command=lambda: self.locate_file(1), bootstyle="secondary")
        # Packing
        path_destination_entry_label.pack(side="left", padx=5)
        path_destination_entry.pack(fill="x", expand=1, padx=5, side="left")
        path_destination_entry_locate_button.pack(padx=5, side="left")
        path_destination_frame.pack(fill="x", padx=5, pady=5)

        # Create relative path button
        generate_relative_path_button = ttk.Button(main_container, text="Generate relative path", style="success",
                                                   command=self.generate_relative_path)
        generate_relative_path_button.pack(pady=10)
        main_container.pack(fill="x", padx=10)

        # Create relative path widgets
        relative_path_frame = ttk.Frame(master)
        relative_path_label = ttk.Label(relative_path_frame, text="Relative path:", style="warning")
        relative_path_label.pack(side="left", padx=5)
        self.relative_path_entry_var = tk.StringVar()
        relative_path_entry = ttk.Entry(relative_path_frame, textvariable=self.relative_path_entry_var)
        relative_path_entry.pack(side="left", expand=1, fill="x", padx=5)
        relative_path_frame.pack(fill="x", padx=5, pady=10)

    def update_widgets(self):
        # This function runs whenever the use default path checkbutton is pressed
        if self.use_default_path_var.get() == 0:
            # Turn option on
            self.starting_path_entry_label.config(bootstyle="info")
            self.starting_path_entry.config(bootstyle="info", state="normal")
            self.starting_path_entry_locate_button.config(bootstyle="info", state="normal")
        else:
            # Turn option off
            self.starting_path_entry_label.config(bootstyle="secondary")
            self.starting_path_entry.config(bootstyle="secondary", state="disabled")
            self.starting_path_entry_locate_button.config(bootstyle="secondary", state="disabled")

    def back(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        Application_Dashboard.ApplicationDashboard(self.master)

    def locate_file(self, index):
        if self.is_directory_checkbutton_var.get() == 1:
            file = filedialog.askdirectory(title="Select directory")
        else:
            file = filedialog.askopenfilename(title="Select file")
        if file != ():
            if file != "":
                if index == 0:
                    self.starting_path_entry_var.set(file)
                if index == 1:
                    self.path_destination_entry_var.set(file)

    def generate_relative_path(self):
        if not self.path_destination_entry_var.get() == "":
            try:
                if self.use_default_path_var.get() == 1:
                    self.relative_path_entry_var.set(os.path.relpath(path=self.path_destination_entry_var.get()))
                else:
                    self.relative_path_entry_var.set(os.path.relpath(start=self.starting_path_entry.get(),
                                                                     path=self.path_destination_entry_var.get()))
            except ValueError:
                ttkbootstrap.dialogs.Messagebox.show_error(title="Error",
                                                           message="Path destination is on a different drive!")
        else:
            ttkbootstrap.dialogs.Messagebox.show_warning(title="Warning", message="You must set the destination path!")
