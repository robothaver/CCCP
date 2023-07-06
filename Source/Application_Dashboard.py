import tkinter as tk
import ttkbootstrap as ttk
from Update_Configfile import UpdateConfigfile
from To_Do_List import ToDoList
from Copy_Network_Settings import CopyNetworkSettings
from Copy_Save_File_To_And_From_Pc import CopySaveFileToAndFromPc
from Break_Pattern import BreakPattern
from Relative_Path_Generator import RelativePathGenerator


class ApplicationDashboard:
    def __init__(self, master):
        UpdateConfigfile("current_page", 3)
        self.master = master
        # Load images
        self.copy_save_file_button_img = tk.PhotoImage(file="Assets/Images/Copy_Save_TAF_Computer_Icon.png")
        self.to_do_list_img = tk.PhotoImage(file="Assets/Images/To_Do_List_Icon.png")
        self.break_pattern_button_img = tk.PhotoImage(file="Assets/Images/Break_Pattern_Icon.png")
        self.copy_network_settings_button_img = tk.PhotoImage(file="Assets/Images/Copy_Network_Settings_Icon.png")
        self.relative_path_generator_button_img = tk.PhotoImage(file="Assets/Images/Relative_Path_Generator_Icon.png")

        # Creating copy save file button
        copy_save_file_button = ttk.Button(master,
                                           text="Copy save file to and from pc",
                                           command=lambda: self.change_page(0),
                                           image=self.copy_save_file_button_img,
                                           compound="left")
        copy_save_file_button.pack(fill="both", padx=30, pady=10)

        # Creating to-do list button
        to_do_list_button = ttk.Button(master,
                                       text="To-do list",
                                       command=lambda: self.change_page(1),
                                       image=self.to_do_list_img,
                                       compound="left")
        to_do_list_button.pack(fill="both", padx=30, pady=10)

        # Creating break pattern button
        break_pattern_button = ttk.Button(master,
                                          text="Break pattern",
                                          command=lambda: self.change_page(2),
                                          image=self.break_pattern_button_img,
                                          compound="left")
        break_pattern_button.pack(fill="both", padx=30, pady=10)

        # Creating copy network settings button
        copy_network_settings_button = ttk.Button(master,
                                                  text="Copy network settings",
                                                  command=lambda: self.change_page(3),
                                                  image=self.copy_network_settings_button_img,
                                                  compound="left")
        copy_network_settings_button.pack(fill="both", padx=30, pady=10)

        # Creating relative path generator button
        relative_path_generator_button = ttk.Button(master,
                                                    text="Relative path generator",
                                                    command=lambda: self.change_page(4),
                                                    image=self.relative_path_generator_button_img,
                                                    compound="left")
        relative_path_generator_button.pack(fill="both", padx=30, pady=10)

    def change_page(self, index):
        # This function clears the middle frame and calls the selected option
        for widget in self.master.winfo_children():
            widget.destroy()
        if index == 0:
            CopySaveFileToAndFromPc(self.master)
        elif index == 1:
            ToDoList(self.master)
        elif index == 2:
            BreakPattern(self.master)
        elif index == 3:
            CopyNetworkSettings(self.master)
        else:
            RelativePathGenerator(self.master)
