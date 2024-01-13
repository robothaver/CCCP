class NavigationController:
    def __init__(self, master_container, refresh_top_panel):
        self.master_container = master_container
        self.refresh_top_panel = refresh_top_panel
        self.page_index = 0
        self.pages = []

    def update_page_at_index(self, index):
        self.pages[index].refresh_page()

    def get_all_pages(self):
        return self.master_container.winfo_children()

    def hide_all_pages(self):
        for widget in self.get_all_pages():
            widget.pack_forget()

    def change_page(self, page_index):
        self.hide_all_pages()
        self.pages = self.get_all_pages()
        self.pages[page_index].pack(fill="both", expand=True)
