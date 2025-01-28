import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.master = master
        self.grid(row=1, column=1, sticky='nsew')
