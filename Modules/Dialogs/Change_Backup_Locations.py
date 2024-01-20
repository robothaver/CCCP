import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
from Modules.Configfile.Config import Configfile
from tkinter import messagebox
from Modules.Configfile.Update_Configfile import UpdateConfigfile


class ChangeBackupLocations:
    def __init__(self, master):
        # This class gets called by the BackupPage class

        # Define variables
        self.master = master
        self.config = Configfile()

        # Create_Top_Level
        self.top_level = ttk.Toplevel(title=f"Change the settings for backup options")
        self.top_level.minsize(width=600, height=430)
        self.top_level.transient(master)
        self.top_level.grab_set()

        # Create_tabel
        column = ["Backup options"]
        self.tabel = ttk.Treeview(master=self.top_level, columns=column, style="secondary", show="headings")
        self.tabel.heading('Backup options', text="Backup options")
        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)
        for location in self.config.file_backup_names:
            self.tabel.insert('', 0, values=[location])
        self.tabel.pack(padx=10, pady=10, fill="both")

        # Entries
        selected_item_frame = ttk.LabelFrame(master=self.top_level, text="Change attributes for selected item",
                                             style="info")
        file_backup_name_entry_frame = ttk.Frame(master=selected_item_frame)
        self.file_backup_name_entry_var = tk.StringVar()
        file_backup_name_label = ttk.Label(master=file_backup_name_entry_frame,
                                           text="Backup option name:", width=20)
        file_backup_name_entry = ttk.Entry(master=file_backup_name_entry_frame,
                                           textvariable=self.file_backup_name_entry_var)

        file_backup_source_entry_frame = ttk.Frame(master=selected_item_frame)
        file_backup_source_label = ttk.Label(master=file_backup_source_entry_frame,
                                             text="File backup source:", width=20)
        self.file_backup_source_entry_var = tk.StringVar()
        file_backup_location_entry = ttk.Entry(master=file_backup_source_entry_frame,
                                               textvariable=self.file_backup_source_entry_var)
        locate_button = ttk.Button(master=file_backup_source_entry_frame, text="locate", command=self.locate_file)

        # Packing
        file_backup_name_entry_frame.pack(fill="x")
        file_backup_name_label.pack(side="left", padx=15, pady=10)
        file_backup_name_entry.pack(side="left", padx=15, pady=10, fill="x", expand=True)
        file_backup_source_entry_frame.pack(pady=1, fill="x")
        file_backup_source_label.pack(side="left", padx=15, pady=10)
        file_backup_location_entry.pack(side="left", padx=15, pady=10, fill="x", expand=True)
        locate_button.pack(padx=(0, 15), side="left")
        selected_item_frame.pack(fill="x", padx=15)

        # Entry buttons
        button_frame = ttk.Frame(master=selected_item_frame)
        apply_button = ttk.Button(master=button_frame, text="Apply changes",
                                  command=self.apply_changes_for_option, style="success")
        delete_button = ttk.Button(master=button_frame, text="Delete option",
                                   command=self.delete_item, style="danger")
        add_button = ttk.Button(master=button_frame, text="Add new option",
                                command=self.add_item, style="info")

        # Packing
        apply_button.pack(pady=10, padx=15, side="left")
        delete_button.pack(pady=10, padx=15, side="left")
        add_button.pack(pady=10, padx=15, side="left")
        button_frame.pack()

        # Bottom buttons
        cancel_button = ttk.Button(master=self.top_level, text="Cancel",
                                   command=self.close_pop_up, style="danger", width=10)
        accept_button = ttk.Button(master=self.top_level, text="Accept",
                                   command=self.save_changes, style="success", width=10)
        accept_button.pack(padx=15, pady=10, side="right", anchor="s")
        cancel_button.pack(padx=15, pady=10, side="right", anchor="s")
        self.top_level.mainloop()

    def locate_file(self):
        # This function runs whenever the "locate" button is pressed
        file = filedialog.askdirectory(title="Select directory")
        self.file_backup_source_entry_var.set(file)

    def update_entries_with_selected_item(self, event):
        # This function runs whenever the user selects one of the preset in the tabel
        selected_item = self.tabel.selection()
        try:
            # If the selection exists
            index = self.config.file_backup_names.index(self.tabel.item(selected_item)['values'][0])
            self.file_backup_name_entry_var.set(self.config.file_backup_names[index])
            self.file_backup_source_entry_var.set(self.config.file_backup_locations[index])
        except IndexError:
            pass

    def apply_changes_for_option(self):
        # This function runs whenever the "apply" or "accept" button is pressed
        # This function changes the selected backup option setting to the ones given by the user in the entry fields
        try:
            # If the selection exists
            selected_item = self.tabel.selection()
            index = self.config.file_backup_names.index(self.tabel.item(selected_item)['values'][0])
            # Update tabel option name
            self.tabel.item(selected_item, values=[self.file_backup_name_entry_var.get()])
            # Update the config list with the new values (not the configfile)
            self.config.file_backup_names[index] = self.file_backup_name_entry_var.get()
            self.config.file_backup_locations[index] = self.file_backup_source_entry_var.get()
        except IndexError:
            pass

    def delete_item(self):
        # This function runs whenever the "delete" button is pressed
        # This function removes the backup option from the config list and the tabel (not the configfile)
        try:
            # If the back option is selected, get all options from tabel

            # Get selected item
            selected_item = self.tabel.selection()
            index = self.config.file_backup_names.index(self.tabel.item(selected_item)['values'][0])
            # Delete selected item
            self.tabel.delete(selected_item)
            # Create new lists to store new values
            new_locations = []
            new_names = []
            # Append values from the backup settings
            for i, location in enumerate(self.config.file_backup_locations):
                if i != index:
                    new_locations.append(location)
            for i, name in enumerate(self.config.file_backup_names):
                if i != index:
                    new_names.append(name)
            self.config.file_backup_locations = new_locations
            self.config.file_backup_names = new_names
        except IndexError:
            pass

    def add_item(self):
        # This function runs whenever the "add new option" button is pressed
        # This function add in a new backup option with the settings given by the user
        if self.file_backup_name_entry_var.get() != "":
            # If a name is given
            if self.file_backup_source_entry_var.get() != "":
                # If a source is given
                if self.check_if_max_number_is_reached():
                    # If max number isn't reached
                    self.tabel.insert('', 0, values=[self.file_backup_name_entry_var.get()])
                    self.config.file_backup_names.append(self.file_backup_name_entry_var.get())
                    self.config.file_backup_locations.append(self.file_backup_source_entry_var.get())
                else:
                    messagebox.showwarning(title="Warning", message="The maximum number of backup options is 10!")
            else:
                messagebox.showwarning(title="Warning", message="You must give a location!")
        else:
            messagebox.showwarning(title="Warning", message="You must give a name!")

    def close_pop_up(self):
        # This function runs whenever the "accept" or "cancel" button is pressed
        for widget in self.master.winfo_children():
            widget.destroy()
        self.top_level.destroy()
        self.top_level.grab_release()

    def save_changes(self):
        # This function runs whenever the "accept" button is pressed
        # This function updates the configfile with the values from the tabel and config list
        self.apply_changes_for_option()
        file_backup_names = []
        for item in reversed(self.tabel.get_children()):
            file_backup_names.append(" ".join(self.tabel.item(item)['values']))
        # Update configfile
        UpdateConfigfile("file_backup_names", file_backup_names)
        UpdateConfigfile("file_backup_locations", self.config.file_backup_locations)
        self.close_pop_up()

    def check_if_max_number_is_reached(self):
        # This function runs whenever the "add" button is pressed,
        # and it checks if the max number of backup options is reached
        file_backup_names = []
        for item in reversed(self.tabel.get_children()):
            file_backup_names.append(" ".join(self.tabel.item(item)['values']))
        if len(file_backup_names) < 10:
            return True
        else:
            return False
