import ttkbootstrap as ttk
import tkinter as tk
from Assets import Assets


class AboutUI:
    def __init__(self, master):

        # Creating the main container
        self.main_container = ttk.Frame(master)

        # Creating container for ttkbootstrap page
        self.bootstrap_container = ttk.Frame(master)

        # Creating back button
        back_frame = ttk.Frame(self.main_container)
        self.back_button = ttk.Button(back_frame, text="Back")
        self.back_button.pack(side="left", padx=10, pady=10)
        back_frame.pack(fill="x")

        # Creating logo label
        self.logo = tk.PhotoImage(file="Assets/Images/CCCP_logo_500x247.png")
        logo_label = ttk.Label(self.main_container, image=self.logo)
        logo_label.pack(padx=20, pady=10)

        # Creating title label
        title_label = ttk.Label(self.main_container, text="Complex Computer Controlling Program",
                                font=('arial', '16', 'bold'), style="info")
        title_label.pack(pady=5)

        # Separator
        separator = ttk.Separator(self.main_container)
        separator.pack(fill="x", padx=100)

        # Creating description
        description = ttk.Label(self.main_container, text=Assets.program_description, font=('arial', '12', 'bold'),
                                wraplength=600, justify="center")
        description.pack(padx=10)

        # Creating version label
        version_label = ttk.Label(self.main_container, text="Version: 1.6", font=('arial', '12', 'bold'), style="info")
        version_label.pack()

        # Creating ttkbootstrap button
        self.ttkbootstrap_button = ttk.Button(master=self.main_container, text="ttkbootstrap", style="info", width=60)
        self.ttkbootstrap_button.pack(pady=15)

        # Creating GitHub button
        self.github_button = ttk.Button(master=self.main_container, text="GitHub", style="warning", width=60, )
        self.github_button.pack()

        self.main_container.pack(fill="both", expand=1)
