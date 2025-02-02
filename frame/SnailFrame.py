import customtkinter as ctk

import frame.MainFrame as MainFrame


class SnailFrame(MainFrame.MainFrame):
    def __init__(self, master):
        MainFrame.MainFrame.__init__(self, master)
        self.master = master

        self.label = ctk.CTkLabel(master=self, text="Snail Frame", font=('Roboto', 20))
        self.label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
