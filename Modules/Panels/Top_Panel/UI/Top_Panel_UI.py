import ttkbootstrap as ttk
import tkinter as tk
from Assets import Assets


class TopPanelUI:
    def __init__(self, master):
        # Configure top_frame column and row settings
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        # Greet label
        self.greet_label_var = tk.StringVar()
        self.greet_label = ttk.Label(
            master=master,
            font=('Calibri', '28', 'bold'),
            style="info",
            textvariable=self.greet_label_var)
        self.greet_label.grid(column=0, row=0, sticky="wn", padx=5, pady=5)

        # Break notifier
        self.secondary_notifier_var = tk.StringVar()
        self.secondary_notifier = ttk.Label(
            master=master,
            font=('Calibri', '13', 'bold'),
            style="info", textvariable=self.secondary_notifier_var)

        # Clock label
        self.clock_label_var = tk.StringVar()
        self.clock_label = ttk.Label(
            master=master,
            font=('Calibri', '18'),
            bootstyle="secondary",
            justify="right",
            textvariable=self.clock_label_var)
        self.clock_label.grid(column=1, row=0, sticky="EN", pady=10, padx=5)

        # End of lesson timer
        self.main_notifier_var = tk.StringVar()
        self.main_notifier = ttk.Label(
            master=master,
            font=('Calibri', '18'),
            bootstyle="warning",
            justify="left",
            textvariable=self.main_notifier_var)

        # Theme selector
        self.theme_var = tk.StringVar()
        self.theme_changer = ttk.OptionMenu(
            master,
            self.theme_var,
            "Select theme"
        )

        self.progress_bar = ttk.Progressbar(master, mode="determinate")
