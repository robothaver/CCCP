import platform

import ttkbootstrap as ttk
import tkinter as tk

from ttkbootstrap.scrolled import ScrolledFrame


class BackupUI:
    def __init__(self, master):
        self.master_container = ttk.Frame(master)
        self.master_container.columnconfigure(0, weight=3)
        self.master_container.columnconfigure(1, weight=3)
        self.master_container.rowconfigure(0, weight=3)
        self.master_container.rowconfigure(1, weight=3)

        main_container = ttk.Frame(self.master_container)
        self.right_container = ttk.Frame(main_container)
        self.placeholder = ttk.Frame(self.right_container)
        self.placeholder.pack()
        self.files_to_include_frame = ttk.LabelFrame(master=self.right_container, style="info", text="Files to include")
        self.location_container = ScrolledFrame(self.files_to_include_frame)

        self.location_container.pack(fill="both", expand=True)

        ttk.Separator(self.files_to_include_frame).pack(fill="x", padx=10, pady=15)

        self.select_all_btn = ttk.Button(self.files_to_include_frame, text="Select all", style="info")
        self.files_to_include_frame.pack(pady=15)
        self.select_all_btn.pack(pady=(0, 15))
        self.left_container = ttk.Frame(main_container)

        # Create progress meter
        if platform.system() == "Windows":
            self.progress_bar = ttk.Meter(
                master=self.left_container,
                metersize=200,
                padding=5,
                amountused=0,
                amounttotal=100,
                subtext="Done",
                style="info",
                textright="%")
            self.progress_bar.pack(pady=15, padx=15)

        # Create back files up button
        self.back_files_up_button = ttk.Button(
            master=self.left_container,
            text="Start backup",
            width=25, style="info",)
        self.back_files_up_button.pack(pady=15)

        # Create add new option button
        self.add_new_option_button = ttk.Button(
            master=self.left_container,
            text="Add new backup option",
            width=25, style="warning")
        self.add_new_option_button.pack(pady=15)

        self.left_container.grid(row=0, column=0, sticky="nsew", padx=15)
        main_container.place(relx=.5, rely=.5, anchor="center")
