import tkinter as tk
import ttkbootstrap as ttk
from Config import Configfile
from Application_Launcher_Gui import ApplicationLauncherGui
from Top_Panel import TopGui
from Bottom_Navigation_Bar import BottomNavigationBar
from Backup_Page import BackupPage
from Settings import Settings
from File_Generator import FileGenerator
from Application_Dashboard import ApplicationDashboard


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
        self.middle_frame = ttk.Frame(master=self.window)
        self.middle_frame.pack(fill="both", expand=True)

        # Bottom frame
        self.bottom_frame = ttk.Frame(master=self.window)
        self.bottom_frame.pack(side="bottom", fill="x", ipady=20)

        # Calling GUI elements
        BottomNavigationBar(self.bottom_frame, self.window, self.middle_frame, self.top_frame, self.style)
        starting_page = config.starting_page
        if starting_page == 5:
            starting_page = config.current_page
        if starting_page == 0:
            ApplicationLauncherGui(self.middle_frame)
        elif starting_page == 1:
            BackupPage(self.middle_frame, self.window)
        elif starting_page == 2:
            FileGenerator(self.middle_frame)
        elif starting_page == 3:
            ApplicationDashboard(self.middle_frame)
        elif starting_page == 4:
            Settings(self.middle_frame, self.top_frame, self.style)
        TopGui(self.top_frame, self.style, self.middle_frame)
        self.window.mainloop()


if __name__ == '__main__':
    AppGui()
