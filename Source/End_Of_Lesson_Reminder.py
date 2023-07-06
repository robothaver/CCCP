import ttkbootstrap as ttk
import tkinter as tk


class EndOfLessonReminder:
    def __init__(self, message):
        # Create top level
        self.top_level = ttk.Toplevel()
        self.top_level.grab_set()
        self.top_level.lift()
        self.top_level.title("End of lesson reminder")
        self.top_level.resizable(False,False) #Blocks resize
        self.top_level.attributes('-topmost', 'true')
        # Create widgets
        top_frame = ttk.Frame(self.top_level)
        # Create warning icon
        self.warning_icon_img = tk.PhotoImage(file="Assets/Images/Warning_Icon.png")
        warning_icon = ttk.Label(top_frame, image=self.warning_icon_img)
        warning_icon.pack(side="left", padx=10, pady=10)
        # Create message label
        message_label = ttk.Label(top_frame, text=message, style="warning")
        message_label.pack(side="right", pady=10, padx=15)
        top_frame.pack()
        separator = ttk.Separator(self.top_level)
        separator.pack(pady=5, fill="x")
        accept_button = ttk.Button(self.top_level, text="Accept", command=self.close_pop_up)
        accept_button.pack(padx=10, pady=10, anchor="e")

    def close_pop_up(self):
        self.top_level.destroy()
