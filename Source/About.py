import tkinter as tk
import ttkbootstrap as ttk
from Assets import Assets
import Settings
from Ttkbootstrap_Page import TtkbootstrapPage
from Config import Configfile
import os


class About:
    def __init__(self, master, top_frame, style):
        # Defining variables
        self.master = master
        self.top_frame = top_frame
        self.style = style
        self.config = Configfile()

        # Creating back button
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=self.back)
        back_button.pack(side="left", padx=10, pady=10)
        back_frame.pack(fill="x")

        # Creating the main container
        main_container = ttk.Frame(master)

        # Creating logo label
        self.logo = tk.PhotoImage(file="Assets/Images/CCCP_logo_500x247.png")
        logo_label = ttk.Label(main_container, image=self.logo)
        logo_label.pack(padx=20, pady=10)

        # Creating title label
        title_label = ttk.Label(main_container, text="Complex Computer Controlling Program",
                                font=('arial', '16', 'bold'), style="info")
        title_label.pack(pady=5)

        # Separator
        separator = ttk.Separator(main_container)
        separator.pack(fill="x", padx=100)

        # Creating description
        description = ttk.Label(main_container, text=Assets.program_description, font=('arial', '12', 'bold'),
                                wraplength=600, justify="center")
        description.pack(padx=10)

        # Creating version label
        version_label = ttk.Label(main_container, text="Version: 1.6", font=('arial', '12', 'bold'), style="info")
        version_label.pack()

        # Creating ttkbootstrap button
        ttkbootstrap_button = ttk.Button(master=main_container, text="ttkbootstrap",
                                         style="info", command=self.ttkbootstrap_page, width=60)
        ttkbootstrap_button.pack(pady=15)

        # Creating GitHub button
        github_button = ttk.Button(master=main_container, text="GitHub", style="warning", width=60, 
                                   command=self.open_github_page)
        github_button.pack()

        main_container.pack(fill="both", expand=1)

    def back(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        Settings.Settings(self.master, self.top_frame, self.style)

    def ttkbootstrap_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        TtkbootstrapPage(self.master, self.top_frame, self.style)
    
    def open_github_page(self):
        # This function opens the link in the browser selected by the user
        os.system(f"start {Assets.github_link}")
