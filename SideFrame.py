import customtkinter as ctk
from PIL import Image

img = Image.open('theme/img/i.png')
img_connect = Image.open('theme/img/tower-broadcast-solid.png')
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        ctk.CTkFrame.__init__(self, master,**kwargs)
        self.master = master
        self.grid(row=1, column=0, sticky='nsw', padx=(0, 10))

        #######
        self.image = ctk.CTkImage(light_image=img, dark_image=img, size=(50, 50))
        self.image_connect = ctk.CTkImage(light_image=img_connect, dark_image=img_connect, size=(50, 50))
        self.btn = ctk.CTkButton(self, text='',
                                 width=100, fg_color='transparent',
                                 image=self.image_connect, hover_color='#353535')
        self.btn.grid(column=0, row=0, padx=10,
                      pady=10, sticky='n')

        # self.btn1 = ctk.CTkButton(self.main_frame, text='',
        #                           width=100, fg_color='transparent',
        #                           image=self.image, hover_color='#353535')
        # self.btn1.grid(column=0, row=1, padx=10,
        #                pady=10, sticky='nw')
        #
        # self.btn2 = ctk.CTkButton(self.main_frame, text='',
        #                           width=100, fg_color='transparent',
        #                           image=self.image, hover_color='#353535')
        # self.btn2.grid(column=0, row=2, padx=10,
        #                pady=10, sticky='nw')
        #
        # self.btn3 = ctk.CTkButton(self.main_frame, text='',
        #                           width=100, fg_color='transparent',
        #                           image=self.image, hover_color='#353535')
        # self.btn3.grid(column=0, row=3, padx=10,
        #                pady=10, sticky='nw')
