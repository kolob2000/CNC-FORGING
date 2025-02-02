import customtkinter as ctk

from utils.constants import ORANGE


class CommonCTkComboBox(ctk.CTkComboBox):
    def __init__(self, master, **kwargs):
        ctk.CTkComboBox.__init__(self, master, **kwargs)
        self.master = master
        self.grid_propagate(False)
        self.configure(height=34, width=246,font=('Roboto', 14), border_color='#343638',
                       border_width=1)