from Assets import Assets
from Modules.Pages.Settings.Sub_Pages.About.UI.About_UI import AboutUI
from Modules.Pages.Settings.Sub_Pages.Ttkbootstrap_Page import TtkbootstrapPage
from Modules.Utilities.Launch_Browser import LaunchBrowser


class About(AboutUI):
    def __init__(self, master, show_settings_page, config):
        super().__init__(master)
        # Defining variables
        self.master = master
        self.config = config

        # Connecting widgets to functions
        self.github_button.config(command=self.open_github_page)
        self.ttkbootstrap_button.config(command=lambda: self.change_page(2))
        self.back_button.config(command=show_settings_page)

        # Creating ttkbootstrap page
        self.bootstrap_page = TtkbootstrapPage(self.bootstrap_container, self.change_page)

    def change_page(self, page_index):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        if page_index == 0:
            self.main_container.pack(fill="both", expand=True)
        else:
            self.bootstrap_container.pack(fill="both", expand=True)
    
    def open_github_page(self):
        LaunchBrowser(Assets.github_link, self.config.browser)
