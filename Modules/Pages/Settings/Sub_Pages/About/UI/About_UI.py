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
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        self.back_button = ttk.Button(back_frame, text="Back", image=self.back_button_icon, compound="left")
        self.back_button.pack(side="left", padx=10, pady=10)
        back_frame.pack(fill="x")

        about_container = ttk.Frame(self.main_container)

        # Creating logo label
        self.logo = tk.PhotoImage(file="Assets/Images/CCCP_logo_500x247.png")
        logo_label = ttk.Label(about_container, image=self.logo)
        logo_label.pack(padx=20)

        # Creating title label
        title_label = ttk.Label(about_container, text="Complex Computer Controlling Program",
                                font=('arial', '16', 'bold'), style="info")
        title_label.pack(pady=5)

        # Separator
        separator = ttk.Separator(about_container)
        separator.pack(ipadx=250)

        # Creating description
        description = ttk.Label(about_container, text=Assets.program_description, font=('arial', '10', 'bold'),
                                wraplength=690, justify="center")
        description.pack(padx=10)

        # Creating version label
        version_label = ttk.Label(about_container, text="Version: 1.7", font=('arial', '12', 'bold'), style="info")
        version_label.pack()

        # Creating ttkbootstrap button
        self.ttkbootstrap_icon = tk.PhotoImage(file="Assets/Images/TTKboostrap_Logo.png")
        self.ttkbootstrap_button = ttk.Button(master=about_container, text="ttkbootstrap", style="info",
                                              width=60, image=self.ttkbootstrap_icon, compound="left")
        self.ttkbootstrap_button.pack(pady=15)

        # Creating GitHub button
        self.github_icon = tk.PhotoImage(file="Assets/Images/Github_Icon.png")
        self.github_button = ttk.Button(master=about_container, text="GitHub", style="warning", width=60,
                                        image=self.github_icon, compound="left")
        self.github_button.pack(pady=(0, 5))
        about_container.place(relx=0.5, rely=0.5, anchor="center")

        self.main_container.pack(fill="both", expand=True)
