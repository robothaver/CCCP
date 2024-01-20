import ttkbootstrap as ttk
from Modules.Pages.Dashboard.UI.Application_Dashboard_UI import ApplicationDashboardUI
from Modules.Pages.Utility_Pages.Break_Pattern.Break_Pattern import BreakPattern
from Modules.Pages.Utility_Pages.Config_Mover.Copy_Save_File_To_And_From_Pc import CopySaveFileToAndFromPc
from Modules.Pages.Utility_Pages.Copy_Network_Settings.Copy_Network_Settings import CopyNetworkSettings
from Modules.Pages.Utility_Pages.Relative_Path_Generator.Relative_Path_Generator import RelativePathGenerator
from Modules.Pages.Utility_Pages.To_Do_List.To_Do_List import ToDoList


class ApplicationDashboard(ApplicationDashboardUI):
    def __init__(self, master, navigation_controller):
        self.dashboard_page = ttk.Frame(master)
        super().__init__(self.dashboard_page)
        self.master = master
        self.navigation_controller = navigation_controller

        self.copy_save_file_button.config(command=lambda: self.change_local_page(0))
        self.to_do_list_button.config(command=lambda: self.change_local_page(1))
        self.break_pattern_button.config(command=lambda: self.change_local_page(2))
        self.copy_network_settings_button.config(command=lambda: self.change_local_page(3))
        self.relative_path_generator_button.config(command=lambda: self.change_local_page(4))

        self.utility_pages = [
            CopySaveFileToAndFromPc(self.secondary_container, self.show_dashboard),
            ToDoList(self.secondary_container, self.show_dashboard),
            BreakPattern(self.secondary_container, self.show_dashboard),
            CopyNetworkSettings(self.secondary_container, self.show_dashboard),
            RelativePathGenerator(self.secondary_container, self.show_dashboard)
        ]

    def hide_menu(self):
        self.main_container.pack_forget()
        self.secondary_container.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.main_container.pack(fill="both", expand=True)
        for widget in self.secondary_container.winfo_children():
            widget.pack_forget()
        self.secondary_container.pack_forget()

    def hide_all_widgets(self):
        for widget in self.secondary_container.winfo_children():
            widget.pack_forget()

    def change_local_page(self, index):
        self.hide_menu()
        self.utility_pages[index].master_container.pack(fill="both", expand=True)
