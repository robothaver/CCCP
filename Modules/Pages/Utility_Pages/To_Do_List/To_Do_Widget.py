import tkinter as tk
import ttkbootstrap as ttk
from Modules.Pages.Utility_Pages.To_Do_List.Update_To_Do_List import UpdateToDoList
import json
from Modules.Pages.Utility_Pages.To_Do_List.Generate_To_Do_File import GenerateToDoFile
# from Modules.Pages.Utility_Pages.To_Do_List.To_Do_List import ToDoList
import ttkbootstrap.dialogs


# noinspection PyArgumentList
class ToDoWidget:
    def __init__(self, master, middle_frame, title, description, index):
        # Parameters:
        #     master: main frame
        #     middle_frame: the frame which contains the whole page
        #     title: the text shown on the main container title label
        #     description: the text displayed on the children description label
        #     index: the index of the widget

        self.children_container = None
        self.index = index
        self.config = GenerateToDoFile()
        # Icons
        self.widget_open_icon = tk.PhotoImage(file="Assets/Images/icons8_double_right_24px.png")
        self.widget_closed_icon = tk.PhotoImage(file="Assets/Images/icons8_double_up_24px.png")
        self.check_button_Selected_img = tk.PhotoImage(file="Assets/Images/Check_Button_Selected_Icon.png")
        self.check_button_Deselected_img = tk.PhotoImage(file="Assets/Images/Check_Button_Deselected_Icon.png")
        self.delete_button_icon = tk.PhotoImage(file="Assets/Images/Delete_Button_Icon.png")
        self.edit_button_icon = tk.PhotoImage(file="Assets/Images/Edit_Button_Icon.png")

        self.is_widget_open = 0

        # Creating main container
        self.main_container = ttk.Frame(master)
        self.main_container.pack(fill="x", padx=20, pady=10)
        self.title_container = ttk.Frame(self.main_container, bootstyle="secondary")
        self.container_title_label = ttk.Label(self.title_container, text=title,
                                               font=('Arial', '16', 'bold'), style="secondary inverse")
        self.container_title_label.pack(padx=5, side="left")

        # Delete button
        delete_button = ttk.Button(self.title_container, image=self.delete_button_icon,
                                   style="danger",
                                   command=lambda: self.delete_task(middle_frame))
        delete_button.pack(side="right")

        # Creating check button
        self.check_button_var = tk.IntVar(value=self.config.is_done[index])
        self.check_button = ttk.Checkbutton(self.title_container, image=self.check_button_Deselected_img,
                                            style="success toolbutton", variable=self.check_button_var,
                                            command=self.mark_task_as_done)
        self.check_button.pack(side="right")

        self.edit_button = ttk.Button(self.title_container, image=self.edit_button_icon,
                                      command=lambda: EditToDoListItem(master, middle_frame, title, description, index),
                                      style="secondary")
        self.edit_button.pack(side="right")

        # Creating open button
        self.open_button = ttk.Button(self.title_container, image=self.widget_closed_icon,
                                      command=lambda: self.open_widget(description), style="secondary")
        self.open_button.pack(side="right", padx=1)
        self.title_container.pack(fill="x")
        self.check_if_task_is_done()

    def check_if_task_is_done(self):
        # This function runs whenever the constructor is called
        # It checks if the task is done and changes the style of the widget to match it
        if self.check_button_var.get() == 1:
            self.check_button.config(image=self.check_button_Selected_img)
            self.title_container.config(bootstyle="success")
            self.container_title_label.config(bootstyle="success inverse")
            self.open_button.config(bootstyle="success")
            self.edit_button.config(bootstyle="success")

    def open_widget(self, description):
        # This function runs whenever open_button is pressed
        if self.is_widget_open == 0:
            self.open_button.config(image=self.widget_open_icon)
            self.create_children_container(description)
            self.is_widget_open = 1
        else:
            self.open_button.config(image=self.widget_closed_icon)
            self.children_container.destroy()
            self.is_widget_open = 0

    def create_children_container(self, description):
        # This function runs whenever open_button is pressed
        # it generates a children frame which contains a title and the description from the config file
        self.children_container = ttk.Frame(self.main_container, style="dark")
        self.children_container.pack(fill="x")
        if description == "":
            description = "No description"
        children_title_label = ttk.Label(self.children_container, text="Description:",
                                         font=('Arial', '16', 'bold'), style="dark inverse")
        children_title_label.pack(anchor="w", pady=(5, 0), padx=5)
        description_label = ttk.Label(self.children_container, text=description, font=('Arial', '11'),
                                      style="dark inverse")
        description_label.pack(anchor="w", pady=5, padx=5)

    def mark_task_as_done(self):
        # This function runs whenever check_button is pressed
        if self.check_button_var.get() == 0:
            # If check_button was pressed
            self.check_button.config(image=self.check_button_Deselected_img)
            self.title_container.config(bootstyle="secondary")
            self.container_title_label.config(bootstyle="secondary inverse")
            self.open_button.config(bootstyle="secondary")
            self.edit_button.config(bootstyle="secondary")
            UpdateToDoList("is_done", self.index, 0)
        if self.check_button_var.get() == 1:
            # If check_button was not pressed
            self.check_button.config(image=self.check_button_Selected_img)
            self.title_container.config(bootstyle="success")
            self.container_title_label.config(bootstyle="success inverse")
            self.open_button.config(bootstyle="success")
            self.edit_button.config(bootstyle="success")
            UpdateToDoList("is_done", self.index, 1)

    def delete_task(self, middle_frame):
        # This function runs whenever the delete button is pressed
        # It modifies the config file bye removing the data at the current index
        # It clears the middle frame and calls the To_Do_List class

        # Destroying the widget
        self.main_container.destroy()

        # Modifying the config file
        with open("To_Do_List.json", "r") as jsonFile:
            data = json.load(jsonFile)
        new_titles = []
        new_descriptions = []
        new_is_done = []
        for i, title in enumerate(data['title']):
            if i != self.index:
                new_titles.append(title)
                new_descriptions.append(data['description'][i])
                new_is_done.append(data['is_done'][i])
        data['title'] = new_titles
        data['description'] = new_descriptions
        data['is_done'] = new_is_done
        with open("To_Do_List.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=3)

        # Clearing the middle_frame and calling To_Do_List class
        for widget in middle_frame.winfo_children():
            widget.destroy()
        # ToDoList(middle_frame)


class EditToDoListItem:
    def __init__(self, master, middle_frame, title, description, index):
        # This class gets called by the ToDoWidget class whenever the edit button is pressed
        # This class loads in all the arrays from the config file and shows them to the user
        # When the accept button is pressed the class saves the modifications by the user to the config file
        self.index = index
        self.master = middle_frame

        # Creating top_level
        self.top_level = ttk.Toplevel(master)
        self.top_level.geometry("600x160")
        self.top_level.grab_set()
        self.top_level.title("Edit settings for task")

        # Creating title_frame
        title_frame = ttk.Frame(self.top_level)
        title_label = ttk.Label(title_frame, text="Title:", font=('Arial', '11'), width=10)
        self.title_entry_var = tk.StringVar(value=title)
        title_entry = ttk.Entry(title_frame, textvariable=self.title_entry_var)
        title_label.pack(side="left", padx=5)
        title_entry.pack(padx=5, fill="x", expand=1)
        title_frame.pack(fill="x", pady=10)

        # Creating description_frame
        description_frame = ttk.Frame(self.top_level)
        description_label = ttk.Label(description_frame, text="Description:", font=('Arial', '11'), width=10)
        self.description_entry_var = tk.StringVar(value=description)
        self.description_entry = ttk.Entry(description_frame, textvariable=self.description_entry_var)
        description_label.pack(padx=5, anchor="w", side="left")
        self.description_entry.pack(fill="x", pady=10, padx=5, expand=1)
        description_frame.pack(fill="x")

        # Creating bottom_frame
        bottom_frame = ttk.Frame(self.top_level)
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
            data["title"][self.index] = (self.title_entry_var.get())
            data["description"][self.index] = (self.description_entry_var.get())
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
        # ToDoList(self.master)
