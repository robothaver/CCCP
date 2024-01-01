class NavigationController:
    def __init__(self, master_container):
        self.master_container = master_container
        self.page_index = 0

    def get_all_pages(self):
        return self.master_container.winfo_children()

    def hide_all_pages(self):
        for widget in self.get_all_pages():
            widget.pack_forget()

    def change_page(self, page_index):
        self.hide_all_pages()
        pages = self.get_all_pages()
        pages[page_index].pack(fill="both", expand=True)
