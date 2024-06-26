from tkinter import filedialog
from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
import ttkbootstrap as ttk
import tkinter as tk

from Modules.Utilities.Locate_File import LocateFile


class ManageProjectOutputLocations:
    def __init__(self, master, update_widget):
        # Define variables
        self.config = Configfile()
        self.update_widget = update_widget

        # Create top level
        self.top_level = ttk.Toplevel(title="Change file output locations")
        self.top_level.minsize(width=600, height=360)
        self.top_level.transient(master)
        self.top_level.grab_set()

        # Create the main container
        self.main_container = ttk.Frame(master=self.top_level)

        # Create tabel
        column = ["File location"]
        self.tabel = ttk.Treeview(master=self.main_container, columns=column, style="secondary", show="headings")
        self.tabel.heading('File location', text="File locations")
        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)

        # Load datas to tabel
        for i, location in enumerate(self.config.project_output_locations):
            self.tabel.insert('', i, values=[location])
        self.tabel.pack(padx=10, pady=10, fill="both")

        # Create location entry widgets
        location_entry_frame = ttk.Frame(self.main_container)
        location_entry_label = ttk.Label(location_entry_frame, text="File destination location", style="info", )
        self.location_entry_var = tk.StringVar()
        location_entry = ttk.Entry(location_entry_frame, textvariable=self.location_entry_var)
        locate_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")
        self.locate_absolute_path_btn = ttk.Button(master=location_entry_frame, image=locate_icon)
        self.locate_absolute_path_btn.image = locate_icon
        relative_path_icon = tk.PhotoImage(file="Assets/Images/Find_Relative_Path.png")
        self.locate_relative_path_btn = ttk.Button(master=location_entry_frame, image=relative_path_icon)
        self.locate_relative_path_btn.image = relative_path_icon
        # Packing
        location_entry_label.pack(side="left", padx=5, pady=5)
        location_entry.pack(side="left", fill="x", expand=1, padx=5)
        self.locate_absolute_path_btn.pack(side="left", padx=5)
        self.locate_relative_path_btn.pack(side="left", padx=(0, 5))
        location_entry_frame.pack(fill="x", padx=5)

        # Create buttons
        button_frame = ttk.LabelFrame(self.main_container, text="Change location settings", style="info")
        # Create delete button
        self.delete_button = ttk.Button(master=button_frame, text="Remove location",
                                        command=self.remove_selected_location, style="warning", width=15)
        self.delete_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Create add button
        self.add_button = ttk.Button(master=button_frame, text="Add location",
                                     command=self.add_item, style="info", width=15)
        self.add_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Create apply changes
        self.apply_changes_button = ttk.Button(master=button_frame, text="Apply changes",
                                               command=self.apply_changes, style="success", width=15)
        self.apply_changes_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Packing
        button_frame.pack(fill="x", padx=10, pady=10)
        self.main_container.pack(fill="both", expand=True)

        # Create bottom frame
        self.bottom_frame = ttk.Frame(master=self.top_level)
        # Create buttons
        self.accept_button = ttk.Button(master=self.bottom_frame, text="Accept",
                                        command=self.save_changes, style="success", width=10)
        self.accept_button.pack(padx=10, pady=10, side="right")
        self.cancel_button = ttk.Button(master=self.bottom_frame, text="Cancel",
                                        command=self.close_pop_up, style="danger", width=10)
        self.cancel_button.pack(pady=10, side="right")
        self.bottom_frame.pack(fill="x", side="bottom")

        self.locate_absolute_path_btn.config(command=self.locate_absolute_path)
        self.locate_relative_path_btn.config(command=self.locate_relative_path)

        self.top_level.mainloop()

    def locate_absolute_path(self):
        location = LocateFile().get_absolute_path(1)
        if location is not None:
            self.location_entry_var.set(location)

    def locate_relative_path(self):
        location = LocateFile().get_relative_path(1)
        if location is not None:
            self.location_entry_var.set(location)

    def update_entries_with_selected_item(self, event):
        selected_item = self.tabel.selection()
        try:
            self.location_entry_var.set(self.tabel.item(selected_item)['values'][0])
        except IndexError:
            pass

    def remove_selected_location(self):
        selected_item = self.tabel.selection()
        if self.tabel.item(selected_item)["values"] != "":
            del self.config.project_output_locations[self.tabel.index(selected_item)]
            self.tabel.delete(selected_item)
        print(self.config.project_output_locations)

    def apply_changes(self):
        selected_item = self.tabel.selection()
        index = self.tabel.index(self.tabel.selection())
        print(index)
        new_path = self.location_entry_var.get()
        if new_path not in self.config.project_output_locations:
            self.tabel.item(selected_item, values=[new_path])
            try:
                self.config.project_output_locations[index] = new_path
            except IndexError:
                pass
            print(self.config.project_output_locations)

    def add_item(self):
        new_location = self.location_entry_var.get()
        if new_location != "" and new_location not in self.config.project_output_locations:
            self.config.project_output_locations.append(new_location)
            self.tabel.insert('', len(self.config.project_output_locations), values=[new_location])

    def save_changes(self):
        UpdateConfigfile("project_output_locations", self.config.project_output_locations)
        self.close_pop_up()

    def close_pop_up(self):
        self.update_widget()
        self.top_level.destroy()
        self.top_level.grab_release()
