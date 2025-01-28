import customtkinter as ctk

from utils.constants import ORANGE


class CommonCTkEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        ctk.CTkEntry.__init__(self, master, **kwargs)
        self.master = master
        self.configure(height=38, font=('Roboto', 14), border_color=ORANGE, border_width=1)
