class NavigationController:
    def __init__(self):
        self.page_index = 0
        self.page_objects = []

    def add_pages(self, pages):
        self.page_objects = pages

    def update_page(self, index, refresh_type=None):
        if refresh_type is not None:
            self.page_objects[index].refresh_page(refresh_type)
        self.page_objects[index].refresh_page()

    def change_page(self, page_index):
        # Hide current page
        self.hide_page(self.page_index)
        self.page_index = page_index
        # Show selected page
        self.page_objects[page_index].master_container.pack(fill="both", expand=True)

    def hide_page(self, index):
        self.page_objects[index].master_container.pack_forget()
