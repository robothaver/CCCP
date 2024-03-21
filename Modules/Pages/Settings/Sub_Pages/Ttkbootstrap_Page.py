import ttkbootstrap as ttk
from Assets import Assets
from Modules.Configfile.Config import Configfile
from Modules.Utilities.Launch_Browser import LaunchBrowser


class TtkbootstrapPage:
    def __init__(self, master, change_page):
        # Define variables
        self.master = master
        self.change_page = change_page

        # Create back button
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=self.back)
        back_button.pack(side="left", padx=10, pady=10)
        back_frame.pack(fill="x")

        # Create main_frame
        main_frame = ttk.Frame(master)
        title = ttk.Label(main_frame, text="ttkboostrap", font=('arial', '16', 'bold'), style="info")
        title.pack(pady=5)
        separator = ttk.Separator(main_frame)
        separator.pack(fill="x", padx=100)

        # Create description widgets
        description = ttk.Label(main_frame, text=Assets.ttkbootstrap_description, font=('arial', '12', 'bold'),
                                wraplength=500, justify="center")
        description.pack()

        # Create GitHub button
        self.github_icon = ttk.PhotoImage(file="Assets/Images/Github_Icon.png")
        github_button = ttk.Button(master=main_frame, text="GitHub page", style="warning",
                                   command=self.open_github_page, width=60, image=self.github_icon, compound="left")

        github_button.pack(pady=20)

        main_frame.pack(fill="both", expand=True)

    def back(self):
        self.change_page(0)

    @staticmethod
    def open_github_page():
        LaunchBrowser(Assets.ttkbootstrap_link, Configfile().browser)
