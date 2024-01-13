import tkinter as tk
import ttkbootstrap as ttk
import subprocess
from Modules.Pages.Dashboard import Application_Dashboard
from tkinter import filedialog


class CopyNetworkSettings:
    def __init__(self, master, show_dashboard):
        # Define variables
        self.master = master

        # Create back button
        self.back_button_icon = tk.PhotoImage(file="Assets/Images/back_icon.png")
        back_frame = ttk.Frame(master)
        back_button = ttk.Button(back_frame, text="Back", command=show_dashboard,
                                 image=self.back_button_icon, compound="left")
        back_button.pack(side="left", padx=10, pady=5)

        # Create is kando checkbutton
        self.is_kando_var = ttk.IntVar()
        is_kando_button = ttk.Checkbutton(back_frame, text="Kando mode", variable=self.is_kando_var,
                                          style="info round-toggle", command=self.refresh)
        is_kando_button.pack(side="right", padx=10, pady=5)
        back_frame.pack(fill="x")

        # Create title label
        title_label = ttk.Label(master, text="Network settings:", font=('Aril', '16', 'bold'), style="info")
        title_label.pack(pady=10)

        # Create ipv4 frame
        ipv4_frame = ttk.Frame(master)
        # Create ipv4 label
        ipv4_label = ttk.Label(ipv4_frame, text="IPv4 Address:", font=('Aril', '13'), style="info", width=15)
        # Create ipv4 entry
        self.ipv4_entry_var = tk.StringVar(value=subprocess.getoutput('ipconfig | findstr /i "ipv4"')[39:60])
        self.ipv4_entry = ttk.Entry(ipv4_frame, textvariable=self.ipv4_entry_var, font=('Aril', '11'))
        # Packing
        ipv4_label.pack(side="left", padx=5)
        self.ipv4_entry.pack(side="left", padx=10, fill="x", expand=1)
        ipv4_frame.pack(padx=25, pady=10, fill="x")

        # Create subnet mask frame
        subnet_mask_frame = ttk.Frame(master)
        # Create subnet mask label
        subnet_mask_label = ttk.Label(subnet_mask_frame, text="Subnet Mask:", font=('Aril', '13'),
                                      style="info", width=15)
        # Create subnet mask entry
        self.subnet_mask_entry_var = tk.StringVar(
            value=subprocess.getoutput('ipconfig | findstr /i "Subnet Mask"')[39:60])
        subnet_mask_entry = ttk.Entry(subnet_mask_frame, textvariable=self.subnet_mask_entry_var, font=('Aril', '11'))
        # Packing
        subnet_mask_label.pack(side="left", padx=5)
        subnet_mask_entry.pack(side="left", padx=10, fill="x", expand=1)
        subnet_mask_frame.pack(padx=25, pady=10, fill="x")

        # Create default gateway frame
        default_gateway_frame = ttk.Frame(master)
        # Create default gateway label
        default_gateway_label = ttk.Label(default_gateway_frame, text="Default Gateway:", font=('Aril', '13'),
                                          style="info", width=15)
        # Create default gateway entry
        self.default_gateway_entry_var = tk.StringVar(value=subprocess.getoutput('ipconfig -all')[891:903])
        default_gateway_entry = ttk.Entry(default_gateway_frame, textvariable=self.default_gateway_entry_var,
                                          font=('Aril', '11'))
        # Packing
        default_gateway_label.pack(side="left", padx=5)
        default_gateway_entry.pack(side="left", padx=10, fill="x", expand=1)
        default_gateway_frame.pack(padx=25, pady=10, fill="x")

        # Create dns server frame
        dns_servers_frame = ttk.Frame(master)
        # Create dns server label
        dns_servers_label = ttk.Label(dns_servers_frame, text="DNS Servers:", font=('Aril', '13'),
                                      style="info", width=15)
        # Create dns server entry
        self.dns_servers_entry_var = tk.StringVar(value=subprocess.getoutput('ipconfig -all')[1311:1319])
        dns_servers_entry = ttk.Entry(dns_servers_frame, textvariable=self.dns_servers_entry_var,
                                      font=('Aril', '11'))
        # Packing
        dns_servers_label.pack(side="left", padx=5)
        dns_servers_entry.pack(side="left", padx=10, fill="x", expand=1)
        dns_servers_frame.pack(padx=25, pady=10, fill="x")

        # Create save network settings button
        save_network_settings_button = ttk.Button(master, text="Save network settings",
                                                  style="success", command=self.save_network_settings)
        save_network_settings_button.pack(fill="x", padx=50, pady=20)

    def back(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        Application_Dashboard.ApplicationDashboard(self.master)

    def save_network_settings(self):
        # This function runs whenever the save network settings button is pressed
        # The function saves the network settings into a txt file into the directory given by the user
        output = filedialog.askdirectory(title="File output directory")
        if output != ():
            with open(f"{output}/network_settings.txt", "w") as file:
                file.write(f"IPv4 Address: {self.ipv4_entry_var.get()}")
                file.write(f"\nSubnet Mask: {self.subnet_mask_entry_var.get()}")
                file.write(f"\nDefault Gateway: {self.default_gateway_entry_var.get()}")
                file.write(f"\nDNS Servers: {self.dns_servers_entry_var.get()}")

    def refresh(self):
        # This function gets called whenever the is kando check button is pressed
        if self.is_kando_var.get() == 0:
            self.dns_servers_entry_var.set(value=subprocess.getoutput('ipconfig -all')[1130:1140].replace(" ", ""))
        else:
            self.dns_servers_entry_var.set(
                value=subprocess.getoutput('ipconfig -all | findstr /i "DNS Servers"')[167:185])
