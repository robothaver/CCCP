import json
import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.dialogs
from ttkbootstrap.scrolled import ScrolledFrame
import Application_Dashboard
from Generate_To_Do_File import GenerateToDoFile
from To_Do_Widget import ToDoWidget


class ToDoList:
    def __init__(self, master):
        self.master = master
        self.config = GenerateToDoFile()

        # Creating back_frame
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=self.back)
        back_button.pack(side="left", padx=10, pady=(2, 10))
        add_new_task_button = ttk.Button(back_frame, text="Add new task", style="warning",
                                         command=lambda: EditToDoList(master))
        add_new_task_button.pack(side="right", padx=10, pady=(2, 10))
        back_frame.pack(fill="x")

        # Creating separator
        separator = ttk.Separator(master)
        separator.pack(fill="x", padx=10, pady=5)

        # Creating top_frame
        top_frame = ttk.Frame(master)
        # This is where the user can choose which type of tasks they want to view
        self.selected_page = tk.IntVar(value=0)
        show_all_button = ttk.Radiobutton(top_frame, text="All tasks", style="info outline-toolbutton",
                                          variable=self.selected_page, value=0, command=self.show_selected_page)
        show_all_button.pack(side="left", fill="x", padx=10, expand=1)
        show_done_button = ttk.Radiobutton(top_frame, text="Tasks done", style="info outline-toolbutton",
                                           variable=self.selected_page, value=1, command=self.show_selected_page)
        show_done_button.pack(side="left", fill="x", padx=10, expand=1)
        show_tasks_to_do = ttk.Radiobutton(top_frame, text="Tasks to do", style="info outline-toolbutton",
                                           variable=self.selected_page, value=2, command=self.show_selected_page)
        show_tasks_to_do.pack(side="left", fill="x", padx=10, expand=1)
        top_frame.pack(pady=10, fill="x")

        # Creating scrolledframe
        self.scrolledframe = ScrolledFrame(master, autohide=True)
        self.scrolledframe.pack(fill="both", expand=1, padx=5, pady=5)

        # If the config file is empty
        if len(self.config.titles) == 0:
            no_tasks_label = ttk.Label(self.scrolledframe, text="There are no tasks :)",
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)

        self.show_selected_page()

    def back(self):
        # This function gets called whenever the back button is pressed
        # The function clears the middle_frame and calls Application_Dashboard class
        for widget in self.master.winfo_children():
            widget.destroy()
        Application_Dashboard.ApplicationDashboard(self.master)

    def show_selected_page(self):
        config = GenerateToDoFile()
        # Clearing scrolledframe
        for widget in self.scrolledframe.winfo_children():
            widget.destroy()

        number_of_tasks = 0
        # Generating ToDoWidgets with correct values
        if self.selected_page.get() == 0:
            # Shows all tasks
            for i, state in enumerate(config.is_done):
                ToDoWidget(self.scrolledframe, self.master, config.titles[i], config.descriptions[i], i)
                number_of_tasks += 1
            if number_of_tasks == 0:
                no_tasks_label = ttk.Label(self.scrolledframe, text="There are no tasks :)",
                                           style="secondary", font=('Arial', '16', 'bold'))
                no_tasks_label.pack(pady=100)
        if self.selected_page.get() == 1:
            # Shows tasks that are done
            for i, state in enumerate(config.is_done):
                if state == 1:
                    ToDoWidget(self.scrolledframe, self.master, config.titles[i], config.descriptions[i], i)
                    number_of_tasks += 1
            if number_of_tasks == 0 and len(self.config.titles) != 0:
                no_tasks_label = ttk.Label(self.scrolledframe, text="No tasks are done :(",
                                           style="secondary", font=('Arial', '16', 'bold'))
                no_tasks_label.pack(pady=100)
            else:
                no_tasks_label = ttk.Label(self.scrolledframe, text="There are no tasks :)",
                                           style="secondary", font=('Arial', '16', 'bold'))
                no_tasks_label.pack(pady=100)
        if self.selected_page.get() == 2:
            # Shows tasks that are not done
            for i, state in enumerate(config.is_done):
                if state != 1:
                    ToDoWidget(self.scrolledframe, self.master, config.titles[i], config.descriptions[i], i)
                    number_of_tasks += 1
            if number_of_tasks == 0:
                no_tasks_label = ttk.Label(self.scrolledframe, text="There are no tasks :)",
                                           style="secondary", font=('Arial', '16', 'bold'))
                no_tasks_label.pack(pady=100)


class EditToDoList:
    def __init__(self, master):
        # Define variables
        self.master = master

        # Create top level
        self.top_level = ttk.Toplevel(master)
        self.top_level.geometry("600x160")
        self.top_level.grab_set()
        self.top_level.title("Add new task")

        # Create title widget
        title_frame = ttk.Frame(self.top_level)
        title_label = ttk.Label(title_frame, text="Title:", font=('Arial', '11'), width=10)
        self.title_entry_var = tk.StringVar()
        title_entry = ttk.Entry(title_frame, textvariable=self.title_entry_var)
        # Packing
        title_label.pack(side="left", padx=5)
        title_entry.pack(padx=5, fill="x", expand=1)
        title_frame.pack(fill="x", pady=10)

        # Create description widgets
        description_frame = ttk.Frame(self.top_level)
        description_label = ttk.Label(description_frame, text="Description:", font=('Arial', '11'), width=10)
        self.description_entry_var = tk.StringVar()
        self.description_entry = ttk.Entry(description_frame, textvariable=self.description_entry_var)
        # Packing
        description_label.pack(padx=5, anchor="w", side="left")
        self.description_entry.pack(fill="x", pady=10, padx=5, expand=1)
        description_frame.pack(fill="x")

        # Create bottom frame
        bottom_frame = ttk.Frame(self.top_level)
        # Create buttons
        accept_button = ttk.Button(master=bottom_frame, text="Accept",
                                   command=self.save_changes, style="success", width=10)
        accept_button.pack(padx=5, pady=10, side="right")
        cancel_button = ttk.Button(master=bottom_frame, text="Cancel",
                                   command=self.close_pop_up, style="danger", width=10)
        cancel_button.pack(padx=(5, 15), pady=10, side="right")
        bottom_frame.pack(fill="x", side="bottom")

        self.top_level.mainloop()

    def save_changes(self):
        # This function gets called whenever the "accept" button is pressed,
        # and it saves the changes that have been made
        if self.title_entry_var.get() != "":
            with open("To_Do_List.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data["title"].append(self.title_entry_var.get())
            data["description"].append(self.description_entry_var.get())
            data["is_done"].append(0)
            with open("To_Do_List.json", "w") as jsonFile:
                json.dump(data, jsonFile, indent=3)
            self.close_pop_up()
        else:
            ttkbootstrap.dialogs.Messagebox.show_warning(title="Warning!", message="You must insert a title!")

    def close_pop_up(self):
        # This function gets called whenever the "accept" or "cancel" button is pressed
        for widget in self.master.winfo_children():
            widget.destroy()
        self.top_level.destroy()
        ToDoList(self.master)
