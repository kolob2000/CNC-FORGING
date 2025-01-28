import customtkinter as ctk

from frame.MainFrame import MainFrame
from utils.constants import ORANGE
from widgets import CommonCTkEntry


class HandFrame(MainFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.speed_label = ctk.CTkLabel(self, text="Скорость:", text_color=ORANGE,
                                        font=('Roboto', 16, 'bold', 'italic'))
        self.speed_label.grid(row=1, column=0, padx=10, pady=(20, 10))
        self.speed_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='скорость', width=250)
        self.speed_entry.grid(row=1, column=1, sticky='w', padx=10, pady=(20, 10))
        self.speed_entry.insert(0, '9600')