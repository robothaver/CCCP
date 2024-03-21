import tkinter as tk
import ttkbootstrap as ttk


class ChangeBackupLocationsUI:
    def __init__(self, master):
        # Create_Top_Level
        self.top_level = ttk.Toplevel(title="Change the settings for backup options")
        self.top_level.minsize(width=600, height=430)
        self.top_level.transient(master)
        self.top_level.grab_set()

        # Create_tabel
        column = ["Backup options"]
        self.tabel = ttk.Treeview(master=self.top_level, columns=column, style="secondary", show="headings")
        self.tabel.heading('Backup options', text="Backup options")
        self.tabel.pack(padx=10, pady=10, fill="both", expand=True)

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

        locate_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")
        self.locate_absolute_path_btn = ttk.Button(master=file_backup_source_entry_frame, image=locate_icon)
        self.locate_absolute_path_btn.image = locate_icon
        relative_path_icon = tk.PhotoImage(file="Assets/Images/Find_Relative_Path.png")
        self.locate_relative_path_btn = ttk.Button(master=file_backup_source_entry_frame, image=relative_path_icon)
        self.locate_relative_path_btn.image = relative_path_icon

        # Packing
        file_backup_name_entry_frame.pack(fill="x")
        file_backup_name_label.pack(side="left", padx=15, pady=10)
        file_backup_name_entry.pack(side="left", padx=15, pady=10, fill="x", expand=True)
        file_backup_source_entry_frame.pack(pady=1, fill="x")
        file_backup_source_label.pack(side="left", padx=15, pady=10)
        file_backup_location_entry.pack(side="left", padx=(15, 0), pady=10, fill="x", expand=True)
        self.locate_absolute_path_btn.pack(side="left", padx=(10, 5))
        self.locate_relative_path_btn.pack(side="left", padx=(0, 15))
        selected_item_frame.pack(fill="x", padx=15)

        path_label = ttk.Label(selected_item_frame, text="You can use [HOME] for getting the path to "
                                                         "your home folder. (e.g. C:/Users/username)",
                               style="secondary")
        path_label.pack(padx=15, anchor="w")

        # Entry buttons
        button_frame = ttk.Frame(master=selected_item_frame)
        self.apply_button = ttk.Button(master=button_frame, text="Apply changes", style="success")
        self.delete_button = ttk.Button(master=button_frame, text="Delete option", style="danger")
        self.add_button = ttk.Button(master=button_frame, text="Add new option", style="info")

        # Packing
        self.apply_button.pack(pady=10, padx=15, side="left")
        self.delete_button.pack(pady=10, padx=15, side="left")
        self.add_button.pack(pady=10, padx=15, side="left")
        button_frame.pack()

        # Bottom buttons
        self.cancel_button = ttk.Button(master=self.top_level, text="Cancel", style="danger", width=10)
        self.accept_button = ttk.Button(master=self.top_level, text="Accept", style="success", width=10)
        self.accept_button.pack(padx=15, pady=10, side="right", anchor="s")
        self.cancel_button.pack(pady=10, side="right", anchor="s")
