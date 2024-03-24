import tkinter as tk
import ttkbootstrap as ttk
from Modules.Configfile.Config import Configfile
from Modules.Pages.Backup.Backup_Page import BackupPage
from Modules.Pages.Dashboard.Application_Dashboard import ApplicationDashboard
from Modules.Pages.Home.Home_Page import HomePage
from Modules.Pages.Project_Generator.Project_Generator_Page import ProjectGeneratorPage
from Modules.Pages.Settings.Settings import Settings
from Modules.Panels.Navigation_Bar.Navigation_Bar import NavigationBar
from Modules.Panels.Top_Panel.Top_Panel import TopPanel
from Modules.Style.Style_Controller import StyleController
from Modules.Utilities.Navigation_Controller.Navigation_Controller import NavigationController


class CCCP:
    def __init__(self):
        config = Configfile()

        self.window = tk.Tk()
        self.window.geometry('650x900')
        self.window.title("CCCP")
        icon = tk.PhotoImage(file="Assets/Images/CCCP_logo_500x500.png")
        self.window.iconphoto(True, icon)
        ttk.utility.enable_high_dpi_awareness(self.window, scaling=1.6)
        self.style = ttk.Style()

        self.top_frame = ttk.Frame(master=self.window)
        self.top_frame.pack(fill="both")

        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill="x", padx=5, pady=('10', '20'))

        self.middle_frame = ttk.Frame(master=self.window)
        self.middle_frame.pack(fill="both", expand=True)

        self.bottom_frame = ttk.Frame(master=self.window)
        self.bottom_frame.pack(side="bottom", fill="x", ipady=20)

        navigation_controller = NavigationController()
        style_controller = StyleController(self.style, config)

        self.top_panel = TopPanel(self.top_frame, config, style_controller, navigation_controller)

        navigation_controller.add_pages([
            HomePage(self.middle_frame, config, navigation_controller),
            BackupPage(self.middle_frame, config),
            ProjectGeneratorPage(self.middle_frame, config),
            ApplicationDashboard(self.middle_frame, config),
            Settings(self.middle_frame, config, style_controller, self.top_panel.refresh, navigation_controller)]
        )

        self.navbar = NavigationBar(self.bottom_frame, navigation_controller, config)
        self.navbar.change_page()
        self.window.mainloop()


if __name__ == '__main__':
    CCCP()
