import time
from datetime import timedelta
from Modules.Utilities.Calculate_Delta import CalculateDelta
from Modules.Dialogs.End_Of_Lesson_Reminder import EndOfLessonReminder
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Panels.Top_Panel.UI.Top_Panel_UI import TopPanelUI
from datetime import datetime
from Modules.Pages.Settings.Settings import Settings
from Modules.Configfile.Config import Configfile
from Assets import Assets
import ttkbootstrap as ttk
import tkinter as tk


class TopPanel(TopPanelUI):
    def __init__(self, master, style_controller):
        super().__init__(master)
        # Define variables
        self.config = Configfile()
        self.style_controller = style_controller

        self.theme_var.trace("w", self.change_theme)

        self.cooldown = False
        self.delta = CalculateDelta()
        self.time = datetime.strptime("12:55:00", "%H:%M:%S")
        # self.time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        self.refresh()
        self.refresh_time()
        self.greet()
        self.update_notifiers()

    def refresh(self):
        self.config = Configfile()
        self.theme_var.set(value=self.config.theme)
        self.theme_changer.set_menu(None, *self.style_controller.themes)
        self.show_enabled_widgets()

    def show_enabled_widgets(self):
        if self.config.enable_secondary_notifier:
            self.secondary_notifier.grid(column=0, row=0, sticky="ws", padx=5)
        else:
            self.secondary_notifier.grid_forget()
        if self.config.enable_primary_notifier:
            self.main_notifier.grid(row=1, column=0, sticky="w", padx=5)
        else:
            self.main_notifier.grid_forget()
        if self.config.enable_top_theme_selector:
            self.theme_changer.grid(row=1, column=1, sticky="e", padx=5)
        else:
            self.theme_changer.grid_forget()

    def change_theme(self, *args):
        # This function gets called whenever the user selects a theme
        self.style_controller.set_current_theme(self.theme_var.get())
        # self.time = datetime.strptime("15:39:55", "%H:%M:%S")

    def refresh_time(self):
        current_time = time.strftime("%H:%M:%S")
        current_year = time.strftime("%Y:%m:%d")
        clock_var = f"{current_year}\n{current_time}"
        self.clock_label_var.set(value=clock_var)
        self.clock_label.after(1000, self.refresh_time)

    def greet(self):
        current_hour = int(time.strftime("%H"))
        if current_hour <= 5:
            self.greet_label_var.set(value="Good evening!")
        elif current_hour < 12:
            self.greet_label_var.set(value="Good morning!")
        elif current_hour < 18:
            self.greet_label_var.set(value="Good afternoon!")
        elif current_hour <= 24:
            self.greet_label_var.set(value="Good evening!")
        self.greet_label.after(60000, self.greet)

    def update_widgets(self, main_notifier, secondary_notifier, show_navbar):
        self.main_notifier_var.set(main_notifier)
        self.secondary_notifier_var.set(secondary_notifier)
        if show_navbar and self.config.enable_progress_bar:
            self.progress_bar.grid(columnspan=2, sticky="we", padx=10, pady=(10, 5))
        else:
            self.progress_bar.grid_forget()

    def change_notifier_styles(self, style):
        self.main_notifier.config(bootstyle=style)
        self.progress_bar.config(bootstyle=style)

    def update_notifiers(self):
        self.delta.check_end_time(self.config, self.time)
        self.time += timedelta(seconds=1)
        self.progress_bar.config(value=self.delta.progress)
        if self.delta.is_lesson_over:
            # If the lesson has ended
            self.change_notifier_styles("success")
            self.show_dynamic_message()
            self.cooldown = False
        else:
            # If the lesson is still going
            self.change_notifier_styles("warning")
            self.show_ongoing_lesson_message()
            self.end_of_lesson_reminder()
        self.main_notifier.after(1000, self.update_notifiers)

    def show_ongoing_lesson_message(self):
        self.update_widgets(
            f"Time left of this class: {self.delta.time_left}",
            f"{self.delta.class_number + 1}. class ends at {self.config.break_pattern[self.delta.class_number][1]}",
            True
        )

    def show_dynamic_message(self):
        day_of_week = 4
        if self.delta.class_number == self.config.number_of_lessons_today - 1 and day_of_week == 4:
            # If It's friday and the lessons are over
            self.update_widgets(
                "You are done for this week! ☕",
                "Have a nice weekend!",
                False
            )
        elif day_of_week > 4:
            # If its weekend
            self.update_widgets(
                "Have a nice weekend! ☕",
                "",
                False
            )
        elif self.delta.class_number == self.config.number_of_lessons_today - 1:
            # If the day is over
            self.update_widgets(
                "You are done for the day ☕",
                f"1. class begins at {self.config.break_pattern[0][0]}",
                False
            )
        elif self.delta.class_number == 0 and self.delta.time_delta == 0:
            # If the day hasn't begun yet
            self.update_widgets(
                "",
                f"Your first class starts at {self.config.break_pattern[0][0]}",
                False
            )
        else:
            # If it is break time
            self.update_widgets(
                f"Break  ☕  remaining: {self.delta.time_left}",
                f"{self.delta.class_number + 2}. class begins at "
                f"{self.config.break_pattern[self.delta.class_number + 1][0]}",
                True
            )

    def end_of_lesson_reminder(self):
        """
        If enabled, the program will open a pop-up to remind the user that the lesson is close to the end
        :return: None
        """
        if not self.cooldown:
            if self.config.end_of_lesson_reminder == 1:
                if self.delta.time_delta <= timedelta(minutes=5):
                    self.cooldown = True
                    EndOfLessonReminder(message="The lesson is ending soon, it is time to prepare!")
