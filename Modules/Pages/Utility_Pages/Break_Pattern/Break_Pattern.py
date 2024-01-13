import tkinter as tk
import ttkbootstrap as ttk
from Modules.Pages.Dashboard import Application_Dashboard
from Assets import Assets
from ttkbootstrap.scrolled import ScrolledFrame


class BreakPattern:
    def __init__(self, master, show_dashboard):
        # Defining variables
        self.master = master
        self.current_page = 0

        # Creating back button
        back_frame = ttk.Frame(master)
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        back_button = ttk.Button(back_frame, text="Back", command=show_dashboard,
                                 image=self.back_button_icon, compound="left")
        back_button.pack(side="left", padx=10, pady=(0, 10))
        back_frame.pack(fill="x")

        # Create title frame
        title_frame = ttk.Frame(master)
        for x in range(3):
            title_frame.columnconfigure(x, weight=1)

        # Create switch back button <--
        switch_back_button = ttk.Button(title_frame, image=self.back_button_icon, command=lambda: self.change_page(-1))
        switch_back_button.grid(column=0, row=0)

        # Create title label
        title_label = ttk.Label(title_frame, text="Break patterns", font=('Arial', '16', 'bold'), style="info")
        title_label.grid(column=1, row=0)

        # Create switch forward button -->
        self.forward_icon = tk.PhotoImage(file="Assets/Images/forward_icon.png")
        switch_forward_button = ttk.Button(title_frame, image=self.forward_icon, command=lambda: self.change_page(1))
        switch_forward_button.grid(column=2, row=0)
        title_frame.pack(fill="x", pady=5)

        # Create current time label
        self.current_time_settings_var = tk.StringVar()
        current_time_settings_label = ttk.Label(master, textvariable=self.current_time_settings_var,
                                                font=('Arial', '13', 'bold'), style="warning")
        current_time_settings_label.pack(pady=5)

        # Create heading container
        headings_container = ScrolledFrame(master, style="info")

        # Configure heading container row and column settings
        for i in range(9):
            headings_container.rowconfigure(i, weight=1)
        headings_container.columnconfigure(0, weight=3)
        headings_container.columnconfigure(1, weight=3)

        # Create class label
        class_label = ttk.Label(headings_container, text="Class:", font=('Arial', '13'), style="info inverse", )
        class_label.grid(row=0, column=0, ipady=25)

        # Create time label
        time_label = ttk.Label(headings_container, text="Time:", font=('Arial', '13'), style="info inverse")
        time_label.grid(row=0, column=1, ipady=25)

        self.text_variables = []
        
        # Create class number and time labels
        for i, start_time in enumerate(Assets.break_pattern_45_10):
            if i % 2 != 0:
                # If the index is not even, the row will be secondary color

                # Create class number (1. class)
                new_class_number_frame = ttk.Frame(headings_container, style="secondary")
                new_class_number_label = ttk.Label(new_class_number_frame, text=f"{i + 1}. Class", font=('Arial', '12'),
                                                   style="secondary inverse")
                new_class_number_label.place(relx=.5, rely=.5, anchor="center")
                new_class_number_frame.grid(sticky="nsew", column=0, row=i + 1, ipady=30)
                new_class_label_frame = ttk.Frame(headings_container, style="secondary")
                # Create class number (7:30 - 8:15)
                class_time_label_var = tk.StringVar()
                class_label = ttk.Label(new_class_label_frame, textvariable=class_time_label_var,
                                        font=('Arial', '12'), style="secondary inverse")
                class_label.place(relx=.5, rely=.5, anchor="center")
                self.text_variables.append(class_time_label_var)
                new_class_label_frame.grid(sticky="nsew", column=1, row=i + 1, ipady=30)
            else:
                # If the index is even the row will be dark color
                # Create class number (2. class)
                new_class_number_frame = ttk.Frame(headings_container, style="dark")
                new_class_number_label = ttk.Label(new_class_number_frame, text=f"{i + 1}. Class", font=('Arial', '12'),
                                                   style="dark inverse")
                new_class_number_label.place(relx=.5, rely=.5, anchor="center")
                new_class_number_frame.grid(sticky="nsew", column=0, row=i + 1, ipady=30)
                new_class_time_label_frame = ttk.Frame(headings_container, style="dark")
                # Create class number (8:25 - 9:10)
                class_time_label_var = tk.StringVar()
                class_time_label = ttk.Label(new_class_time_label_frame, textvariable=class_time_label_var,
                                             font=('Arial', '12'), style="dark inverse")
                class_time_label.place(relx=.5, rely=.5, anchor="center")
                self.text_variables.append(class_time_label_var)
                new_class_time_label_frame.grid(sticky="nsew", column=1, row=i + 1, ipady=30)

        headings_container.pack(pady=20, fill="both", padx=20, expand=1)
        self.set_page()

    def set_page(self):
        # This function runs whenever one of the navigation buttons is pressed
        # The function changes the time data according to the selected option
        if self.current_page == 0:
            self.current_time_settings_var.set(value="45 min 10 min break")
            for i, time in enumerate(self.text_variables):
                time.set(value=f"{Assets.break_pattern_45_10[i][0]} - {Assets.break_pattern_45_10[i][1]}")
        elif self.current_page == 1:
            self.current_time_settings_var.set(value="40 min 10 min break")
            for i, time in enumerate(self.text_variables):
                time.set(value=f"{Assets.break_pattern_40_10[i][0]} - {Assets.break_pattern_40_10[i][1]}")
        elif self.current_page == 2:
            self.current_time_settings_var.set(value="35 min 10 min break")
            for i, time in enumerate(self.text_variables):
                time.set(value=f"{Assets.break_pattern_35_10[i][0]} - {Assets.break_pattern_35_10[i][1]}")
        elif self.current_page == 3:
            self.current_time_settings_var.set(value="35 min 5 min break")
            for i, time in enumerate(self.text_variables):
                time.set(value=f"{Assets.break_pattern_35_05[i][0]} - {Assets.break_pattern_35_05[i][1]}")

    def change_page(self, amount):
        # This function changes between the pages
        if 0 <= self.current_page + amount < 5:
            self.current_page += amount
        self.set_page()
