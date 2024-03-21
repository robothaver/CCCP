import tkinter as tk
import ttkbootstrap as ttk


class ChangeProjectNamesUI:
    def __init__(self, master):
        self.top_level = ttk.Toplevel(title="Change project names")
        self.top_level.minsize(width=600, height=360)
        self.top_level.transient(master)
        self.top_level.grab_set()

        self.main_container = ttk.Frame(master=self.top_level)

        # Create tabel
        column = ["Project names"]
        self.tabel = ttk.Treeview(master=self.main_container, columns=column, style="secondary", show="headings")
        self.tabel.heading('Project names', text="Project names")
        self.tabel.pack(padx=10, pady=10, fill="both")

        # Create location entry widgets
        location_entry_frame = ttk.Frame(self.main_container)
        location_entry_label = ttk.Label(location_entry_frame, text="Project name", style="info", )
        self.name_entry_var = tk.StringVar()
        location_entry = ttk.Entry(location_entry_frame, textvariable=self.name_entry_var)
        locate_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")
        self.locate_absolute_path_btn = ttk.Button(master=location_entry_frame, image=locate_icon)
        self.locate_absolute_path_btn.image = locate_icon
        relative_path_icon = tk.PhotoImage(file="Assets/Images/Find_Relative_Path.png")
        self.locate_relative_path_btn = ttk.Button(master=location_entry_frame, image=relative_path_icon)
        self.locate_relative_path_btn.image = relative_path_icon
        # Packing
        location_entry_label.pack(side="left", padx=5, pady=5)
        location_entry.pack(side="left", fill="x", expand=1, padx=5)
        self.locate_absolute_path_btn.pack(side="left", padx=5)
        self.locate_relative_path_btn.pack(side="left", padx=(0, 5))
        location_entry_frame.pack(fill="x", padx=5)

        # Create buttons
        button_frame = ttk.LabelFrame(self.main_container, text="Change project name", style="info")
        # Create delete button
        self.delete_button = ttk.Button(master=button_frame, text="Remove name", style="warning", width=15)
        self.delete_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Create add button
        self.add_button = ttk.Button(master=button_frame, text="Add name", style="info", width=15)
        self.add_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Create apply changes
        self.apply_changes_button = ttk.Button(master=button_frame, text="Apply changes", style="success", width=15)
        self.apply_changes_button.pack(padx=10, pady=5, side="left", fill="x", expand=1)

        # Packing
        button_frame.pack(fill="x", padx=10, pady=10)

        # Create bottom frame
        self.bottom_frame = ttk.Frame(master=self.main_container)
        # Create buttons
        self.accept_button = ttk.Button(master=self.bottom_frame, text="Accept", style="success", width=10)
        self.accept_button.pack(padx=10, pady=10, side="right")
        self.cancel_button = ttk.Button(master=self.bottom_frame, text="Cancel", style="danger", width=10)
        self.cancel_button.pack(pady=10, side="right")
        self.bottom_frame.pack(fill="x", side="bottom")

        self.main_container.pack(fill="both", expand=True)
