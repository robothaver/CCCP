from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Utilities.Assets import break_pattern_45_10
import tkinter as tk
import ttkbootstrap as ttk


class ChangeNOL:
    def __init__(self, master, refresh_top_panel):
        self.top_level = ttk.Toplevel(master=master, title="Set LPD", width=225, height=370)
        self.top_level.transient(master)
        self.top_level.grab_set()
        self.top_level.resizable(False, False)

        self.refresh_top_panel = refresh_top_panel
        self.config = Configfile()
        self.options = [str(i) for i in range(len(break_pattern_45_10) + 1)]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.values = []

        self.generate_widgets()
        self.create_buttons()

    def close_dialog(self):
        self.top_level.grab_release()
        self.top_level.destroy()

    def save_changes(self):
        lessons_per_day = [value.get() for value in self.values]
        UpdateConfigfile("number_of_lessons", lessons_per_day)
        self.refresh_top_panel()
        self.close_dialog()

    def generate_widgets(self):
        for i in range(5):
            frame = ttk.Frame(self.top_level)
            label = ttk.Label(frame, width=15, text=self.days[i], font=('calibri', '10', 'bold'))
            option_menu_var = tk.IntVar(value=self.config.number_of_lessons[i])
            option_menu = ttk.OptionMenu(frame, option_menu_var, "", *self.options)
            option_menu.config(width=2)
            label.pack(side="left")
            option_menu.pack(side="right")
            frame.pack(fill="x", padx=10, pady=15)
            self.values.append(option_menu_var)

    def create_buttons(self):
        button_frame = ttk.Frame(self.top_level)
        cancel_button = ttk.Button(button_frame, text="Cancel", style="danger", command=self.close_dialog)
        accept_button = ttk.Button(button_frame, text="Accept", style="success", command=self.save_changes)
        cancel_button.pack(side="left", padx=5, fill="x", expand=True)
        accept_button.pack(side="left", padx=5, fill="x", expand=True)
        button_frame.pack(pady=15, fill="x", side="bottom")
