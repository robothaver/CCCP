import ttkbootstrap as ttk
from Modules.Configfile.Config import Configfile
from Assets import Assets
import os
from Modules.Utilities.Launch_Browser import LaunchBrowser


class TtkbootstrapPage:
    def __init__(self, master, change_page):
        # Define variables
        self.config = Configfile()
        self.master = master
        self.change_page = change_page

        # Create back button
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=self.back)
        back_button.pack(side="left", padx=10, pady=10)
        back_frame.pack(fill="x")

        # Create main_frame
        main_frame = ttk.Frame(master)
        title = ttk.Label(main_frame, text="Ttkbootstrap", font=('arial', '16', 'bold'), style="info")
        title.pack(pady=5)
        separator = ttk.Separator(main_frame)
        separator.pack(fill="x", padx=100)

        # Create description widgets
        description = ttk.Label(main_frame, text=Assets.ttkbootstrap_description, font=('arial', '12', 'bold'),
                                wraplength=500, justify="center")
        description.pack()

        # Create GitHub button
        github_button = ttk.Button(master=main_frame, text="GitHub page", style="warning",
                                   command=self.open_github_page, width=60)

        github_button.pack(pady=20)

        main_frame.pack(fill="both", expand=True)

    def back(self):
        self.change_page(0)

    def open_github_page(self):
        LaunchBrowser(Assets.ttkbootstrap_link, self.config.browser)
