import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox


class EditTodo:
    def __init__(self, master, title, description, index, update_widget):
        self.index = index

        # Creating top_level
        self.top_level = ttk.Toplevel(master)
        self.top_level.geometry("600x160")
        self.top_level.grab_set()
        self.top_level.title("Edit settings for task")

        self.update_widget = update_widget

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
            self.update_widget(self.title_entry_var.get(), self.description_entry_var.get())
        else:
            Messagebox.show_warning(title="Warning!", message="You must insert a title!")

    def close_pop_up(self):
        self.top_level.destroy()
