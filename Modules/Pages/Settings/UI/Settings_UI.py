import tkinter as tk
import ttkbootstrap as ttk
from Assets import Assets


class SettingsUI:
    def __init__(self, master, config):
        # Create clock settings
        self.clock_settings_frame = ttk.LabelFrame(master=master, text="Change clock settings", style="warning")
        self.selected = tk.StringVar(value=config.clock_mode)
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
        general_settings = ttk.LabelFrame(master, text="General settings", style="info")

        # Create starting page setting
        starting_page_frame = ttk.Frame(general_settings)
        self.starting_page_icon = tk.PhotoImage(file="Assets/Images/Starting_Page_Icon.png")
        starting_page_label = ttk.Label(master=starting_page_frame, text="Starting page", image=self.starting_page_icon,
                                        compound="left")
        self.page_var = tk.StringVar()
        self.default_page_changer = ttk.OptionMenu(
            starting_page_frame,
            self.page_var,
            Assets.page_names[config.starting_page],
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

        self.end_of_lesson_reminder_button_var = tk.IntVar(value=config.end_of_lesson_reminder)
        self.end_of_lesson_reminder_button = ttk.Checkbutton(
            master=end_of_lesson_reminder_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.end_of_lesson_reminder_button_var)

        end_of_lesson_reminder_label.pack(side="left", padx=10, pady=10)
        self.end_of_lesson_reminder_button.pack(pady=10, side="right", padx=5)
        end_of_lesson_reminder_frame.pack(fill="x")

        # Create theme selector
        theme_frame = ttk.Frame(general_settings)
        self.theme_icon = tk.PhotoImage(file="Assets/Images/Theme_Icon.png")
        theme_label = ttk.Label(master=theme_frame, text="Change theme", image=self.theme_icon,
                                compound="left")
        self.current_theme = config.theme
        self.theme_var = tk.StringVar()
        self.theme_changer = ttk.OptionMenu(
            theme_frame,
            self.theme_var,
            self.current_theme,
            *Assets.theme_names,
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
            config.browser,
            *Assets.browsers,
            style="info outline",
        )

        browser_label.pack(side="left", padx=10)
        self.browser_changer.pack(side="right", padx=10, pady=10)
        browser_frame.pack(fill="x")

        general_settings.pack(fill="x", padx=20)

        # Create top panel settings
        top_panel_settings_frame = ttk.LabelFrame(master, text="Top panel settings", style="success")

        # Create top theme selector setting
        top_theme_selector_frame = ttk.Frame(top_panel_settings_frame)
        self.top_theme_selector_icon = tk.PhotoImage(file="Assets/Images/Top_Theme_Selector_Icon.png")
        top_theme_selector_label = ttk.Label(top_theme_selector_frame,
                                             text="Top theme selector",
                                             image=self.top_theme_selector_icon,
                                             compound="left")

        self.top_theme_selector_var = tk.IntVar(value=config.top_theme_selector)
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
        top_end_of_lesson_timer_frame = ttk.Frame(top_panel_settings_frame)
        self.top_end_of_lesson_timer_icon = tk.PhotoImage(file="Assets/Images/Top_End_Of_Lesson_Timer.png")
        top_end_of_lesson_timer_label = ttk.Label(top_end_of_lesson_timer_frame,
                                                  text="Top end of lesson timer",
                                                  image=self.top_end_of_lesson_timer_icon,
                                                  compound="left")

        self.top_end_of_lesson_timer_var = tk.IntVar(value=config.top_end_of_lesson_timer)
        self.top_end_of_lesson_timer_button = ttk.Checkbutton(
            master=top_end_of_lesson_timer_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.top_end_of_lesson_timer_var)

        top_end_of_lesson_timer_label.pack(side="left", padx=10)
        self.top_end_of_lesson_timer_button.pack(pady=10, side="right", padx=5)
        top_end_of_lesson_timer_frame.pack(fill="x", pady=10)

        # Create "top lesson number" setting
        top_lesson_number_frame = ttk.Frame(top_panel_settings_frame)
        self.top_lesson_number_icon = tk.PhotoImage(file="Assets/Images/Top_Lesson_Number.png")
        top_lesson_number_label = ttk.Label(top_lesson_number_frame,
                                            text="Top lesson number",
                                            image=self.top_lesson_number_icon,
                                            compound="left"
                                            )

        self.top_lesson_number_var = tk.IntVar(value=config.top_lesson_number)
        self.top_lesson_number_button = ttk.Checkbutton(
            master=top_lesson_number_frame,
            style="info Roundtoggle.Toolbutton",
            variable=self.top_lesson_number_var
        )

        top_lesson_number_label.pack(side="left", padx=10)
        self.top_lesson_number_button.pack(pady=10, side="right", padx=5)
        top_lesson_number_frame.pack(fill="x", pady=10)

        top_panel_settings_frame.pack(fill="x", padx=20, pady=10)

        self.about_icon = tk.PhotoImage(file="Assets/Images/About_Icon.png")
        self.about_button = ttk.Button(master, text="About", image=self.about_icon, compound="left")
        self.about_button.pack(fill="x", padx=20, pady=20, side="bottom")
