from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Settings.Sub_Pages.About.About import About
from Modules.Configfile.Config import Configfile
from Modules.Pages.Settings.UI.Settings_UI import SettingsUI
from Assets import Assets
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame


class Settings(SettingsUI):
    def __init__(self, master, top_frame, style):
        # Define variables
        self.config = Configfile()
        self.style = style
        self.master = master
        self.top_frame = top_frame

        self.settings_page = ScrolledFrame(master)
        self.secondary_container = ttk.Frame(master)
        # Initialize UI
        super().__init__(self.settings_page, self.config)

        self.about_page = About(self.secondary_container, self.show_settings_page)

        self.clock_settings_40_5.config(command=self.change_clock_settings)
        self.clock_settings_45_10.config(command=self.change_clock_settings)
        self.clock_settings_35_5.config(command=self.change_clock_settings)
        self.clock_settings_35_10.config(command=self.change_clock_settings)

        self.page_var.trace("w", self.change_starting_page)

        self.theme_var.trace("w", self.change_theme)

        self.browser_var.trace("w", self.change_browser)

        self.end_of_lesson_reminder_button.config(command=self.update_end_of_lesson_reminder)

        self.top_theme_selector_button.config(command=self.change_top_theme_selector_settings)

        self.top_end_of_lesson_timer_button.config(command=self.change_top_end_of_lesson_timer_settings)

        self.top_lesson_number_button.config(command=self.top_lesson_number_settings)

        self.about_button.config(command=self.change_page_to_about)

    def update_end_of_lesson_reminder(self):
        UpdateConfigfile("end_of_lesson_reminder", bool(self.end_of_lesson_reminder_button_var.get()))

    def change_starting_page(self, *args):
        UpdateConfigfile("starting_page", Assets.page_names.index(self.page_var.get()))

    def change_clock_settings(self):
        UpdateConfigfile("clock_mode", self.selected.get())

    def change_top_theme_selector_settings(self):
        UpdateConfigfile("top_theme_selector", self.top_theme_selector_var.get())

    def top_lesson_number_settings(self):
        UpdateConfigfile("top_lesson_number", self.top_lesson_number_var.get())

    def change_top_end_of_lesson_timer_settings(self):
        UpdateConfigfile("top_end_of_lesson_timer", self.top_end_of_lesson_timer_var.get())

    def change_theme(self, *args):
        theme = self.theme_var.get()
        UpdateConfigfile("theme", theme)
        self.style.theme_use(theme)

    def change_page_to_about(self):
        self.settings_page.pack_forget()
        self.secondary_container.pack(fill="both", expand=True)
        self.about_page.change_page(0)

    def show_settings_page(self):
        self.secondary_container.pack_forget()
        self.settings_page.pack(fill="both", expand=True)

    def change_browser(self, *args):
        UpdateConfigfile("browser", self.browser_var.get())
