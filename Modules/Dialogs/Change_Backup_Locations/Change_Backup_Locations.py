from ttkbootstrap.dialogs import Messagebox
from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Dialogs.Change_Backup_Locations.UI.Change_Backup_Locations_UI import ChangeBackupLocationsUI
from Modules.Utilities.Locate_File import LocateFile
from Modules.Utilities.Validate_Name import ValidateName


class ChangeBackupLocations(ChangeBackupLocationsUI):
    def __init__(self, master, update_page):
        super().__init__(master)
        # This class gets called by the BackupPage class

        self.config = Configfile()
        self.update_page = update_page

        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)
        self.load_items()

        self.locate_absolute_path_btn.config(command=self.locate_absolute_path)
        self.locate_relative_path_btn.config(command=self.locate_relative_path)

        self.add_button.config(command=self.add_item)
        self.delete_button.config(command=self.delete_item)
        self.apply_button.config(command=self.apply_changes_for_option)

        self.cancel_button.config(command=self.close_pop_up)
        self.accept_button.config(command=self.save_changes)

        self.top_level.mainloop()

    def locate_absolute_path(self):
        option = Messagebox.show_question(message="What would you like to locate? file or folder",
                                          title="Choose locate option", parent=self.top_level,
                                          buttons=["File", "Folder"])
        if option == "File":
            location = LocateFile().get_absolute_path(0)
        else:
            location = LocateFile().get_absolute_path(1)
        if location is not None:
            self.file_backup_source_entry_var.set(location)

    def locate_relative_path(self):
        option = Messagebox.show_question(message="What would you like to locate? file or folder",
                                          title="Choose locate option", parent=self.top_level,
                                          buttons=["File", "Folder"])
        if option == "File":
            location = LocateFile().get_relative_path(0)
        else:
            location = LocateFile().get_relative_path(1)
        if location is not None:
            self.file_backup_source_entry_var.set(location)

    def load_items(self):
        for i, location in enumerate(self.config.file_backup_names):
            self.tabel.insert('', i, values=[location])

    def update_entries_with_selected_item(self, event):
        # This function runs whenever the user selects one of the preset in the tabel
        try:
            # If the selection exists
            index = self.get_current_row_index()
            self.file_backup_name_entry_var.set(self.config.file_backup_names[index])
            self.file_backup_source_entry_var.set(self.config.file_backup_locations[index])
        except IndexError:
            pass

    def apply_changes_for_option(self):
        selected_item = self.tabel.selection()
        index = self.get_current_row_index()
        new_name = self.file_backup_name_entry_var.get()
        new_location = self.file_backup_source_entry_var.get()
        if len(self.config.file_backup_names) != 0:
            if ValidateName(new_name).is_valid and self.validate_location(new_location):
                if not self.name_in_config(new_name) or new_location != self.config.file_backup_locations[index]:
                    self.tabel.item(selected_item, values=[new_name])
                    self.config.file_backup_names[index] = self.file_backup_name_entry_var.get()
                    self.config.file_backup_locations[index] = self.file_backup_source_entry_var.get()

    def get_current_row_index(self):
        return self.tabel.index(self.tabel.selection())

    def delete_item(self):
        index = self.get_current_row_index()
        selected_item = self.tabel.selection()
        if len(self.config.file_backup_names) != 0:
            self.tabel.delete(selected_item)
            del (self.config.file_backup_names[index])
            del (self.config.file_backup_locations[index])

    def add_item(self):
        # This function runs whenever the "add new option" button is pressed
        # This function add in a new backup option with the settings given by the user
        if self.validate_name(self.file_backup_name_entry_var.get()):
            if self.validate_location(self.file_backup_source_entry_var.get()):
                # If max number isn't reached
                print(len(self.config.file_backup_names))
                self.tabel.insert('', len(self.config.file_backup_names),
                                  values=[str(self.file_backup_name_entry_var.get())])
                self.config.file_backup_names.append(self.file_backup_name_entry_var.get())
                self.config.file_backup_locations.append(self.file_backup_source_entry_var.get())

    def validate_name(self, name):
        if not self.does_name_exists(name) and ValidateName(name).is_valid:
            return True
        return False

    def does_name_exists(self, name):
        if not self.name_in_config(name):
            return False
        Messagebox.show_warning(title="Warning", message="Name already in list!")
        return True

    def name_in_config(self, name):
        return name in self.config.file_backup_names

    def close_pop_up(self):
        self.top_level.grab_release()
        self.top_level.destroy()

    def save_changes(self):
        if self.file_backup_source_entry_var.get() != "" and self.file_backup_name_entry_var.get() != "":
            self.apply_changes_for_option()

        # Update configfile
        UpdateConfigfile("file_backup_names", self.config.file_backup_names)
        UpdateConfigfile("file_backup_locations", self.config.file_backup_locations)
        self.update_page()
        self.close_pop_up()

    @staticmethod
    def validate_location(location):
        # If a name is given
        if location != "":
            return True
        else:
            Messagebox.show_warning(title="Warning", message="You must give a location!")
            return False
