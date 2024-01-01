import os
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from Modules.Configfile.Config import Configfile
from Modules.Pages.Home.Change_Settings_For_Button import ChangeButtonSettings
from Assets import Assets
from Modules.Configfile.Update_Configfile import UpdateConfigfile


class ApplicationLauncher:
    def __init__(self, master):
        UpdateConfigfile("current_page", 0)
        # Defining variables
        self.config = Configfile()
        self.icons = []
        
        self.home_page = ttk.Frame(master)
        
        # Create button_container
        self.button_container = ttk.Labelframe(self.home_page, text='Applications', style='info.TLabelframe')

        # Configure button container rows and columns
        for x in range(0, 4):
            self.button_container.columnconfigure(x, weight=3)
        for x in range(0, 3):
            self.button_container.rowconfigure(x, weight=1)

        # Load images
        try:
            # If self.icons are found
            for x in range(12):
                self.icon = tk.PhotoImage(file=self.config.image_locations[x])
                self.icons.append(self.icon)
        except tk.TclError:
            # if self.icons are not found
            Messagebox.show_error(title="Error", message="self.icons not found! Reverting to default self.icons.")
            self.icons = []
            for x in range(12):
                self.icons.append(tk.PhotoImage(file=Assets.default_image_locations))

        # Create edit button
        self.is_editing = tk.IntVar()
        self.edit_button = ttk.Checkbutton(master=self.home_page, text="Edit buttons", style="warning.Roundtoggle.Toolbutton",
                                           variable=self.is_editing, command=self.edit_is_on)
        self.edit_button.pack(side="top", anchor="e", padx=35)

        # Create buttons
        self.buttons = []
        column = 0
        self.row = 0
        for i in range(12):
            # noinspection PyArgumentList
            self.button = ttk.Button(master=self.button_container, text=self.config.program_names[i],
                                     image=self.icons[i],
                                     bootstyle="secondary", compound="top",
                                     command=lambda n=i: self.open_program(n))
            self.buttons.append(self.button)
            self.button.grid(row=self.get_row(i), column=column, padx=5, pady=5, sticky="swen")
            # Update row
            if column != 3:
                column += 1
            else:
                column = 0
        # Pack button container
        self.button_container.pack(fill="both", padx="30", expand=True)

        # Secondary buttons
        self.secondary_button_container = ttk.LabelFrame(
            master=self.home_page,
            text="Secondary functions",
            style="warning")

        # Create end of class reminder button
        self.end_of_lesson_reminder_button_var = tk.IntVar(value=self.config.end_of_lesson_reminder)
        self.end_of_lesson_reminder_icon = tk.PhotoImage(
            file="Assets/Images/End_Of_Lesson_Reminder_Icon_White.png")
        self.end_of_lesson_reminder_button = ttk.Checkbutton(
            master=self.secondary_button_container,
            text="End of lesson reminder",
            style="info outline-toolbutton",
            command=lambda: UpdateConfigfile("end_of_lesson_reminder", self.end_of_lesson_reminder_button_var.get()),
            width=30, image=self.end_of_lesson_reminder_icon, compound="left",
            variable=self.end_of_lesson_reminder_button_var)
        self.end_of_lesson_reminder_button.pack(fill="x", pady=10, padx=10, side="left", expand=True)

        # Create classroom button
        self.classroom_icon = tk.PhotoImage(file="Assets/Images/Classroom_Icon.png")
        self.open_classroom_button = ttk.Button(master=self.secondary_button_container, text="Open Classroom",
                                                style="success", width=30, image=self.classroom_icon, compound="left",
                                                command=self.open_link_in_selected_browser)
        self.open_classroom_button.pack(fill="x", pady=10, padx=10, side="left", expand=True)

        # Pack secondary button container
        self.secondary_button_container.pack(fill="both", padx=30, pady=20, side="bottom")

        # self.home_page.grid(column = 0, row = 0, sticky = 'nsew')


    def open_program(self, index):
        if self.is_editing.get() == 1:
            # If editing is enabled, it calls the ChangeButtonSettings class
            ChangeButtonSettings(index, self.home_page)
        else:
            # If editing is not enabled
            if self.config.program_locations[index] == "default":
                # If button is not set up
                messagebox.showinfo(title="Error", message="You must set the location of a program!")
            else:
                try:
                    os.startfile(self.config.program_locations[index])
                except FileNotFoundError:
                    messagebox.showerror(title="Error", message="Program not found!")

    def edit_is_on(self):
        # This function runs whenever the edit button is pressed, and it turns editing on
        if self.is_editing.get() == 0:
            # Turn editing off
            for button in self.buttons:
                button.config(bootstyle="secondary")
        else:
            # Turn editing on
            for button in self.buttons:
                button.config(bootstyle="warning")

    def open_link_in_selected_browser(self):
        # This function opens the link in the browser selected by the user
        if self.config.browser == "system default":
            os.system(f"start {Assets.classroom_link}")
        else:
            if self.config.browser == "firefox":
                os.system(f"start {self.config.browser} --private-window {Assets.classroom_link}")
            else:
                os.system(f"start {self.config.browser} --guest {Assets.classroom_link}")

    def get_row(self, index):
        if 7 < index <= 11:
            self.row = 2
        elif 3 < index <= 7:
            self.row = 1
        else:
            self.row = 0
        return self.row
