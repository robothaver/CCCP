from Calculate_Delta import CalculateDelta
import time
from datetime import timedelta
from Settings import *
from Assets import Assets
from Update_Configfile import UpdateConfigfile
from ttkbootstrap.dialogs import Messagebox


class TopGui:
    def __init__(self, master, style, middle_frame):
        # Define variables
        self.config = Configfile()
        self.style = style
        self.master = master
        self.middle_frame = middle_frame
        self.cooldown = False
        self.delta = CalculateDelta()

        # Configure top_frame column and row settings
        for x in range(0, 1):
            master.rowconfigure(x, weight=1)
            master.columnconfigure(x, weight=1)

        # Greet label
        self.greet_label_var = tk.StringVar()
        self.greet_label = ttk.Label(
            master=master,
            font=('Calibri', '28', 'bold'),
            style="info",
            textvariable=self.greet_label_var)
        self.greet_label.grid(column=0, row=0, sticky="wn", padx=5, pady=5)
        self.greet()

        # Break notifier
        self.break_notifier_var = tk.StringVar()
        self.break_notifier = ttk.Label(
            master=master,
            font=('Calibri', '13', 'bold'),
            style="info", textvariable=self.break_notifier_var)
        if self.config.top_lesson_number == 1:
            self.break_notifier.grid(column=0, row=0, sticky="ws", padx=5)

        # Clock label
        self.clock_label_var = tk.StringVar()
        self.clock_label = ttk.Label(
            master=master,
            font=('Calibri', '18'),
            bootstyle="secondary",
            justify="right",
            textvariable=self.clock_label_var)
        self.clock()
        self.clock_label.grid(column=1, row=0, sticky="EN", pady=10, padx=5)

        # End of lesson timer
        self.time_left_label_var = tk.StringVar()
        self.time_left_label = ttk.Label(
            master=master,
            font=('Calibri', '18'),
            bootstyle="warning",
            justify="left",
            textvariable=self.time_left_label_var)
        if self.config.top_end_of_lesson_timer == 1:
            self.time_left_label.grid(row=1, column=0, sticky="w", padx=5)

        # Theme selector
        if self.config.top_theme_selector == 1:
            self.theme_var = tk.StringVar()
            self.theme_changer = ttk.OptionMenu(
                master,
                self.theme_var,
                "Select theme",
                *Assets.theme_names,
                command=lambda theme: self.change_theme(theme))
            self.theme_changer.grid(row=1, column=1, sticky="e", padx=5)
        self.check_delta()
        self.end_of_lesson_reminder()

    def change_theme(self, theme):
        # This function gets called whenever the user selects a theme
        UpdateConfigfile("theme", theme)
        self.style.theme_use(theme)
        if Configfile().current_page == 4:
            for widget in self.middle_frame.winfo_children():
                widget.destroy()
            Settings(self.middle_frame, self.master, self.style)

    def clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_year = time.strftime("%Y:%m:%d")
        clock_var = f"{current_year}\n{current_time}"
        self.clock_label_var.set(value=clock_var)
        self.clock_label.after(1000, self.clock)

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

    def check_delta(self):
        if self.delta.check_if_lesson_is_over()[0]:
            # If the lesson has ended
            self.time_left_label.config(bootstyle="success")
            if self.delta.check_if_lesson_is_over()[1] == 8:
                # If the day is over
                self.time_left_label_var.set(value=f"You are done for the day ☕")
                self.break_notifier_var.set(f"1. class begins at {self.config.class_start[0]}")
            elif self.delta.check_if_lesson_is_over()[1] == 0:
                # If it is next day
                self.break_notifier_var.set("")
                self.time_left_label_var.set(value=f"Your first class starts at {self.config.class_start[0]}")
            else:
                # If it is break time
                self.time_left_label_var.set(value=f"Break  ☕  remaining: {self.delta.check_if_lesson_is_over()[2]}")
                self.break_notifier_var.set(f"{self.delta.check_if_lesson_is_over()[1] + 1}. class begins at "
                                            f"{self.config.class_start[self.delta.check_if_lesson_is_over()[1]]}")
        else:
            # If the lesson is still going
            self.time_left_label.config(bootstyle="warning")
            self.time_left_label_var.set(value=f"Time left of this class: {self.delta.time_difference()[1]}")
            self.break_notifier_var.set(f"{self.delta.check_if_lesson_is_over()[1]}. class")
        self.time_left_label.after(1000, self.check_delta)

    def end_of_lesson_reminder(self):
        # This function checks if the lesson is over and then checks if the cooldown is initialized or not
        # If everything is True the program will open a pop-up to remind the user that the lesson is close to the end
        if not self.delta.check_if_lesson_is_over()[0]:
            if not self.cooldown:
                if Configfile().end_of_lesson_reminder == 1:
                    if self.delta.time_difference()[0] <= timedelta(minutes=5):
                        self.cooldown = True
                        Messagebox.show_warning(title="End of lesson reminder",
                                                message="The lesson is ending soon, it is time to prepare!")
        else:
            self.cooldown = False
        self.time_left_label.after(5000, self.end_of_lesson_reminder)
