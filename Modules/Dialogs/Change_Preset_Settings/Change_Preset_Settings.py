import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.dialogs import Messagebox
from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Dialogs.Change_Preset_Settings.UI.Change_Preset_Settings_UI import ChangePresetSettingsUI
from Modules.Utilities.Locate_File import LocateFile


class ChangePresetSettings(ChangePresetSettingsUI):
    def __init__(self, master, update_page):
        super().__init__(master)
        self.config = Configfile()
        self.update_page = update_page

        # Load in preset names to tabel
        for i, location in enumerate(self.config.preset_name):
            self.tabel.insert('', i, values=[location], iid=f"{i}")
        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)

        self.locate_absolute_source_btn.config(command=lambda: self.locate_absolute_path(0))
        self.locate_relative_source_btn.config(command=lambda: self.locate_relative_path(0))
        self.preset_destination_locate_button.config(command=lambda: self.locate_absolute_path(1))
        self.application_locate_button.config(command=lambda: self.locate_absolute_path(2))

        self.launch_application_check_button.config(
            command=lambda: self.change_launch_application_setting(bool(self.launch_application_check_button_var.get()))
        )
        self.apply_button.config(command=self.apply_changes_for_option)
        self.add_button.config(command=self.add_item)
        self.delete_button.config(command=self.delete_item)
        self.accept_button.config(command=self.save_changes)

        self.top_level.mainloop()

    def change_launch_application_setting(self, is_active):
        # This function runs whenever the launch application check button is pressed
        if is_active:
            self.toggle_launch_application_option("info", "active")
        else:
            self.toggle_launch_application_option("secondary", "disabled")

    def update_entries(self, index, file):
        if index == 0:
            self.preset_source_entry_var.set(file)
        elif index == 1:
            self.preset_destination_entry_var.set(file)
        elif index == 2:
            self.launch_application_entry_var.set(file)

    def ask_locate_mode(self, index):
        if index == 0:
            option = Messagebox.show_question(message="What would you like to locate? file or folder",
                                              title="Choose locate option", parent=self.top_level,
                                              buttons=["File", "Folder"])
        elif index == 1:
            option = "Folder"
        else:
            option = "File"
        return option

    def locate_absolute_path(self, index):
        locate_mode = self.ask_locate_mode(index)
        if locate_mode == "File":
            location = LocateFile().get_absolute_path(0)
        else:
            location = LocateFile().get_absolute_path(1)
        if location is not None:
            self.update_entries(index, location)

    def locate_relative_path(self, index):
        locate_mode = self.ask_locate_mode(index)
        if locate_mode == "File":
            location = LocateFile().get_relative_path(0)
        else:
            location = LocateFile().get_relative_path(1)
        if location is not None:
            self.update_entries(index, location)

    def toggle_launch_application_option(self, style, state):
        is_on = 0 if state == "disabled" else 1
        self.launch_application_check_button_var.set(is_on)
        self.launch_application_label.config(bootstyle=style)
        self.launch_application_entry.config(bootstyle=style, state=state)
        self.application_locate_button.config(bootstyle=style, state=state)

    def update_entries_with_selected_item(self, event):
        # This function runs whenever the user selects one of the preset in the tabel
        selected_item = self.tabel.selection()
        if selected_item != ():
            index = self.tabel.index(selected_item)
            if self.config.preset_application_location[index] != "":
                self.change_launch_application_setting(True)
            else:
                # If the preset does not have "launch application option" enabled
                self.change_launch_application_setting(False)
            # Set the entries to the selected preset
            self.preset_name_entry_var.set(self.config.preset_name[index])
            self.preset_source_entry_var.set(self.config.preset_source[index])
            self.preset_destination_entry_var.set(self.config.preset_destination[index])
            self.launch_application_entry_var.set(self.config.preset_application_location[index])

    def delete_item(self):
        selected_item = self.tabel.selection()
        index = self.tabel.index(selected_item)
        if self.tabel.item(selected_item)["values"] != "":
            del self.config.preset_name[index]
            del self.config.preset_source[index]
            del self.config.preset_destination[index]
            del self.config.preset_application_location[index]
            self.tabel.delete(selected_item)

    def apply_changes_for_option(self):
        selected_item = self.tabel.selection()
        index = self.tabel.index(selected_item)
        self.tabel.item(selected_item, values=[self.preset_name_entry_var.get()])
        if self.preset_has_been_changed(index) and self.validate_entries():
            self.update_selected_preset(index)

    def validate_entries(self):
        if self.preset_name_entry_var.get() != "":
            if self.preset_source_entry_var.get() != "":
                if self.preset_destination_entry_var.get() != "":
                    return True
                else:
                    messagebox.showwarning(title="Warning", message="You must set an output location!")
            else:
                messagebox.showwarning(title="Warning", message="You must set an input location!")
        else:
            messagebox.showwarning(title="Warning", message="You must set a name!")
        return False

    def update_selected_preset(self, index):
        self.config.preset_name[index] = self.preset_name_entry_var.get()
        self.config.preset_source[index] = self.preset_source_entry_var.get()
        self.config.preset_destination[index] = self.preset_destination_entry_var.get()
        if self.launch_application_check_button_var.get() == 1:
            # If the launch application option is enabled
            self.config.preset_application_location[index] = self.launch_application_entry_var.get()
        else:
            # If the launch application option is not enabled
            self.config.preset_application_location[index] = ""

    def preset_has_been_changed(self, index):
        return (
                self.preset_source_entry_var.get() != self.config.preset_source[index]
                or self.preset_destination_entry_var.get() != self.config.preset_destination[index]
                or self.launch_application_entry_var.get() != self.config.preset_application_location[index]
                or self.launch_application_check_button_var.get() == 0 and self.launch_application_entry_var.get() != ""
                or self.validate_name()
        )

    def validate_name(self):
        if self.preset_name_entry_var.get() != "":
            if self.preset_name_entry_var.get() not in self.config.preset_name:
                return True
            messagebox.showwarning(title="Warning", message="Name already in list!")
        else:
            messagebox.showwarning(title="Warning", message="You must give a name!")

    def add_item(self):
        # This function runs whenever the "add new option" button is pressed
        # This function add in a new preset with the settings given by the user
        if self.validate_name():
            # If a name is given
            if self.preset_source_entry_var.get() != "":
                # If a source is given
                if self.preset_destination_entry_var.get() != "":
                    # If a destination is given
                    self.tabel.insert('', len(self.config.preset_name), values=[self.preset_name_entry_var.get()])
                    self.config.preset_name.append(self.preset_name_entry_var.get())
                    self.config.preset_source.append(self.preset_source_entry_var.get())
                    self.config.preset_destination.append(self.preset_destination_entry_var.get())
                    if self.launch_application_check_button_var.get() == 1:
                        self.config.preset_application_location.append(self.launch_application_entry_var.get())
                    else:
                        self.config.preset_application_location.append("")
                else:
                    messagebox.showwarning(title="Warning", message="You must set an output location!")
            else:
                messagebox.showwarning(title="Warning", message="You must set an input location!")

    def save_changes(self):
        UpdateConfigfile("preset_name", self.config.preset_name)
        UpdateConfigfile("preset_source", self.config.preset_source)
        UpdateConfigfile("preset_destination", self.config.preset_destination)
        UpdateConfigfile("preset_application_location", self.config.preset_application_location)
        # Close pop-up
        self.top_level.destroy()
        self.update_page()
