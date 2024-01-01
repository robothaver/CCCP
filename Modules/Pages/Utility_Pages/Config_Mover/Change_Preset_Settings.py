import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from Modules.Configfile.Config import Configfile
from tkinter import messagebox
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Utility_Pages.Config_Mover import Copy_Save_File_To_And_From_Pc


class ChangePresetSettings:
    def __init__(self, master):
        # This class gets called by CopySaveFileToAndFromPc whenever the edit preset settings button is pressed

        # Define variables
        self.master = master
        self.config = Configfile()

        # Create top level
        self.top_level = ttk.Toplevel(master)
        self.top_level.geometry("600x586")
        self.top_level.title("Change preset settings")
        self.top_level.grab_set()

        # Create tabel
        column = ["Backup options"]
        self.tabel = ttk.Treeview(master=self.top_level, columns=column, style="secondary", show="headings")
        self.tabel.heading('Backup options', text="Backup options")
        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)

        # Load in preset names to tabel
        for i, location in enumerate(self.config.preset_name):
            self.tabel.insert('', 0, values=[location], iid=f"{i}")
        self.tabel.pack(padx=10, pady=10, fill="both")

        # Create the main container
        main_container = ttk.LabelFrame(master=self.top_level, text="Change attributes for selected preset",
                                        style="info")

        # Create preset name entry widgets
        preset_name_entry_frame = ttk.Frame(master=main_container)
        preset_name_label = ttk.Label(master=preset_name_entry_frame,
                                      text="Preset name", width=22)
        self.preset_name_entry_var = tk.StringVar()
        preset_name_entry = ttk.Entry(master=preset_name_entry_frame,
                                      textvariable=self.preset_name_entry_var)
        # Packing
        preset_name_label.pack(side="left", padx=5)
        preset_name_entry.pack(side="left", fill="x", padx=5, expand=1)
        preset_name_entry_frame.pack(fill="x", pady=10)

        # Create preset source entry widgets
        preset_source_entry_frame = ttk.Frame(master=main_container)
        preset_source_entry_label = ttk.Label(master=preset_source_entry_frame,
                                              text="Save source location", width=22)
        self.preset_source_entry_var = tk.StringVar()
        preset_source_entry = ttk.Entry(master=preset_source_entry_frame,
                                        textvariable=self.preset_source_entry_var)
        preset_input_locate_button = ttk.Button(master=preset_source_entry_frame, text="locate",
                                                command=lambda: self.locate_file(0))
        # Packing
        preset_source_entry_label.pack(side="left", padx=5)
        preset_source_entry.pack(side="left", fill="x", padx=5, expand=1)
        preset_input_locate_button.pack(side="left", padx=5)
        preset_source_entry_frame.pack(fill="x", pady=10)

        # Create preset destination entry widgets
        preset_destination_entry_frame = ttk.Frame(master=main_container)
        preset_destination_label = ttk.Label(master=preset_destination_entry_frame,
                                             text="Save destination location", width=22)
        self.preset_destination_entry_var = tk.StringVar()
        preset_destination_entry = ttk.Entry(master=preset_destination_entry_frame,
                                             textvariable=self.preset_destination_entry_var)
        preset_destination_locate_button = ttk.Button(master=preset_destination_entry_frame, text="locate",
                                                      command=lambda: self.locate_file(1))
        # Packing
        preset_destination_label.pack(side="left", padx=5)
        preset_destination_entry.pack(side="left", fill="x", padx=5, expand=1)
        preset_destination_locate_button.pack(side="left", padx=5)
        preset_destination_entry_frame.pack(fill="x", pady=10)

        # Create bottom frame
        bottom_frame = ttk.LabelFrame(main_container, style="secondary",
                                      text="Change launch application button setting")
        # Create launch application check button widgets
        launch_application_check_button_frame = ttk.Frame(bottom_frame)
        self.launch_application_check_button_var = tk.IntVar()
        launch_application_check_button = ttk.Checkbutton(launch_application_check_button_frame,
                                                          text="Should launch application",
                                                          variable=self.launch_application_check_button_var,
                                                          style="info round-togglebutton",
                                                          command=self.change_launch_application_setting)
        launch_application_check_button.pack(side="left", padx=5)
        launch_application_check_button_frame.pack(fill="x", pady=10)

        # Create launch application widgets
        launch_application_frame = ttk.Frame(bottom_frame)
        self.launch_application_label = ttk.Label(launch_application_frame, text="Application location:",
                                                  bootstyle="secondary")
        self.launch_application_label.pack(side="left", padx=5)
        self.launch_application_entry_var = tk.StringVar()
        self.launch_application_entry = ttk.Entry(launch_application_frame,
                                                  textvariable=self.launch_application_entry_var, bootstyle="secondary",
                                                  state="disabled")
        self.launch_application_entry.pack(side="left", padx=5, expand=1, fill="x")
        self.application_locate_button = ttk.Button(master=launch_application_frame, text="locate",
                                                    command=lambda: self.locate_file(2), bootstyle="secondary",
                                                    state="disabled")
        self.application_locate_button.pack(side="left", padx=5)

        # Pack launch application frame
        launch_application_frame.pack(fill="x", pady=5)

        # Pack bottom frame
        bottom_frame.pack(fill="x", expand=1, padx=10, pady=5)

        # Pack main container
        main_container.pack(fill="x", pady=10, padx=10)

        # Entry buttons
        button_frame = ttk.Frame(master=main_container)
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

    # noinspection PyArgumentList
    def change_launch_application_setting(self):
        # This function runs whenever the launch application check button is pressed
        if self.launch_application_check_button_var.get() == 1:
            self.enable_launch_application_option()
        else:
            self.disable_launch_application_option()

    def locate_file(self, index):
        # This function runs whenever one of the "locate" buttons is pressed
        if index <= 1:
            file = filedialog.askdirectory(title="Select directory")
        else:
            file = filedialog.askopenfilename(title="Select file")
        if file != ():
            if file != "":
                if index == 0:
                    self.preset_source_entry_var.set(file)
                elif index == 1:
                    self.preset_destination_entry_var.set(file)
                elif index == 2:
                    self.launch_application_entry_var.set(file)

    def enable_launch_application_option(self):
        # This function enables the launch application option
        self.launch_application_check_button_var.set(1)
        self.launch_application_label.config(bootstyle="info")
        self.launch_application_entry.config(bootstyle="info", state="normal")
        self.application_locate_button.config(bootstyle="info", state="normal")

    def disable_launch_application_option(self):
        # This function disables the launch application option
        self.launch_application_check_button_var.set(0)
        self.launch_application_label.config(bootstyle="secondary")
        self.launch_application_entry.config(bootstyle="secondary", state="disabled")
        self.application_locate_button.config(bootstyle="secondary", state="disabled")

    def update_entries_with_selected_item(self, event):
        # This function runs whenever the user selects one of the preset in the tabel
        selected_item = self.tabel.selection()
        try:
            # If the selection exists
            index = int(selected_item[0])
            if self.config.preset_application_location[index] != "":
                # If the preset has "launch application option" enabled
                self.enable_launch_application_option()
            else:
                # If the preset does not have "launch application option" enabled
                self.disable_launch_application_option()
            # Set the entries to the selected preset
            self.preset_name_entry_var.set(self.config.preset_name[index])
            self.preset_source_entry_var.set(self.config.preset_input[index])
            self.preset_destination_entry_var.set(self.config.preset_output[index])
            self.launch_application_entry_var.set(self.config.preset_application_location[index])
        except IndexError:
            pass

    # noinspection PyTypeChecker
    def apply_changes_for_option(self):
        # This function runs whenever the "apply" or "accept" button is pressed
        # This function changes the selected presets setting to the ones given by the user in the entry fields
        try:
            # If the selection is not empty
            selected_item = self.tabel.selection()
            index = int(selected_item[0])
            # Update tabel option name
            self.tabel.item(selected_item, values=[self.preset_name_entry_var.get()])
            # Update the config list with the new values (not the configfile)
            self.config.preset_name[index] = self.preset_name_entry_var.get()
            self.config.preset_input[index] = self.preset_source_entry_var.get()
            self.config.preset_output[index] = self.preset_destination_entry_var.get()
            if self.launch_application_check_button_var.get() == 1:
                # If the launch application option is enabled
                self.config.preset_application_location[index] = self.launch_application_entry_var.get()
            else:
                # If the launch application option is not enabled
                self.config.preset_application_location[index] = ""
        except IndexError:
            pass

    def delete_item(self):
        # This function runs whenever the "delete" button is pressed
        # This function removes the preset from the config list and the tabel (not the configfile)
        try:
            # If the preset is selected, get all options from tabel
            items = []
            for item in reversed(self.tabel.get_children()):
                items.append(item)

            # Get selected item
            index = items.index(self.tabel.selection()[0])
            selected_item = self.tabel.selection()[0]
            # Delete selected item
            self.tabel.delete(selected_item)
            # Create new lists to store new values
            new_names = []
            new_inputs = []
            new_outputs = []
            new_application_locations = []
            # Append values from the presets
            for i, name in enumerate(self.config.preset_name):
                if i != index:
                    new_names.append(name)
            for i, preset_input in enumerate(self.config.preset_input):
                if i != index:
                    new_inputs.append(preset_input)
            for i, preset_output in enumerate(self.config.preset_output):
                if i != index:
                    new_outputs.append(preset_output)
            for i, application_locations in enumerate(self.config.preset_application_location):
                if i != index:
                    new_application_locations.append(application_locations)
            self.config.preset_name = new_names
            self.config.preset_input = new_inputs
            self.config.preset_output = new_outputs
            self.config.preset_application_location = new_application_locations
        except IndexError:
            pass

    def add_item(self):
        # This function runs whenever the "add new option" button is pressed
        # This function add in a new preset with the settings given by the user
        if self.preset_name_entry_var.get() != "":
            # If a name is given
            if self.preset_source_entry_var.get() != "":
                # If a source is given
                if self.preset_destination_entry_var.get() != "":
                    # If a destination is given
                    self.tabel.insert('', 0, values=[self.preset_name_entry_var.get()],
                                      iid=str(len(self.config.preset_name)))
                    self.config.preset_name.append(self.preset_name_entry_var.get())
                    self.config.preset_input.append(self.preset_source_entry_var.get())
                    self.config.preset_output.append(self.preset_destination_entry_var.get())
                    self.config.preset_application_location.append(self.launch_application_entry_var.get())
                else:
                    messagebox.showwarning(title="Warning", message="You must set an output location!")
            else:
                messagebox.showwarning(title="Warning", message="You must set an input location!")
        else:
            messagebox.showwarning(title="Warning", message="You must give a name!")

    def close_pop_up(self):
        # This function runs whenever the "accept" or "cancel" button is pressed
        for widget in self.master.winfo_children():
            widget.destroy()
        self.top_level.destroy()
        self.top_level.grab_release()
        Copy_Save_File_To_And_From_Pc.CopySaveFileToAndFromPc(self.master)

    def save_changes(self):
        # This function runs whenever the "accept" button is pressed
        # This function updates the configfile with the values from the config lists
        self.apply_changes_for_option()
        # Update configfile
        UpdateConfigfile("preset_name", self.config.preset_name)
        UpdateConfigfile("preset_input", self.config.preset_input)
        UpdateConfigfile("preset_output", self.config.preset_output)
        UpdateConfigfile("preset_application_location", self.config.preset_application_location)
        # Close pop-up
        self.close_pop_up()
