import customtkinter as ctk

import frame.MainFrame as MainFrame
from utils.constants import RED
from widgets import CommonCTkButton


class SnailFrame(MainFrame.MainFrame):
    def __init__(self, master):
        MainFrame.MainFrame.__init__(self, master)
        self.master = master

        self.label = ctk.CTkLabel(master=self, text="Snail Frame", font=('Roboto', 20))
        self.label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        #################
        self.connect_button = ctk.CTkButton(self, text="Круглая", width=100, height=100, corner_radius=50)
        self.connect_button.grid(row=0, column=3, padx=10, pady=(20, 10))