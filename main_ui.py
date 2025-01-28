import customtkinter as ctk
import TopFrame as tfr
from PIL import Image
import SideFrame as sf
import ConnectFrame as cfr


class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('CNC Forging')
        self.resizable(True, True)
        self.geometry('1000x600')
        self.configure(padx=10, pady=10)
        ctk.set_appearance_mode('dark')
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, weight=1)
        ######################################################################################
        self.top_frame = tfr.TopFrame(self)
        ######################################################################################
        self.side_frame = sf.SideFrame(self)
        ######################################################################################
        self.connect_frame = cfr.ConnectFrame(self)

