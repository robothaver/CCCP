import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

from Assets import Assets


class SettingsUI:
    def __init__(self, master):
        # Create clock settings

        self.master_container = ttk.Frame(master)

        self.settings_container = ScrolledFrame(self.master_container)
        self.about_container = ttk.Frame(self.master_container)

        self.clock_settings_frame = ttk.LabelFrame(master=self.settings_container,
                                                   text="Change clock settings",
                                                   style="warning")

        self.selected = tk.StringVar()
        self.clock_settings_45_10 = ttk.Radiobutton(master=self.clock_settings_frame, text="45min 10min",
                                                    value="45_10",
                                                    variable=self.selected, style="warning-toolbutton")
        self.clock_settings_40_5 = ttk.Radiobutton(master=self.clock_settings_frame, text="40min 5min",
                                                   value="40_5",
                                                   variable=self.selected, style="warning-toolbutton")
        self.clock_settings_35_10 = ttk.Radiobutton(master=self.clock_settings_frame, text="35min 10min",
                                                    value="35_10",
                                                    variable=self.selected, style="warning-toolbutton")
        self.clock_settings_35_5 = ttk.Radiobutton(master=self.clock_settings_frame, text="35min 5min",
                                                   value="35_5",
                                                   variable=self.selected, style="warning-toolbutton")
        self.clock_settings_45_10.pack(side="left", padx=10, pady=15, fill="x", expand=True)
        self.clock_settings_40_5.pack(side="left", padx=10, pady=15, fill="x", expand=True)
        self.clock_settings_35_10.pack(side="left", padx=10, pady=15, fill="x", expand=True)
        self.clock_settings_35_5.pack(side="left", padx=10, pady=15, fill="x", expand=True)
        self.clock_settings_frame.pack(pady=15, fill="x", padx=20)

        # Create general settings
        general_settings = ttk.LabelFrame(self.settings_container, text="General settings", style="info")

        # Create starting page setting
        starting_page_frame = ttk.Frame(general_settings)
        self.starting_page_icon = tk.PhotoImage(file="Assets/Images/Starting_Page_Icon.png")
        starting_page_label = ttk.Label(master=starting_page_frame, text="Starting page", image=self.starting_page_icon,
                                        compound="left")
        self.page_var = tk.StringVar()
        self.default_page_changer = ttk.OptionMenu(
            starting_page_frame,
            self.page_var,
            "",
            *Assets.page_names, style="info outline",
        )

        starting_page_label.pack(side="left", pady=10)
        self.default_page_changer.pack(side="right", pady=10)
        starting_page_frame.pack(fill="x", padx=10)

        # Create "end of lesson reminder" option
        end_of_lesson_reminder_frame = ttk.Frame(general_settings)
        self.end_of_lesson_reminder_icon = tk.PhotoImage(file="Assets/Images/End_Of_Lesson_Reminder_Icon.png")
        end_of_lesson_reminder_label = ttk.Label(end_of_lesson_reminder_frame,
                                                 text="End of lesson reminder",
                                                 image=self.end_of_lesson_reminder_icon,
                                                 compound="left")

        self.end_of_lesson_reminder_button_var = tk.IntVar()
        self.end_of_lesson_reminder_button = ttk.Checkbutton(
            master=end_of_lesson_reminder_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.end_of_lesson_reminder_button_var)

        end_of_lesson_reminder_label.pack(side="left", padx=10, pady=10)
        self.end_of_lesson_reminder_button.pack(pady=10, side="right", padx=5)
        end_of_lesson_reminder_frame.pack(fill="x")

        # Create enable custom themes option
        custom_themes_frame = ttk.Frame(general_settings)
        self.custom_themes_icon = tk.PhotoImage(file="Assets/Images/Custom_Themes_Icon.png")
        custom_themes_label = ttk.Label(custom_themes_frame,
                                        text="Enable custom themes",
                                        image=self.custom_themes_icon,
                                        compound="left")

        self.custom_themes_button_var = tk.IntVar()
        self.custom_themes_button = ttk.Checkbutton(
            master=custom_themes_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.custom_themes_button_var)

        custom_themes_label.pack(side="left", padx=10, pady=10)
        self.custom_themes_button.pack(pady=10, side="right", padx=5)
        custom_themes_frame.pack(fill="x")

        # Create theme selector
        theme_frame = ttk.Frame(general_settings)
        self.theme_icon = tk.PhotoImage(file="Assets/Images/Themes_Icon.png")
        theme_label = ttk.Label(master=theme_frame, text="Change theme", image=self.theme_icon,
                                compound="left")

        self.theme_var = tk.StringVar()
        self.theme_changer = ttk.OptionMenu(
            theme_frame,
            self.theme_var,
            "",
            style="info outline")

        theme_label.pack(side="left", padx=10)
        self.theme_changer.pack(side="right", padx=10, pady=10)
        theme_frame.pack(fill="x")

        # Create browser selector
        browser_frame = ttk.Frame(general_settings)
        self.browser_icon = tk.PhotoImage(file="Assets/Images/Web_Browser_Icon.png")
        browser_label = ttk.Label(master=general_settings, text="Change browser", image=self.browser_icon,
                                  compound="left")
        self.browser_var = tk.StringVar()
        self.browser_changer = ttk.OptionMenu(
            browser_frame,
            self.browser_var,
            "",
            *Assets.browsers,
            style="info outline",
        )

        browser_label.pack(side="left", padx=10)
        self.browser_changer.pack(side="right", padx=10, pady=10)
        browser_frame.pack(fill="x")

        general_settings.pack(fill="x", padx=20)

        # Create top panel settings
        top_panel_settings_frame = ttk.LabelFrame(self.settings_container, text="Top panel settings", style="success")

        # Create top theme selector setting
        top_theme_selector_frame = ttk.Frame(top_panel_settings_frame)
        self.top_theme_selector_icon = tk.PhotoImage(file="Assets/Images/Top_Theme_Selector_Icon.png")
        top_theme_selector_label = ttk.Label(top_theme_selector_frame,
                                             text="Top theme selector",
                                             image=self.top_theme_selector_icon,
                                             compound="left")

        self.top_theme_selector_var = tk.IntVar()
        self.top_theme_selector_button = ttk.Checkbutton(
            master=top_theme_selector_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.top_theme_selector_var)

        top_theme_selector_label.pack(side="left", padx=10)
        self.top_theme_selector_button.pack(pady=10, side="right", padx=5)
        top_theme_selector_frame.pack(fill="x", pady=10)

        self.about_icon = tk.PhotoImage(file="Assets/Images/About_Icon.png")
        top_panel_settings_frame.pack(fill="x", padx=20, pady=10)

        # Create "top end of lesson timer" setting
        primary_notifier_frame = ttk.Frame(top_panel_settings_frame)
        self.primary_notifier_icon = tk.PhotoImage(file="Assets/Images/Top_End_Of_Lesson_Timer.png")
        top_end_of_lesson_timer_label = ttk.Label(primary_notifier_frame,
                                                  text="Top end of lesson timer",
                                                  image=self.primary_notifier_icon,
                                                  compound="left")

        self.primary_notifier_var = tk.IntVar()
        self.primary_notifier = ttk.Checkbutton(
            master=primary_notifier_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.primary_notifier_var)

        top_end_of_lesson_timer_label.pack(side="left", padx=10)
        self.primary_notifier.pack(pady=10, side="right", padx=5)
        primary_notifier_frame.pack(fill="x", pady=10)

        # Create "top lesson number" setting
        secondary_notifier_frame = ttk.Frame(top_panel_settings_frame)
        self.secondary_notifier_icon = tk.PhotoImage(file="Assets/Images/Top_Lesson_Number.png")
        top_lesson_number_label = ttk.Label(secondary_notifier_frame,
                                            text="Top lesson number",
                                            image=self.secondary_notifier_icon,
                                            compound="left"
                                            )

        self.secondary_notifier_var = tk.IntVar()
        self.secondary_notifier = ttk.Checkbutton(
            master=secondary_notifier_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.secondary_notifier_var
        )

        top_lesson_number_label.pack(side="left", padx=10)
        self.secondary_notifier.pack(pady=10, side="right", padx=5)
        secondary_notifier_frame.pack(fill="x", pady=10)

        # Create progress_bar setting
        progress_bar = ttk.Frame(top_panel_settings_frame)
        self.progress_bar_icon = tk.PhotoImage(file="Assets/Images/Progress_Bar_Icon.png")
        progress_bar_label = ttk.Label(progress_bar,
                                 text="Progress bar",
                                 image=self.progress_bar_icon,
                                 compound="left"
                                 )

        self.progress_bar_var = tk.IntVar()
        self.progress_bar_button = ttk.Checkbutton(
            master=progress_bar,
            style="info Roundtoggle.Toolbutton",
            variable=self.progress_bar_var
        )

        progress_bar_label.pack(side="left", padx=10)
        self.progress_bar_button.pack(pady=10, side="right", padx=5)
        progress_bar.pack(fill="x", pady=10)

        top_panel_settings_frame.pack(fill="x", padx=20, pady=10)

        self.about_icon = tk.PhotoImage(file="Assets/Images/About_Icon.png")
        self.about_button = ttk.Button(self.settings_container, text="About", image=self.about_icon, compound="left")
        self.about_button.pack(fill="x", padx=20, pady=20, side="bottom")
