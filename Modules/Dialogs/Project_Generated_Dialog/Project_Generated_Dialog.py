import os

from Modules.Dialogs.Project_Generated_Dialog.UI.Project_Generated_UI import ProjectGeneratedUI
import ttkbootstrap as ttk


class ProjectGeneratedDialog(ProjectGeneratedUI):
    def __init__(self, master, path_to_file):
        super().__init__(master)
        self.path_to_file = path_to_file

        self.open_in_vs_code_btn.config(command=self.open_in_vs_code)
        self.open_in_explorer_btn.config(command=self.open_in_explorer)
        self.close_button.config(command=self.close_dialog)

        self.top_level.mainloop()

    def open_in_vs_code(self):
        os.system(f'code "{self.path_to_file}"')
        self.close_dialog()

    def open_in_explorer(self):
        os.system(f'start "" "{self.path_to_file}')
        self.close_dialog()

    def close_dialog(self):
        self.top_level.destroy()
        self.top_level.grab_release()
