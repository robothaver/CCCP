import tkinter as tk
import ttkbootstrap as ttk


class TodoWidgetUI:
    def __init__(self, master, title):
        # Icons
        self.widget_open_icon = tk.PhotoImage(file="Assets/Images/icons8_double_right_24px.png")
        self.widget_closed_icon = tk.PhotoImage(file="Assets/Images/icons8_double_up_24px.png")
        self.check_button_selected_img = tk.PhotoImage(file="Assets/Images/Check_Button_Selected_Icon.png")
        self.check_button_deselected_img = tk.PhotoImage(file="Assets/Images/Check_Button_Deselected_Icon.png")
        self.delete_button_icon = tk.PhotoImage(file="Assets/Images/Delete_Button_Icon.png")
        self.edit_button_icon = tk.PhotoImage(file="Assets/Images/Edit_Button_Icon.png")

        self.description_label = None
        self.children_container = None

        # Creating main container
        self.main_container = ttk.Frame(master)
        self.main_container.pack(fill="x", padx=20, pady=10)
        self.title_container = ttk.Frame(self.main_container, bootstyle="secondary")
        self.container_title_label = ttk.Label(self.title_container, text=title,
                                               font=('Arial', '14', 'bold'), style="secondary inverse")
        self.container_title_label.pack(padx=5, side="left")

        # Delete button
        self.delete_button = ttk.Button(self.title_container, image=self.delete_button_icon, style="danger")
        self.delete_button.pack(side="right")

        # Creating check button
        self.check_button_var = tk.IntVar(value=0)
        self.check_button = ttk.Checkbutton(self.title_container, image=self.check_button_deselected_img,
                                            variable=self.check_button_var, style="success.Toolbutton")
        self.check_button.pack(side="right")

        self.edit_button = ttk.Button(self.title_container, image=self.edit_button_icon, style="secondary")
        self.edit_button.pack(side="right")

        # Creating open button
        self.open_button = ttk.Button(self.title_container, image=self.widget_closed_icon, style="secondary")
        self.open_button.pack(side="right", padx=1)
        self.title_container.pack(fill="x")
