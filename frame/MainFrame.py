import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)
        self.master = master
        self.grid(row=1, column=1, sticky='nsew')
