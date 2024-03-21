from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Project_Generator.Project_Generator_Page import ProjectGeneratorPage
from Modules.Pages.Home.Home_Page import HomePage
from Modules.Pages.Backup.Backup_Page import BackupPage
from Modules.Pages.Settings.Settings import Settings
import tkinter as tk
import ttkbootstrap as ttk
from Modules.Configfile.Config import Configfile
from Assets import Assets
from Modules.Pages.Dashboard.Application_Dashboard import ApplicationDashboard


# noinspection PyArgumentList
class NavigationBar:
    def __init__(self, master, navigation_controller, config: Configfile):
        # Define variables
        self.master = master
        self.navigation_controller = navigation_controller
        self.config = config

        # Configure frame column and row settings
        for x in range(5):
            self.master.columnconfigure(x, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Set page to starting page
        self.page_index = None

        # Page button icons
        self.selected_navbar_icons = []
        self.deselected_navbar_icons = []

        # Selected page button
        self.selected_page_button_var = tk.IntVar(value=self.get_initial_page())

        # Load icons
        for i, icon in enumerate(Assets.selected_navbar_icons):
            self.selected_navbar_icons.append(tk.PhotoImage(file=icon))
            self.deselected_navbar_icons.append(tk.PhotoImage(file=Assets.deselected_navbar_icons[i]))
        style = "info, outline-toolbutton"
        # Create home button
        self.home_button = ttk.Radiobutton(master=self.master,
                                           style=style,
                                           value=0, variable=self.selected_page_button_var,
                                           image=self.deselected_navbar_icons[0],
                                           command=self.change_page)
        self.home_button.grid(row=0, column=0, sticky="nsew")

        # Create backup button
        self.backup_button = ttk.Radiobutton(master=self.master,
                                             style=style,
                                             value=1,
                                             variable=self.selected_page_button_var,
                                             image=self.deselected_navbar_icons[1],
                                             command=self.change_page)
        self.backup_button.grid(row=0, column=1, sticky="nsew")

        # Create filegenerator button
        self.filegenerator_button = ttk.Radiobutton(master=self.master,
                                                    style=style,
                                                    value=2,
                                                    variable=self.selected_page_button_var,
                                                    image=self.deselected_navbar_icons[2],
                                                    command=self.change_page)
        self.filegenerator_button.grid(row=0, column=2, sticky="nsew")

        # Create application dashboard button
        self.application_dashboard = ttk.Radiobutton(master=self.master,
                                                     style=style,
                                                     value=3,
                                                     variable=self.selected_page_button_var,
                                                     image=self.deselected_navbar_icons[3],
                                                     command=self.change_page)
        self.application_dashboard.grid(row=0, column=3, sticky="nsew")

        # Create settings button
        self.settings = ttk.Radiobutton(master=self.master,
                                        text="Settings",
                                        style=style,
                                        value=4,
                                        variable=self.selected_page_button_var,
                                        image=self.deselected_navbar_icons[4],
                                        command=self.change_page)
        self.settings.grid(row=0, column=4, sticky="nsew")

        # Call selected button class
        self.selected_button(self.selected_page_button_var.get())

    def get_initial_page(self):
        page_index = self.config.starting_page
        if self.config.starting_page == 5:
            page_index = self.config.current_page
        return page_index

    def selected_button(self, selected_button):
        # This function runs whenever the constructor runs or a page is selected
        # This function sets the selected buttons icon to the selected one
        buttons = []
        for i, widget in enumerate(self.master.winfo_children()):
            widget.config(image=self.deselected_navbar_icons[i])
            buttons.append(widget)
        buttons[selected_button].config(image=self.selected_navbar_icons[selected_button])

    def change_page(self):
        # This function runs whenever an option is selected and, it makes the button selected
        selected_index = self.selected_page_button_var.get()
        if selected_index != self.page_index:
            self.selected_button(selected_index)
            self.navigation_controller.change_page(selected_index)
            self.page_index = self.selected_page_button_var.get()
            UpdateConfigfile("current_page", self.page_index)
