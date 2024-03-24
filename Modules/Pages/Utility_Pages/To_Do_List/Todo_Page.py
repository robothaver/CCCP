import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from Modules.Pages.Utility_Pages.To_Do_List.Dialogs.Add_New_Todo import AddNewTodo
from Modules.Pages.Utility_Pages.To_Do_List.Todo_File.Todo_File import TodoFile
from Modules.Pages.Utility_Pages.To_Do_List.Todo_Widget.Todo_Widget import TodoWidget


class TodoPage:
    def __init__(self, master, show_dashboard):
        self.master = master
        self.config = TodoFile()

        self.no_tasks_message = "There are no tasks :)"
        self.no_tasks = False
        self.selected_page_index = 1

        # Creating back_frame
        self.master_container = ttk.Frame(master)
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        back_frame = ttk.Frame(self.master_container)
        back_button = ttk.Button(back_frame, text="Back", command=show_dashboard,
                                 image=self.back_button_icon, compound="left")
        back_button.pack(side="left", padx=10, pady=(2, 10))
        self.add_icon = ttk.PhotoImage(file="Assets/Images/add_icon.png")
        add_new_task_button = ttk.Button(
            back_frame, text="Add new task",
            style="warning",
            image=self.add_icon,
            compound="left",
            command=lambda: AddNewTodo(master, self.todo_container, self.add_new_widget)
        )
        add_new_task_button.pack(side="right", padx=10, pady=(2, 10))
        back_frame.pack(fill="x")

        # Creating separator
        separator = ttk.Separator(self.master_container)
        separator.pack(fill="x", padx=10, pady=5)

        top_frame = ttk.Frame(self.master_container)
        self.selected_page = tk.IntVar(value=0)
        button_style = "info outline-toolbutton"
        show_all_button = ttk.Radiobutton(top_frame, text="All tasks", style=button_style,
                                          variable=self.selected_page, value=0, command=self.show_selected_page)
        show_all_button.pack(side="left", fill="x", padx=10, expand=1)
        show_done_button = ttk.Radiobutton(top_frame, text="Tasks done", style=button_style,
                                           variable=self.selected_page, value=1, command=self.show_selected_page)
        show_done_button.pack(side="left", fill="x", padx=10, expand=1)
        show_tasks_to_do = ttk.Radiobutton(top_frame, text="Tasks to do", style=button_style,
                                           variable=self.selected_page, value=2, command=self.show_selected_page)
        show_tasks_to_do.pack(side="left", fill="x", padx=10, expand=1)
        top_frame.pack(pady=10, fill="x")

        self.todo_container = ScrolledFrame(self.master_container, autohide=True)
        self.todo_container.pack(fill="both", expand=1, padx=5, pady=5)
        self.show_selected_page()

    def show_tasks_done(self, config):
        tasks_finished = [i for i, is_done in enumerate(config.is_done) if is_done == 1]
        if len(tasks_finished) != 0:
            for index in tasks_finished:
                TodoWidget(self.todo_container, config.titles[index], config.descriptions[index],
                           index, self.task_deleted, 1)
        elif len(tasks_finished) == 0 and len(self.config.titles) != 0:
            no_tasks_label = ttk.Label(self.todo_container, text="No tasks are done :(",
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)
            self.no_tasks = True
        else:
            no_tasks_label = ttk.Label(self.todo_container, text=self.no_tasks_message,
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)
            self.no_tasks = True

    def show_all_tasks(self, config):
        if len(config.is_done) != 0:
            for i, state in enumerate(config.is_done):
                TodoWidget(self.todo_container, config.titles[i], config.descriptions[i], i, self.task_deleted, state)
        else:
            no_tasks_label = ttk.Label(self.todo_container, text=self.no_tasks_message,
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)
            self.no_tasks = True

    def show_unfinished_tasks(self, config):
        unfinished_tasks = [i for i, is_done in enumerate(config.is_done) if is_done == 0]
        if len(unfinished_tasks) != 0:
            for index in unfinished_tasks:
                TodoWidget(self.todo_container, config.titles[index], config.descriptions[index],
                           index, self.task_deleted)
        elif len(unfinished_tasks) == 0 and len(self.config.titles) != 0:
            no_tasks_label = ttk.Label(self.todo_container, text="No tasks to do :)",
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)
            self.no_tasks = True
        else:
            no_tasks_label = ttk.Label(self.todo_container, text=self.no_tasks_message,
                                       style="secondary", font=('Arial', '16', 'bold'))
            no_tasks_label.pack(pady=100)
            self.no_tasks = True

    def clear_todo_container(self):
        for child in self.todo_container.winfo_children():
            child.destroy()

    def add_new_widget(self, title, description):
        self.config.add_new_todo(title, description)
        if self.selected_page_index != 1:
            if self.no_tasks:
                self.clear_todo_container()
            TodoWidget(self.todo_container, title, description, len(self.config.titles) - 1, self.task_deleted)
        else:
            self.clear_todo_container()
            self.show_tasks_done(self.config)

    def task_deleted(self, title):
        self.config.remove_todo(title)
        if len(self.todo_container.winfo_children()) == 0:
            self.show_tasks_done(self.config)

    def show_selected_page(self):
        new_index = self.selected_page.get()
        self.no_tasks = False
        if self.selected_page_index != new_index:
            self.config = TodoFile()
            self.clear_todo_container()
            if new_index == 0:
                self.show_all_tasks(self.config)
            elif new_index == 1:
                self.show_tasks_done(self.config)
            else:
                self.show_unfinished_tasks(self.config)
        self.selected_page_index = new_index
