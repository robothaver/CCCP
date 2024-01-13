import os
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from Assets import Assets
from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Home.Update_Button_Settings import UpdateButtonSettings
from Modules.Pages.Home.UI.Home_Page_UI import HomePageUI
from Modules.Utilities.Launch_Browser import LaunchBrowser


class HomePage(HomePageUI):
    def __init__(self, master):
        super().__init__(master)
        # Defining variables
        self.config = Configfile()
        self.icons = self.load_images()
        self.buttons = self.create_buttons()

        self.end_of_lesson_reminder_button_var.set(value=self.config.end_of_lesson_reminder)

        self.end_of_lesson_reminder_button.config(command=self.toggle_end_of_lesson_reminder)

        self.open_classroom_button.config(command=self.open_classroom)

        self.edit_button.config(command=self.edit_is_on)

    def toggle_end_of_lesson_reminder(self):
        UpdateConfigfile("end_of_lesson_reminder", bool(self.end_of_lesson_reminder_button_var.get()))

    def create_buttons(self):
        buttons = []
        for x in range(3):
            for y in range(4):
                # noinspection PyArgumentList
                index = len(buttons)
                button = ttk.Button(master=self.button_container,
                                    text=self.config.program_names[index],
                                    image=self.icons[index],
                                    bootstyle="secondary",
                                    compound="top",
                                    command=lambda i=index: self.open_program(i))
                buttons.append(button)
                button.grid(row=x, column=y, padx=5, pady=5, sticky="swen")
        return buttons

    def load_images(self):
        icons = []
        # Load images
        try:
            # Try loading icons
            for x in range(12):
                icons.append(tk.PhotoImage(file=self.config.image_locations[x]))
        except tk.TclError:
            # if an icon is not found
            Messagebox.show_error(title="Error", message="Icon not found! Reverting to default icons.")
            for x in range(12):
                icons.append(tk.PhotoImage(file=Assets.default_image_locations))
        return icons

    def update_button(self, index):
        self.config = Configfile()
        new_icon = tk.PhotoImage(file=self.config.image_locations[index])
        self.buttons[index].config(image=new_icon, text=self.config.program_names[index])
        self.buttons[index].image = new_icon

    def open_program(self, index):
        if self.is_editing.get() == 1:
            UpdateButtonSettings(index, self.config, self.update_button)
        else:
            # If editing is not enabled
            if self.config.program_locations[index] == "default":
                # If button is not set up
                messagebox.showinfo(title="Error", message="You must set the location of a program!")
            else:
                self.try_start_program(self.config.program_locations[index])

    def edit_is_on(self):
        if self.is_editing.get() == 0:
            # Turn editing off
            self.set_button_style("secondary")
        else:
            # Turn editing on
            self.set_button_style("warning")

    def set_button_style(self, style):
        for button in self.buttons:
            button.config(bootstyle=style)

    def open_classroom(self):
        LaunchBrowser(Assets.classroom_link, self.config.browser, is_guest=True)

    @staticmethod
    def try_start_program(program):
        try:
            os.startfile(program)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Program not found!")
