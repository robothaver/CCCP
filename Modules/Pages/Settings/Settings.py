from Assets import Assets
from Modules.Configfile.Update_Configfile import UpdateConfigfile
from Modules.Pages.Settings.Sub_Pages.About.About import About
from Modules.Pages.Settings.UI.Settings_UI import SettingsUI
from Modules.Dialogs.Change_NOL import ChangeNOL


class Settings(SettingsUI):
    def __init__(self, master, config, style_controller, refresh_top_panel, navigation_controller):
        super().__init__(master)
        # Define variables
        self.config = config
        self.style_controller = style_controller
        self.refresh_top_panel = refresh_top_panel
        self.navigation_controller = navigation_controller
        self.about_page = About(self.about_container, self.show_settings_page, self.config)

        self.show_settings_page()
        self.refresh_theme()

        # Setting widget values
        self.custom_themes_button_var.set(self.config.custom_themes)
        reminder_value = "minute" if self.config.reminder_activation == 1 else "minutes"
        self.reminder_activation_var.set(f"{self.config.reminder_activation} {reminder_value}")
        self.end_of_lesson_reminder_button_var.set(self.config.end_of_lesson_reminder)
        self.primary_notifier_var.set(self.config.enable_primary_notifier)
        self.secondary_notifier_var.set(self.config.enable_secondary_notifier)
        self.top_theme_selector_var.set(self.config.enable_top_theme_selector)
        self.progress_bar_var.set(self.config.enable_progress_bar)
        self.theme_var.set(style_controller.style.theme.name)
        self.selected.set(self.config.clock_mode)
        self.page_var.set(Assets.page_names[self.config.starting_page])
        self.browser_var.set(self.config.browser)

        # Connecting buttons to functions
        self.page_var.trace("w", self.change_starting_page)
        self.theme_var.trace("w", self.change_theme)
        self.custom_themes_button_var.trace("w", self.change_custom_themes)
        self.reminder_activation_var.trace("w", self.change_reminder_activation)
        self.browser_var.trace("w", self.change_browser)
        self.progress_bar_var.trace("w", self.change_progress_bar_settings)

        self.clock_settings_40_10.config(command=self.change_clock_settings)
        self.clock_settings_45_10.config(command=self.change_clock_settings)
        self.clock_settings_35_5.config(command=self.change_clock_settings)
        self.clock_settings_35_10.config(command=self.change_clock_settings)
        self.lesson_per_day_button.config(command=lambda: ChangeNOL(self.master_container))
        self.end_of_lesson_reminder_button.config(command=self.update_end_of_lesson_reminder)
        self.top_theme_selector_button.config(command=self.change_top_theme_selector_settings)
        self.primary_notifier.config(command=self.change_top_end_of_lesson_timer_settings)
        self.secondary_notifier.config(command=self.top_lesson_number_settings)
        self.about_button.config(command=self.change_page_to_about)

    def refresh_theme(self):
        self.theme_changer.set_menu(None, *self.style_controller.themes)

    def change_custom_themes(self, *args):
        custom_themes = bool(self.custom_themes_button_var.get())
        UpdateConfigfile("custom_themes", custom_themes)
        self.style_controller.load_themes(custom_themes)
        self.refresh_theme()
        self.refresh_top_panel()

    def change_reminder_activation(self, *args):
        UpdateConfigfile("reminder_activation", int(self.reminder_activation_var.get().split()[0]))
        self.refresh_top_panel(True)

    def change_theme(self, *args):
        theme = self.theme_var.get()
        self.style_controller.set_current_theme(theme)
        self.refresh_top_panel()

    def change_starting_page(self, *args):
        UpdateConfigfile("starting_page", Assets.page_names.index(self.page_var.get()))

    def change_browser(self, *args):
        UpdateConfigfile("browser", self.browser_var.get())

    def update_end_of_lesson_reminder(self):
        UpdateConfigfile("end_of_lesson_reminder", bool(self.end_of_lesson_reminder_button_var.get()))
        self.refresh_top_panel(True)

    def change_clock_settings(self):
        UpdateConfigfile("clock_mode", self.selected.get())
        self.refresh_top_panel(True)

    def change_top_theme_selector_settings(self):
        UpdateConfigfile("enable_top_theme_selector", bool(self.top_theme_selector_var.get()))
        self.refresh_top_panel()

    def change_progress_bar_settings(self, *args):
        UpdateConfigfile("enable_progress_bar", bool(self.progress_bar_var.get()))
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
