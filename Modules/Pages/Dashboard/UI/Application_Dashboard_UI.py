import tkinter as tk

import ttkbootstrap as ttk


class ApplicationDashboardUI:
    def __init__(self, master):
        self.secondary_container = ttk.Frame(master)
        self.main_container = ttk.Frame(master)

        # Load images
        copy_save_file_button_img = tk.PhotoImage(file="Assets/Images/Copy_Save_TAF_Computer_Icon.png")
        to_do_list_img = tk.PhotoImage(file="Assets/Images/To_Do_List_Icon.png")
        break_pattern_button_img = tk.PhotoImage(file="Assets/Images/Break_Pattern_Icon.png")
        copy_network_settings_button_img = tk.PhotoImage(file="Assets/Images/Copy_Network_Settings_Icon.png")
        relative_path_generator_button_img = tk.PhotoImage(file="Assets/Images/Relative_Path_Generator_Icon.png")

        # Creating copy save file button
        self.copy_save_file_button = ttk.Button(self.main_container,
                                                text="Copy save file to and from pc",
                                                image=copy_save_file_button_img,
                                                compound="left")
        self.copy_save_file_button.pack(fill="both", padx=30, pady=10)
        self.copy_save_file_button.image = copy_save_file_button_img

        # Creating to-do list button
        self.to_do_list_button = ttk.Button(self.main_container,
                                            text="To-do list",
                                            image=to_do_list_img,
                                            compound="left")
        self.to_do_list_button.pack(fill="both", padx=30, pady=10)
        self.to_do_list_button.image = to_do_list_img

        # Creating break pattern button
        self.break_pattern_button = ttk.Button(self.main_container,
                                               text="Break pattern",
                                               image=break_pattern_button_img,
                                               compound="left")
        self.break_pattern_button.pack(fill="both", padx=30, pady=10)
        self.break_pattern_button.image = break_pattern_button_img

        # Creating copy network settings button
        self.copy_network_settings_button = ttk.Button(self.main_container,
                                                       text="Copy network settings",
                                                       image=copy_network_settings_button_img,
                                                       compound="left")
        self.copy_network_settings_button.pack(fill="both", padx=30, pady=10)
        self.copy_network_settings_button.image = copy_network_settings_button_img

        # Creating relative path generator button
        self.relative_path_generator_button = ttk.Button(self.main_container,
                                                         text="Relative path generator",
                                                         image=relative_path_generator_button_img,
                                                         compound="left")
        self.relative_path_generator_button.pack(fill="both", padx=30, pady=10)
        self.relative_path_generator_button.image = relative_path_generator_button_img

        self.main_container.pack(fill="both", expand=True)
