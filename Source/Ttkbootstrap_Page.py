import os
from Config import Configfile
import About
import Assets.Assets
from About import *


class TtkbootstrapPage:
    def __init__(self, master, top_frame, style):
        # Define variables
        self.config = Configfile()
        self.master = master
        self.top_frame = top_frame
        self.style = style

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
        for widget in self.master.winfo_children():
            widget.destroy()
        About.About(self.master, self.top_frame, self.style)

    def open_github_page(self):
        # This function opens the link in the browser selected by the user
        if self.config.browser == "system default":
            os.system(f"start {Assets.ttkbootstrap_link}")
        else:
            if self.config.browser == "firefox":
                os.system(f"start {self.config.browser} --private-window {Assets.ttkbootstrap_link}")
            else:
                os.system(f"start {self.config.browser} --guest {Assets.ttkbootstrap_link}")
