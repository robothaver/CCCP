import ttkbootstrap as ttk
import tkinter as tk


class HomePageUI:
    def __init__(self, master):
        self.master_container = ttk.Frame(master)

        # Create button_container
        self.button_container = ttk.Labelframe(self.master_container, text='Applications', style='info.TLabelframe')

        # Configure button container rows and columns
        for x in range(0, 4):
            self.button_container.columnconfigure(x, weight=3)
        for x in range(0, 3):
            self.button_container.rowconfigure(x, weight=1)

        # Create edit button
        self.is_editing = tk.IntVar()
        self.edit_button = ttk.Checkbutton(master=self.master_container, text="Edit buttons",
                                           style="warning.Roundtoggle.Toolbutton",
                                           variable=self.is_editing, command=self.is_editing)
        self.edit_button.pack(side="top", anchor="e", padx=35)

        # Pack button container
        self.button_container.pack(fill="both", padx="30", expand=True)

        # Secondary buttons
        self.secondary_button_container = ttk.LabelFrame(
            master=self.master_container,
            text="Secondary functions",
            style="warning")

        # Create end of class reminder button
        self.end_of_lesson_reminder_button_var = tk.IntVar()
        self.end_of_lesson_reminder_icon = tk.PhotoImage(
            file="Assets/Images/End_Of_Lesson_Reminder_Icon_White.png")
        self.end_of_lesson_reminder_button = ttk.Checkbutton(
            master=self.secondary_button_container,
            text="End of lesson reminder",
            style="info outline-toolbutton",
            width=30, image=self.end_of_lesson_reminder_icon, compound="left",
            variable=self.end_of_lesson_reminder_button_var)
        self.end_of_lesson_reminder_button.pack(fill="x", pady=10, padx=10, side="left", expand=True)

        # Create classroom button
        self.classroom_icon = tk.PhotoImage(file="Assets/Images/Classroom_Icon.png")
        self.open_classroom_button = ttk.Button(master=self.secondary_button_container, text="Open Classroom",
                                                style="success", width=30, image=self.classroom_icon, compound="left")
        self.open_classroom_button.pack(fill="x", pady=10, padx=10, side="left", expand=True)

        # Pack secondary button container
        self.secondary_button_container.pack(fill="both", padx=30, pady=20, side="bottom")
