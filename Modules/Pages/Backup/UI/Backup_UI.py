import ttkbootstrap as ttk
import tkinter as tk

from ttkbootstrap.scrolled import ScrolledFrame


class BackupUI:
    def __init__(self, master):
        self.master_container = ttk.Frame(master)

        # Creating files to include frame
        self.top_container = ttk.Frame(self.master_container)
        placeholder = ttk.Frame(self.top_container)
        placeholder.pack()
        self.files_to_include_frame = ttk.LabelFrame(master=self.top_container, style="info", text="Files to include")
        self.location_container = ScrolledFrame(self.files_to_include_frame)

        self.location_container.pack(fill="both", expand=True)

        self.top_container.pack()

        # Create progress meter
        # self.progress_bar = ttk.Meter(
        #     master=self.backup_page,
        #     metersize=200,
        #     padding=5,
        #     amountused=0,
        #     amounttotal=100,
        #     subtext="Done",
        #     style="info",
        #     textright="%")
        # self.progress_bar.pack(pady=15, padx=15)

        # Create back files up button
        self.back_files_up_button = ttk.Button(
            master=self.master_container,
            text="Start backup",
            width=25, style="info",)
        self.back_files_up_button.pack(pady=15)

        # Create add new option button
        self.add_new_option_button = ttk.Button(
            master=self.master_container,
            text="Add new backup option",
            width=25, style="warning")
        self.add_new_option_button.pack(pady=15)
