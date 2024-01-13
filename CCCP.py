import tkinter as tk

import ttkbootstrap as ttk
from Modules.Style.Style_Controller import StyleController
from Modules.Configfile.Config import Configfile
from Modules.Pages.Backup.Backup_Page import BackupPage
from Modules.Pages.Dashboard.Application_Dashboard import ApplicationDashboard
from Modules.Pages.File_Generator.File_Generator_Page import FileGeneratorPage
from Modules.Pages.Home.Home_Page import HomePage
from Modules.Pages.Settings.Settings import Settings
from Modules.Panels.Navigation_Bar.Bottom_Navigation_Bar import BottomNavigationBar
from Modules.Panels.Top_Panel.Top_Panel import TopPanel
from Modules.Utilities.Navigation_Controller.Navigation_Controller import NavigationController


class CCCP:
    def __init__(self):
        # This is the main class of the program

        # Load in the configfile
        config = Configfile()

        # Create the tkinter window
        self.window = tk.Tk()
        self.window.geometry("600x850")
        self.window.title("CCCP")
        icon = tk.PhotoImage(file="Assets/Images/CCCP_logo_500x500.png")
        self.window.iconphoto(False, icon)
        self.style = ttk.Style()

        # self.window.resizable(False,False) #Blocks resize
        # self.window.attributes('-topmost', 'true')

        # Creating main frames
        # Top frame
        self.top_frame = ttk.Frame(master=self.window)
        self.top_frame.pack(fill="both")

        # Separate
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill="x", padx=5, pady=('10', '20'))

        # Middle frame
        self.middle_frame = ttk.Frame(master=self.window)
        self.middle_frame.pack(fill="both", expand=True)

        # Bottom frame
        self.bottom_frame = ttk.Frame(master=self.window)
        self.bottom_frame.pack(side="bottom", fill="x", ipady=20)

        self.navigation_controller = NavigationController(self.middle_frame, self.refresh_top_panel)
        self.style_controller = StyleController(self.style, config)

        self.top_panel = TopPanel(self.top_frame, self.style_controller)

        # Add pages to middle frame
        HomePage(self.middle_frame)
        BackupPage(self.middle_frame, self.window)
        FileGeneratorPage(self.middle_frame)
        ApplicationDashboard(self.middle_frame)
        Settings(self.middle_frame, self.style_controller, self.refresh_top_panel)

        # Calling GUI elements
        self.navbar = BottomNavigationBar(self.bottom_frame, self.navigation_controller)
        self.navbar.change_page()
        self.window.mainloop()

    def refresh_top_panel(self):
        self.top_panel.refresh()


if __name__ == '__main__':
    CCCP()
