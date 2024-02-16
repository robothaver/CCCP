from ttkbootstrap.dialogs.dialogs import Messagebox
import os


class GetRelativePath:
    def __init__(self, path):
        self.path = path
        self.results = None

    def get_path(self, start=""):
        if self.path is not None:
            try:
                self.results = os.path.relpath(start=start, path=self.path)
            except ValueError:
                Messagebox.show_error(title="Error", message="Path destination is on a different drive!")
        return self.results
