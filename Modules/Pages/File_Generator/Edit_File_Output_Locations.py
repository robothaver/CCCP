from Modules.Pages.File_Generator.File_Generator_Page import *
from tkinter import filedialog
from Modules.Configfile.Update_Configfile import UpdateConfigfile
import ttkbootstrap as ttk
import tkinter as tk


class EditFileOutputLocations:
    def __init__(self, update_widget):
        # Define variables
        self.config = Configfile()
        self.update_widget = update_widget

        # Create top level
        self.top_level = ttk.Toplevel(title=f"Change file output locations")
        self.top_level.minsize(width=600, height=360)
        self.top_level.grab_set()

        # Create the main container
        self.main_container = ttk.Frame(master=self.top_level)

        # Create tabel
        column = ["File location"]
        self.tabel = ttk.Treeview(master=self.main_container, columns=column, style="secondary", show="headings")
        self.tabel.heading('File location', text="File locations")
        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)

        # Load datas to tabel
        for location in self.config.file_output_locations:
            self.tabel.insert('', 0, values=[location])
        self.tabel.pack(padx=10, pady=10, fill="both")

        # Create location entry widgets
        location_entry_frame = ttk.Frame(self.main_container)
        location_entry_label = ttk.Label(location_entry_frame, text="File destination location", style="info", )
        self.location_entry_var = tk.StringVar()
        location_entry = ttk.Entry(location_entry_frame, textvariable=self.location_entry_var)
        location_entry_locate_button = ttk.Button(location_entry_frame, text="locate",
                                                  style="info", command=self.locate_file)
        # Packing
        location_entry_label.pack(side="left", padx=5, pady=5)
        location_entry.pack(side="left", fill="x", expand=1, padx=5)
        location_entry_locate_button.pack(side="left", padx=5)
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
        self.accept_button.pack(padx=5, pady=10, side="right")
        self.cancel_button = ttk.Button(master=self.bottom_frame, text="Cancel",
                                        command=self.close_pop_up, style="danger", width=10)
        self.cancel_button.pack(padx=(5, 15), pady=10, side="right")
        self.bottom_frame.pack(fill="x", side="bottom")

        self.top_level.mainloop()

    def update_entries_with_selected_item(self, event):
        # This function runs whenever the user selects one of the preset in the tabel
        selected_item = self.tabel.selection()
        try:
            self.location_entry_var.set(self.tabel.item(selected_item)['values'][0])
        except IndexError:
            pass

    def locate_file(self):
        # This function runs whenever the "locate" button is pressed
        file = filedialog.askdirectory(title="Select directory")
        self.location_entry_var.set(file)

    def remove_selected_location(self):
        # This function gets called whenever the "remove location" button is pressed,
        # and it deletes the selected location
        if not self.tabel.item(self.tabel.selection())["values"] == "":
            self.tabel.delete(self.tabel.selection())

    def apply_changes(self):
        # This function runs whenever the "apply changes" button is pressed
        selected_item = self.tabel.selection()
        self.tabel.item(selected_item, values=[self.location_entry_var.get()])

    def add_item(self):
        # This function gets called whenever the "add location" button is pressed, and it adds in the new location
        if self.location_entry_var.get() != "":
            self.tabel.insert('', 0, values=[self.location_entry_var.get()])

    def save_changes(self):
        # This function runs whenever the "accept" button is pressed
        # This function updates the self.configfile with the values from the tabel and self.config list
        self.apply_changes()
        output_locations = []
        for item in self.tabel.get_children():
            print(self.tabel.item(item)['values'])
            output_locations.append(" ".join(self.tabel.item(item)['values']))
        UpdateConfigfile("file_output_locations", output_locations)
        self.close_pop_up()

    def close_pop_up(self):
        # This function runs whenever the "accept" or "cancel" button is pressed
        self.update_widget()
        self.top_level.destroy()
        self.top_level.grab_release()
