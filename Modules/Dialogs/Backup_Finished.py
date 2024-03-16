import ttkbootstrap as ttk


class BackupFinished:
    def __init__(self, master, delta, files_not_found, all_files):
        self.top_level = ttk.Toplevel(master=master, title="Backup finished")
        self.top_level.minsize(width=600, height=220)
        self.top_level.transient(master)
        self.top_level.grab_set()

        title_label = ttk.Label(master=self.top_level, text="Backup finished", font=('Calibri', '22', 'bold'),
                                style="primary")
        title_label.pack(padx=15, pady=(15, 0))

        time_label = ttk.Label(master=self.top_level, text=f"Duration: {delta}", font=('Calibri', '14'),
                               style="warning")
        time_label.pack()

        info_frame = ttk.LabelFrame(self.top_level, text="Info", style="info")

        total_label = ttk.Label(master=info_frame, text=f"Total files: {all_files}", font=('Calibri', '14'),
                                style="info", anchor="w", width=30)
        total_label.pack(padx=10, anchor="w")

        successful = ttk.Label(master=info_frame, text=f"Successfull: {all_files - len(files_not_found)}",
                               font=('Calibri', '14'),
                               style="success", anchor="w", width=30)
        successful.pack(padx=10, anchor="w")

        files_not_found_label = ttk.Label(master=info_frame, text=f"Files not found: {len(files_not_found)}",
                                          font=('Calibri', '14'),
                                          style="danger", anchor="w", width=30)
        files_not_found_label.pack(padx=10, anchor="w")

        column = ["Files not found"]
        self.tabel = ttk.Treeview(master=info_frame, columns=column, style="secondary", show="headings")
        self.tabel.heading('Files not found', text="Files not found")

        # Load in preset names to tabel
        for i, location in enumerate(files_not_found):
            self.tabel.insert('', i, values=[location])
        self.tabel.pack(padx=10, pady=10, fill="both", expand=True)

        info_frame.pack(pady=(0, 10), padx=10, fill="both", expand=True)
        accept_button = ttk.Button(master=self.top_level, text="Accept", command=self.top_level.destroy)
        accept_button.pack(padx=10, pady=10, anchor="e")
        self.top_level.mainloop()
