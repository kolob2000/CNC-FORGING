import customtkinter as ctk
from PIL import Image


class TransparentImageCTkButton(ctk.CTkButton):
    def __init__(self, master,img, **kwargs):
        ctk.CTkButton.__init__(self, master, **kwargs)
        self.master = master
        print(img)
        self.img = Image.open(img)
        self.image = ctk.CTkImage(light_image=self.img, dark_image=self.img, size=(50, 50))
        self.configure( text='', width=100, fg_color='transparent',hover_color='#353535', image=self.image)

