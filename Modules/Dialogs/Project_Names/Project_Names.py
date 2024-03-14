from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile

from Modules.Dialogs.Project_Names.UI.Project_Names_UI import ProjectNamesUI
from Modules.Utilities.Locate_File import LocateFile
from Modules.Utilities.Validate_Name import ValidateName


class ProjectNames(ProjectNamesUI):
    def __init__(self, master):
        super().__init__(master)
        # Define variables
        self.config = Configfile()

        # Load datas to tabel
        for i, location in enumerate(self.config.project_names):
            self.tabel.insert('', i, values=[location])

        self.tabel.bind('<<TreeviewSelect>>', self.update_entries_with_selected_item)

        self.locate_absolute_path_btn.config(command=self.locate_absolute_path)
        self.locate_relative_path_btn.config(command=self.locate_relative_path)

        self.apply_changes_button.config(command=self.apply_changes)
        self.delete_button.config(command=self.remove_selected)
        self.add_button.config(command=self.add_item)

        self.cancel_button.config(command=self.close_pop_up)
        self.accept_button.config(command=self.save_changes)

        self.top_level.mainloop()

    def locate_absolute_path(self):
        name = LocateFile().get_absolute_path(1)
        if name is not None:
            self.name_entry_var.set(name)

    def locate_relative_path(self):
        name = LocateFile().get_relative_path(1)
        if name is not None:
            self.name_entry_var.set(name)

    def update_entries_with_selected_item(self, event):
        selected_item = self.tabel.selection()
        try:
            self.name_entry_var.set(self.tabel.item(selected_item)['values'][0])
        except IndexError:
            pass

    def remove_selected(self):
        selected_item = self.tabel.selection()
        if self.tabel.item(selected_item)["values"] != "":
            del self.config.project_names[self.tabel.index(selected_item)]
            self.tabel.delete(selected_item)

    def apply_changes(self):
        selected_item = self.tabel.selection()
        index = self.tabel.index(self.tabel.selection())
        new_name = self.name_entry_var.get()
        if new_name not in self.config.project_names and ValidateName(new_name).is_valid:
            self.tabel.item(selected_item, values=[new_name])
            try:
                self.config.project_names[index] = new_name
            except IndexError:
                pass

    def add_item(self):
        new_name = self.name_entry_var.get()
        if new_name != "" and new_name not in self.config.project_names:
            if ValidateName(new_name).is_valid:
                self.config.project_names.append(new_name)
                self.tabel.insert('', len(self.config.project_names), values=[new_name])

    def save_changes(self):
        UpdateConfigfile("project_names", self.config.project_names)
        self.close_pop_up()

    def close_pop_up(self):
        self.top_level.destroy()
        self.top_level.grab_release()
