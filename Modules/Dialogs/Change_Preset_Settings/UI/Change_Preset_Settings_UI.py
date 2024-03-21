import tkinter as tk

import ttkbootstrap as ttk


class ChangePresetSettingsUI:
    def __init__(self, master):
        # Create top level
        self.top_level = ttk.Toplevel(master=master, title="Change preset settings")
        self.top_level.minsize(width=600, height=430)
        self.top_level.transient(master)
        self.top_level.grab_set()

        # Create tabel
        column = ["Backup options"]
        self.tabel = ttk.Treeview(master=self.top_level, columns=column, style="secondary", show="headings")
        self.tabel.heading('Backup options', text="Backup options")

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
        locate_icon = tk.PhotoImage(file="Assets/Images/Open_Folder.png")
        self.locate_absolute_source_btn = ttk.Button(master=preset_source_entry_frame, image=locate_icon)
        self.locate_absolute_source_btn.image = locate_icon
        relative_path_icon = tk.PhotoImage(file="Assets/Images/Find_Relative_Path.png")
        self.locate_relative_source_btn = ttk.Button(master=preset_source_entry_frame, image=relative_path_icon)
        self.locate_relative_source_btn.image = relative_path_icon

        # Packing
        preset_source_entry_label.pack(side="left", padx=5)
        preset_source_entry.pack(side="left", fill="x", padx=5, expand=1)
        self.locate_absolute_source_btn.pack(side="left", padx=5)
        self.locate_relative_source_btn.pack(side="left", padx=(0, 5))
        preset_source_entry_frame.pack(fill="x", pady=10)

        # Create preset destination entry widgets
        preset_destination_entry_frame = ttk.Frame(master=main_container)
        preset_destination_label = ttk.Label(master=preset_destination_entry_frame,
                                             text="Save destination location", width=22)
        self.preset_destination_entry_var = tk.StringVar()
        preset_destination_entry = ttk.Entry(master=preset_destination_entry_frame,
                                             textvariable=self.preset_destination_entry_var)
        self.preset_destination_locate_button = ttk.Button(master=preset_destination_entry_frame, text="locate",
                                                           image=locate_icon)
        # Packing
        preset_destination_label.pack(side="left", padx=5)
        preset_destination_entry.pack(side="left", fill="x", padx=5, expand=1)
        self.preset_destination_locate_button.pack(side="left", padx=5)
        preset_destination_entry_frame.pack(fill="x", pady=10)

        path_label = ttk.Label(
            main_container,
            text="You can use [HOME] for getting the path to your home folder. (e.g. C:/Users/username)",
            style="secondary"
        )
        path_label.pack(padx=10, anchor="w")

        # Create bottom frame
        bottom_frame = ttk.LabelFrame(main_container, style="secondary",
                                      text="Change launch application button setting")
        # Create launch application check button widgets
        launch_application_check_button_frame = ttk.Frame(bottom_frame)
        self.launch_application_check_button_var = tk.IntVar()
        self.launch_application_check_button = ttk.Checkbutton(launch_application_check_button_frame,
                                                               text="Should launch application",
                                                               variable=self.launch_application_check_button_var,
                                                               style="info round-togglebutton", )
        self.launch_application_check_button.pack(side="left", padx=5)
        launch_application_check_button_frame.pack(fill="x", pady=10)

        # Create launch application widgets
        launch_application_frame = ttk.Frame(bottom_frame)
        self.launch_application_label = ttk.Label(launch_application_frame, text="Application location:",
                                                  style="secondary")
        self.launch_application_label.pack(side="left", padx=5)
        self.launch_application_entry_var = tk.StringVar()
        self.launch_application_entry = ttk.Entry(launch_application_frame,
                                                  textvariable=self.launch_application_entry_var, style="secondary",
                                                  state="disabled")
        self.launch_application_entry.pack(side="left", padx=5, expand=1, fill="x")
        self.application_locate_button = ttk.Button(master=launch_application_frame, text="locate",
                                                    style="secondary",
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
        self.apply_button = ttk.Button(master=button_frame, text="Apply changes",
                                       style="success")
        self.delete_button = ttk.Button(master=button_frame, text="Delete option",
                                        style="danger")
        self.add_button = ttk.Button(master=button_frame, text="Add new option",
                                     style="info")

        # Packing
        self.apply_button.pack(pady=10, padx=15, side="left")
        self.delete_button.pack(pady=10, padx=15, side="left")
        self.add_button.pack(pady=10, padx=15, side="left")
        button_frame.pack()

        # Bottom buttons
        self.cancel_button = ttk.Button(master=self.top_level, text="Cancel",
                                        command=self.top_level.destroy, style="danger", width=10)
        self.accept_button = ttk.Button(master=self.top_level, text="Accept",
                                        style="success", width=10)
        self.accept_button.pack(padx=15, pady=10, side="right", anchor="s")
        self.cancel_button.pack(pady=10, side="right", anchor="s")
