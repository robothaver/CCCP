import ttkbootstrap as ttk
from Modules.Pages.Dashboard.UI.Application_Dashboard_UI import ApplicationDashboardUI
from Modules.Pages.Utility_Pages.Break_Pattern.Break_Pattern import BreakPattern
from Modules.Pages.Utility_Pages.Config_Mover.Copy_Save_File_To_And_From_Pc import CopySaveFileToAndFromPc
from Modules.Pages.Utility_Pages.Copy_Network_Settings.Copy_Network_Settings import CopyNetworkSettings
from Modules.Pages.Utility_Pages.Relative_Path_Generator.Relative_Path_Generator import RelativePathGenerator
from Modules.Pages.Utility_Pages.To_Do_List.To_Do_List import ToDoList


class ApplicationDashboard(ApplicationDashboardUI):
    def __init__(self, master):
        self.dashboard_page = ttk.Frame(master)
        super().__init__(self.dashboard_page)
        self.master = master

        self.copy_save_file_button.config(command=lambda: self.change_local_page(0))
        self.to_do_list_button.config(command=lambda: self.change_local_page(1))
        self.break_pattern_button.config(command=lambda: self.change_local_page(2))
        self.copy_network_settings_button.config(command=lambda: self.change_local_page(3))
        self.relative_path_generator_button.config(command=lambda: self.change_local_page(4))

    def hide_dashboard(self):
        self.main_container.pack_forget()
        self.secondary_container.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.main_container.pack(fill="both", expand=True)
        for widget in self.secondary_container.winfo_children():
            widget.destroy()
        self.secondary_container.pack_forget()

    def change_local_page(self, index):
        self.hide_dashboard()
        if index == 0:
            CopySaveFileToAndFromPc(self.secondary_container, self.show_dashboard)
        elif index == 1:
            ToDoList(self.secondary_container, self.show_dashboard)
        elif index == 2:
            BreakPattern(self.secondary_container, self.show_dashboard)
        elif index == 3:
            CopyNetworkSettings(self.secondary_container, self.show_dashboard)
        else:
            RelativePathGenerator(self.secondary_container, self.show_dashboard)
