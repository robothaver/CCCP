import os.path
import File_Generator
from File_Generator import *
from tkinter import filedialog
from Update_Configfile import UpdateConfigfile


class EditFileOutputLocations:
    def __init__(self, master):
        # Define variables
        config = Configfile()
        self.master = master

        # Create top level
        self.top_level = ttk.Toplevel(title=f"Change file output locations")
        self.top_level.minsize(width=600, height=280)
        self.top_level.grab_set()

        # Create the main container
        self.main_container = ttk.Frame(master=self.top_level)

        # Create top left frame
        self.top_left_frame = ttk.Frame(master=self.main_container)

        # Create tabel
        column = ["File location"]
        self.tabel = ttk.Treeview(master=self.top_left_frame, columns=column, style="secondary", show="headings")
        self.tabel.heading('File location', text="File locations")

        # Load datas to tabel
        for location in config.file_output_locations:
            self.tabel.insert('', 0, values=location)

        # Create top right frame
        self.top_right_frame = ttk.Frame(master=self.main_container)

        # Create delete button
        self.delete_button = ttk.Button(master=self.top_right_frame, text="Remove location",
                                        command=self.remove_selected_location, style="warning", width=15)
        self.delete_button.pack(padx=(5, 10), pady=11, anchor="n")

        # Create add button
        self.add_button = ttk.Button(master=self.top_right_frame, text="Add location",
                                     command=self.add_item, style="info", width=15)
        self.add_button.pack(padx=(5, 10), pady=5, anchor="n")

        # Packing
        self.tabel.pack(padx=10, pady=10, fill="both")
        self.top_left_frame.pack(side="left", fill="both", expand=True)
        self.top_right_frame.pack(side="right", fill="y")
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

    def remove_selected_location(self):
        # This function gets called whenever the "remove location" button is pressed,
        # and it deletes the selected location
        if not self.tabel.item(self.tabel.selection())["values"] == "":
            self.tabel.delete(self.tabel.selection())

    def add_item(self):
        # This function gets called whenever the "add location" button is pressed, and it adds in the new location
        directory = filedialog.askdirectory(title="Select directory")
        if not len(directory) == 0:
            self.tabel.insert('', 0, values=[os.path.realpath(directory)])

    def save_changes(self):
        # This function runs whenever the "accept" button is pressed
        # This function updates the configfile with the values from the tabel and config list
        output_locations = []
        for item in self.tabel.get_children():
            output_locations.append(" ".join(self.tabel.item(item)['values']))
        UpdateConfigfile("file_output_locations", output_locations)
        self.close_pop_up()

    def close_pop_up(self):
        # This function runs whenever the "accept" or "cancel" button is pressed
        for widget in self.master.winfo_children():
            widget.destroy()
        self.top_level.destroy()
        self.top_level.grab_release()
        File_Generator.FileGenerator(self.master)
