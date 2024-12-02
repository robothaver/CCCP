import os


class LaunchBrowser:
    def __init__(self, link, preferred_browser, is_private=False, is_guest=False):
        self.link = link
        self.preferred_browser = preferred_browser
        self.is_private = is_private
        self.is_guest = is_guest

        self.open_link()

    def open_link(self):
        if self.preferred_browser == "system default":
            command = f"start {self.link}"
        elif self.preferred_browser == "firefox":
            command = self.get_firefox_parameters()
        else:
            command = self.get_chromium_parameters()
        os.system(command)

    def get_chromium_parameters(self):
        command = f"start {self.preferred_browser} "
        disable_search_engine_screen = "--disable-search-engine-choice-screen"
        if self.is_private:
            command += f"{disable_search_engine_screen} --private-window {self.link}"
        elif self.is_guest:
            command += f"{disable_search_engine_screen} --guest {self.link}"
        else:
            command += f"{disable_search_engine_screen} {self.link}"
        return command

    def get_firefox_parameters(self):
        command = f"start {self.preferred_browser} "
        if self.is_private:
            command += "--private-window {link}"
        else:
            command += "link"
        return command
