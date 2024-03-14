import ttkbootstrap as ttk
import tkinter as tk


class ProjectGeneratedUI:
    def __init__(self, master):
        self.top_level = ttk.Toplevel(master=master, title="Project generated")
        self.top_level.transient(master)
        self.top_level.grab_set()
        self.top_level.minsize(width=600, height=400)

        title_label = ttk.Label(master=self.top_level, text="Project generated", font=('Calibri', '22', 'bold'), style="primary")
        title_label.pack(padx=15, pady=(15, 0))

        main_container = ttk.Frame(self.top_level)

        main_container.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=1)

        self.vs_code_icon = tk.PhotoImage(file="Assets/Images/VSCode_Icon.png")
        self.open_in_vs_code_btn = ttk.Button(main_container, text="Open in VS Code",
                                         image=self.vs_code_icon, compound="top", style="secondary")
        self.open_in_vs_code_btn.grid(row=0, column=0, sticky="nsew", padx=15, pady=15, ipadx=15, ipady=15)

        self.file_explorer_icon = tk.PhotoImage(file="Assets/Images/File_Explorer_Icon.png")
        self.open_in_explorer_btn = ttk.Button(main_container, text="Open in file explorer",
                                          image=self.file_explorer_icon, compound="top", style="secondary")
        self.open_in_explorer_btn.grid(row=0, column=1, sticky="nsew", padx=15, pady=15, ipadx=15, ipady=15)

        self.close_icon = tk.PhotoImage(file="Assets/Images/Close_Icon.png")
        self.close_button = ttk.Button(main_container, text="Close", image=self.close_icon, compound="left")
        self.close_button.grid(row=1, columnspan=2, sticky="we", padx=15, pady=15)

        main_container.pack(fill="both", expand=True)
