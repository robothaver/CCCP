from tkinter import filedialog

from Modules.Utilities.Get_Relative_Path import GetRelativePath


class LocateFile:
    def get_absolute_path(self, mode=0):
        path = self.locate_file("Get absolute path to file", mode)
        return path

    def get_relative_path(self, mode=0):
        path = self.locate_file("Get relative path to file", mode)
        return GetRelativePath(path).get_path()

    @staticmethod
    def locate_file(title, mode):
        if mode == 0:
            path = filedialog.askopenfilename(title=title)
        else:
            path = filedialog.askdirectory(title=title)
        if path == () or path == "":
            return None
        else:
            return path
