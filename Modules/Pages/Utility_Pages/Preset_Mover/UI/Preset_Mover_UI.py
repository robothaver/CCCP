import tkinter as tk

import ttkbootstrap as ttk


class PresetMoverUI:
    def __init__(self, master):
        self.master_container = ttk.Frame(master)
        back_frame = ttk.Frame(self.master_container)
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        self.back_button = ttk.Button(back_frame, text="Back",
                                      image=self.back_button_icon, compound="left")
        self.back_button.pack(side="left", padx=10, pady=5)
        back_frame.pack(fill="x")

        # Create preset selector
        self.preset_selector_var = tk.StringVar()
        self.preset_selector = ttk.OptionMenu(self.master_container, self.preset_selector_var, "Select preset",
                                         style="info outline")
        self.preset_selector.pack(pady=10)

        # Load icons
        self.copy_to_computer_icon = tk.PhotoImage(file="Assets/Images/Copy_Save_To_Computer_Icon.png")
        self.copy_from_computer_icon = tk.PhotoImage(file="Assets/Images/Copy_Save_From_Computer_Icon.png")

        # Create button frame
        button_frame = ttk.Frame(self.master_container)
        button_frame.rowconfigure(0, weight=1)

        # Configure button frame row and column settings
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # Create copy to computer button
        self.copy_to_computer_button = ttk.Button(master=button_frame, text="Copy save to computer",
                                                  image=self.copy_to_computer_icon,
                                                  compound="top", style="secondary")
        self.copy_to_computer_button.grid(row=0, column=0, padx=25, pady=0, sticky="nsew")

        # Create copy from computer button
        self.copy_from_computer_button = ttk.Button(master=button_frame, text="Copy save from computer",
                                                    image=self.copy_from_computer_icon,
                                                    compound="top", style="secondary")
        self.copy_from_computer_button.grid(row=0, column=1, padx=25, pady=0, sticky="nsew")

        # Pack button frame
        button_frame.pack(pady=15, padx=15, fill="both", expand=True)

        # Create change preset settings button
        self.change_preset_settings = ttk.Button(master=self.master_container, text="Change preset settings", width=30)
        self.change_preset_settings.pack(side="bottom", pady=(10, 40))

        # Create launch application button
        self.launch_application_button = ttk.Button(master=self.master_container, text="Launch application",
                                                    width=30, style="success", state="disabled")
        self.launch_application_button.pack(side="bottom", pady=10)
