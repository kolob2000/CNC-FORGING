import customtkinter as ctk

from utils.constants import ORANGE


class CommonCTkButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        ctk.CTkButton.__init__(self, master, **kwargs)
        self.master = master
        self.configure(height=38, fg_color='transparent',
                       border_width=1, text_color=ORANGE, font=('Roboto', 16, 'bold'))
