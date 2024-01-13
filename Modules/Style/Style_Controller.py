import os.path
from ttkbootstrap.dialogs.dialogs import Messagebox
from Modules.Configfile.Update_Configfile import UpdateConfigfile


class StyleController:
    def __init__(self, style, config):
        self.style = style
        self.default_themes = style.theme_names()
        self.themes = []
        self.initial_theme = config.theme
        self.load_themes(config.custom_themes)

    def load_themes(self, custom_themes):
        if custom_themes:
            print("BAR")
            self.load_custom_themes()
        else:
            print("GOOD")
            self.themes = self.default_themes
            # self.set_current_theme(self.initial_theme)

    def load_custom_themes(self):
        if self.check_if_themes_exists():
            loading_success_full = self.try_load_custom_themes()
            self.themes = self.style.theme_names()
            self.set_current_theme(self.initial_theme)
            if not loading_success_full:
                self.show_error_dialog("Themes file is invalid! Some of the custom themes might not be available.")
        else:
            self.set_current_theme(self.initial_theme)
            self.show_error_dialog("The themes file doesn't exists!\nOnly default theme are available.")

    def set_current_theme(self, theme):
        if theme in self.themes:
            self.style.theme_use(theme)
        else:
            self.show_error_dialog("Selected theme is invalid! Reverting to default theme.")
        UpdateConfigfile("theme", self.style.theme.name)

    def try_load_custom_themes(self):
        try:
            self.style.load_user_themes(file="Themes/themes.json")
        except TypeError:
            return False
        return True

    @staticmethod
    def check_if_themes_exists():
        if os.path.exists("Themes/themes.json"):
            if os.path.exists("Themes/themes.json"):
                return True
        return False

    @staticmethod
    def show_error_dialog(message):
        Messagebox.show_error(title="Theme error", message=message)
