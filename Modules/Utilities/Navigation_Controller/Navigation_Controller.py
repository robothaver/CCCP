class NavigationController:
    def __init__(self, master_container):
        self.master_container = master_container
        self.page_index = 0
        self.pages = []
        self.page_objects = []

    def add_pages(self, pages):
        self.page_objects = pages

    def update_page(self, index, refresh_type=None):
        if refresh_type is not None:
            self.page_objects[index].refresh_page(refresh_type)
        self.page_objects[index].refresh_page()

    def change_page(self, page_index):
        self.hide_all_pages()
        self.pages = self.get_all_pages()
        self.pages[page_index].pack(fill="both", expand=True)

    def get_all_pages(self):
        return self.master_container.winfo_children()

    def hide_all_pages(self):
        for page in self.master_container.winfo_children():
            page.pack_forget()
