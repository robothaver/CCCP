import tkinter as tk
import ttkbootstrap as ttk
from Modules.Configfile.Config import Configfile
from Modules.Pages.Home.Application_Launcher_Gui import ApplicationLauncher
from Modules.Panels.Top_Panel.Top_Panel import TopGui
from Modules.Panels.Navigation_Bar.Bottom_Navigation_Bar import BottomNavigationBar
from Modules.Pages.Backup.Backup_Page import BackupPage
from Modules.Pages.Settings.Settings import Settings
from Modules.Pages.File_Generator.File_Generator import FileGenerator
from Modules.Pages.Dashboard.Application_Dashboard import ApplicationDashboard
from Modules.Utilities.Navigation_Controller.Navigation_Controller import NavigationController

class AppGui:
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
        self.style = ttk.Style(config.theme)
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
        self.middle_frame = ttk.Frame(master=self.window, style="danger")
        self.middle_frame.pack(fill="both", expand=True)

        # Bottom frame
        self.bottom_frame = ttk.Frame(master=self.window)
        self.bottom_frame.pack(side="bottom", fill="x", ipady=20)

        self.navigation_controller = NavigationController(self.middle_frame)

        # Add pages to middle frame
        ApplicationLauncher(self.middle_frame)
        BackupPage(self.middle_frame, self.window)
        FileGenerator(self.middle_frame)
        ApplicationDashboard(self.middle_frame)
        Settings(self.middle_frame, self.top_frame, self.style)

        # Calling GUI elements
        self.navbar = BottomNavigationBar(self.bottom_frame, self.navigation_controller)
        self.navbar.change_page()
        # starting_page = config.starting_page
        # if starting_page == 5:
        #     starting_page = config.current_page
        # if starting_page == 0:
        #     ApplicationLauncherGui(self.middle_frame)
        # elif starting_page == 1:
        #     BackupPage(self.middle_frame, self.window)
        # elif starting_page == 2:
        #     FileGenerator(self.middle_frame)
        # elif starting_page == 3:
        #     ApplicationDashboard(self.middle_frame)
        # elif starting_page == 4:
        #     Settings(self.middle_frame, self.top_frame, self.style, self.update_top_panel())
        TopGui(self.top_frame, self.style)
        self.window.mainloop()

    def update_top_panel(self):
        for widget in self.top_frame.winfo_children():
            widget.destroy()
        TopGui(self.top_frame, self.style)


if __name__ == '__main__':
    AppGui()
