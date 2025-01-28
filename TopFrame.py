import customtkinter as ctk

from PIL import Image

img_light = Image.open('theme/img/sun-solid.png')
img_dark = Image.open('theme/img/moon-solid.png')


class TopFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(0, 10))

        self.label = ctk.CTkLabel(master=self, font=('Roboto', 20, 'bold', 'italic'),
                                  text='CNC FORGING', text_color='#ef5b25')
        self.label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.image = ctk.CTkImage(light_image=img_light, dark_image=img_dark, size=(24, 24))
        self.toggle_theme = ctk.CTkButton(master=self, text='', width=0,
                                          font=('Roboto', 20, 'bold', 'italic'), text_color='#ef5b25',
                                          image=self.image, fg_color='transparent', command=self.toggle_theme)
        self.toggle_theme.grid(row=0, column=1, sticky='e', padx=10, pady=10)

    def toggle_theme(self):
        ctk.set_appearance_mode('light') if ctk.get_appearance_mode().lower() == 'dark' else ctk.set_appearance_mode(
            'dark')
