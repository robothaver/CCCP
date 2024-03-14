from ttkbootstrap.dialogs import Messagebox
import os


def open_path_in_explorer(path):
    if os.path.exists(path):
        os.system(f'start "" "{path}')
    else:
        Messagebox.show_error(title="Error", message="Path does not exists!")