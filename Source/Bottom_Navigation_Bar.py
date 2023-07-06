from File_Generator import FileGenerator
from Application_Launcher_Gui import ApplicationLauncherGui
from Backup_Page import BackupPage
from Settings import Settings
import tkinter as tk
import ttkbootstrap as ttk
from Config import Configfile
from Assets import Assets
from Application_Dashboard import ApplicationDashboard


# noinspection PyArgumentList
class BottomNavigationBar:
    def __init__(self, master, window, middle_frame, top_frame, style):
        # Define variables
        self.top_frame = top_frame
        self.style = style
        self.master = master
        self.middle_frame = middle_frame
        self.window = window
        self.config = Configfile()

        # Configure frame column and row settings
        for x in range(5):
            self.master.columnconfigure(x, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Set page to starting page
        if self.config.starting_page == 5:
            page = self.config.current_page
        else:
            page = self.config.starting_page

        # Page button icons
        self.selected_navbar_icons = []
        self.deselected_navbar_icons = []

        # Selected page button
        self.selected_page_button_var = tk.IntVar(value=page)

        # Load icons
        for i, icon in enumerate(Assets.selected_navbar_icons):
            self.selected_navbar_icons.append(tk.PhotoImage(file=icon))
            self.deselected_navbar_icons.append(tk.PhotoImage(file=Assets.deselected_navbar_icons[i]))

        # Create home button
        self.home_button = ttk.Radiobutton(master=self.master,
                                           style="info, outline-toolbutton",
                                           value=0, variable=self.selected_page_button_var,
                                           image=self.deselected_navbar_icons[0],
                                           command=self.change_page)
        self.home_button.grid(row=0, column=0, sticky="nsew")

        # Create backup button
        self.backup_button = ttk.Radiobutton(master=self.master,
                                             style="info, outline-toolbutton",
                                             value=1,
                                             variable=self.selected_page_button_var,
                                             image=self.deselected_navbar_icons[1],
                                             command=self.change_page)
        self.backup_button.grid(row=0, column=1, sticky="nsew")

        # Create filegenerator button
        self.filegenerator_button = ttk.Radiobutton(master=self.master,
                                                    style="info, outline-toolbutton",
                                                    value=2,
                                                    variable=self.selected_page_button_var,
                                                    image=self.deselected_navbar_icons[2],
                                                    command=self.change_page)
        self.filegenerator_button.grid(row=0, column=2, sticky="nsew")

        # Create application dashboard button
        self.application_dashboard = ttk.Radiobutton(master=self.master,
                                                     style="info, outline-toolbutton",
                                                     value=3,
                                                     variable=self.selected_page_button_var,
                                                     image=self.deselected_navbar_icons[3],
                                                     command=self.change_page)
        self.application_dashboard.grid(row=0, column=3, sticky="nsew")

        # Create settings button
        self.settings = ttk.Radiobutton(master=self.master,
                                        text="Settings",
                                        style="info, outline-toolbutton",
                                        value=4,
                                        variable=self.selected_page_button_var,
                                        image=self.deselected_navbar_icons[4],
                                        command=self.change_page)
        self.settings.grid(row=0, column=4, sticky="nsew")

        # Call selected button class
        self.selected_button(self.selected_page_button_var.get())

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
        # Clearing the middle frame
        for widget in self.middle_frame.winfo_children():
            widget.destroy()
        # Calling the correct option
        if self.selected_page_button_var.get() == 0:
            self.selected_button(0)
            ApplicationLauncherGui(self.middle_frame)
        elif self.selected_page_button_var.get() == 1:
            self.selected_button(1)
            BackupPage(self.middle_frame, self.window)
        elif self.selected_page_button_var.get() == 2:
            self.selected_button(2)
            FileGenerator(self.middle_frame)
        elif self.selected_page_button_var.get() == 3:
            self.selected_button(3)
            ApplicationDashboard(self.middle_frame)
        elif self.selected_page_button_var.get() == 4:
            self.selected_button(4)
            Settings(self.middle_frame, self.top_frame, self.style)
