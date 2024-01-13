from Assets import Assets
from Modules.Configfile.Config import Configfile
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Settings.Sub_Pages.About.About import About
from Modules.Pages.Settings.UI.Settings_UI import SettingsUI


class Settings(SettingsUI):
    def __init__(self, master, style_controller, refresh_top_panel):
        super().__init__(master)
        # Define variables
        self.config = Configfile()
        self.style_controller = style_controller
        self.refresh_top_panel = refresh_top_panel
        self.about_page = About(self.about_container, self.show_settings_page, self.config)

        self.show_settings_page()
        self.refresh_page()

        # Connecting buttons to functions
        self.clock_settings_40_5.config(command=self.change_clock_settings)
        self.clock_settings_45_10.config(command=self.change_clock_settings)
        self.clock_settings_35_5.config(command=self.change_clock_settings)
        self.clock_settings_35_10.config(command=self.change_clock_settings)

        self.page_var.trace("w", self.change_starting_page)
        self.theme_var.trace("w", self.change_theme)
        self.custom_themes_button_var.trace("w", self.change_custom_themes)
        self.browser_var.trace("w", self.change_browser)
        self.end_of_lesson_reminder_button.config(command=self.update_end_of_lesson_reminder)

        self.top_theme_selector_button.config(command=self.change_top_theme_selector_settings)

        self.primary_notifier.config(command=self.change_top_end_of_lesson_timer_settings)

        self.secondary_notifier.config(command=self.top_lesson_number_settings)

        self.about_button.config(command=self.change_page_to_about)

    def refresh_page(self):
        self.config = Configfile()
        self.selected.set(self.config.clock_mode)
        self.page_var.set(Assets.page_names[self.config.starting_page])
        self.theme_var.set(self.config.theme)
        self.custom_themes_button_var.set(self.config.custom_themes)
        self.browser_var.set(self.config.browser)
        self.end_of_lesson_reminder_button_var.set(self.config.end_of_lesson_reminder)
        self.primary_notifier_var.set(self.config.enable_primary_notifier)
        self.secondary_notifier_var.set(self.config.enable_secondary_notifier)
        self.top_theme_selector_var.set(self.config.enable_top_theme_selector)
        self.theme_changer.set_menu(None, *self.style_controller.themes)

    def change_custom_themes(self, *args):
        custom_themes = bool(self.custom_themes_button_var.get())
        UpdateConfigfile("custom_themes", custom_themes)
        self.style_controller.load_themes(custom_themes)
        self.refresh_page()
        self.refresh_top_panel()

    def change_theme(self, *args):
        theme = self.theme_var.get()
        UpdateConfigfile("theme", theme)
        self.style_controller.set_current_theme(theme)

    def change_starting_page(self, *args):
        UpdateConfigfile("starting_page", Assets.page_names.index(self.page_var.get()))

    def change_browser(self, *args):
        UpdateConfigfile("browser", self.browser_var.get())

    def update_end_of_lesson_reminder(self):
        UpdateConfigfile("end_of_lesson_reminder", bool(self.end_of_lesson_reminder_button_var.get()))

    def change_clock_settings(self):
        UpdateConfigfile("clock_mode", self.selected.get())

    def change_top_theme_selector_settings(self):
        UpdateConfigfile("enable_top_theme_selector", bool(self.top_theme_selector_var.get()))
        self.refresh_top_panel()

    def top_lesson_number_settings(self):
        UpdateConfigfile("enable_secondary_notifier", bool(self.secondary_notifier_var.get()))
        self.refresh_top_panel()

    def change_top_end_of_lesson_timer_settings(self):
        UpdateConfigfile("enable_primary_notifier", bool(self.primary_notifier_var.get()))
        self.refresh_top_panel()

    def change_page_to_about(self):
        self.settings_container.pack_forget()
        self.about_container.pack(fill="both", expand=True)
        self.about_page.change_page(0)

    def show_settings_page(self):
        self.about_container.pack_forget()
        self.settings_container.pack(fill="both", expand=True)
