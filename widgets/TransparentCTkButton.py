import customtkinter as ctk
from PIL import Image

from utils.constants import TRANSPARENT_BUTTON_HOVER


class TransparentImageCTkButton(ctk.CTkButton):
    def __init__(self, master,img, **kwargs):
        ctk.CTkButton.__init__(self, master, **kwargs)
        self.master = master
        self.img = Image.open(img)
        self.image = ctk.CTkImage(light_image=self.img, dark_image=self.img, size=(50, 50))
        self.configure( text='', width=100, fg_color='transparent',hover_color=TRANSPARENT_BUTTON_HOVER, image=self.image)

