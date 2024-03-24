import ttkbootstrap as ttk
import json
from Modules.Pages.Utility_Pages.To_Do_List.Dialogs.Edit_Todo import EditTodo
from Modules.Pages.Utility_Pages.To_Do_List.Todo_Widget.UI.Todo_Widget_UI import TodoWidgetUI
from Modules.Pages.Utility_Pages.To_Do_List.Todo_File.Update_To_Do_List import UpdateToDoList

TODO_File = "User config/To_Do_List.json"


class TodoWidget(TodoWidgetUI):
    def __init__(self, master, title, description, index, task_deleted, is_done=0):
        # Parameters:
        #     master: main frame
        #     middle_frame: the frame which contains the whole page
        #     title: the text shown on the main container title label
        #     description: the text displayed on the children description label
        #     index: the index of the widget
        super().__init__(master, title)

        self.index = index
        self.is_widget_open = 0
        self.title = title
        self.description = description
        self.task_deleted = task_deleted

        self.check_button_var.set(is_done)
        self.delete_button.config(command=self.delete_task)
        self.check_button.config(command=self.mark_task_as_done)
        self.edit_button.config(
            command=lambda: EditTodo(master, self.title, self.description, index, self.update_todo)
        )
        self.open_button.config(command=lambda: self.open_widget(description))

        self.check_if_task_is_done()

    def check_if_task_is_done(self):
        if self.check_button_var.get() == 1:
            self.check_button.config(image=self.check_button_selected_img)
            self.title_container.config(bootstyle="success")
            self.container_title_label.config(bootstyle="success inverse")
            self.open_button.config(bootstyle="success")
            self.edit_button.config(bootstyle="success")

    def open_widget(self, description):
        if self.is_widget_open == 0:
            self.open_button.config(image=self.widget_open_icon)
            self.create_children_container(description)
            self.is_widget_open = 1
        else:
            self.open_button.config(image=self.widget_closed_icon)
            self.children_container.destroy()
            self.is_widget_open = 0

    def update_wrap_length(self, *args):
        self.description_label.config(wraplength=self.description_label.winfo_width())

    def create_children_container(self, description):
        self.children_container = ttk.Frame(self.main_container, style="dark")
        self.children_container.pack(fill="x")
        if description == "":
            description = "No description"
        children_title_label = ttk.Label(self.children_container, text="Description:",
                                         font=('Arial', '16', 'bold'), style="dark inverse")
        children_title_label.pack(anchor="w", pady=(5, 0), padx=5)
        self.description_label = ttk.Label(self.children_container, text=description, font=('Arial', '11'),
                                           style="dark inverse")
        self.description_label.pack(anchor="w", pady=5, padx=5, fill="both", expand=True)
        self.description_label.bind('<Configure>', self.update_wrap_length)

    def mark_task_as_done(self):
        # This function runs whenever check_button is pressed
        if self.check_button_var.get() == 0:
            # If check_button was pressed
            self.check_button.config(image=self.check_button_deselected_img)
            self.title_container.config(bootstyle="secondary")
            self.container_title_label.config(bootstyle="secondary inverse")
            self.open_button.config(bootstyle="secondary")
            self.edit_button.config(bootstyle="secondary")
            UpdateToDoList("is_done", self.index, 0)
        if self.check_button_var.get() == 1:
            # If check_button was not pressed
            self.check_button.config(image=self.check_button_selected_img)
            self.title_container.config(bootstyle="success")
            self.container_title_label.config(bootstyle="success inverse")
            self.open_button.config(bootstyle="success")
            self.edit_button.config(bootstyle="success")
            UpdateToDoList("is_done", self.index, 1)

    def update_todo(self, title, description):
        self.title = title
        self.description = description
        self.container_title_label.config(text=title)
        if self.is_widget_open:
            self.description_label.config(text=description)

    def delete_task(self):
        # Destroying the widget
        self.main_container.destroy()
        with open(TODO_File, "r") as jsonFile:
            data = json.load(jsonFile)
        index = data['title'].index(self.title)
        del data['title'][index]
        del data['description'][index]
        del data['is_done'][index]
        with open(TODO_File, "w") as jsonFile:
            json.dump(data, jsonFile, indent=3)
        self.task_deleted(self.title)
