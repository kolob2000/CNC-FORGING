import customtkinter as ctk
import widgets.TransparentCTkButton as TransparentCTkButton
from utils.constants import ORANGE, TRANSPARENT_ACTIVE_BUTTON


class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)
        self.master = master
        self.grid(row=1, column=0, sticky='nsw', padx=(0, 10))
        self.configure(border_color=ORANGE, border_width=1)

        #######
        self.btn_connect = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/net.png',
                                                                          command=lambda: master.show('connect_frame',self.btn_connect))
        self.btn_connect.configure(fg_color=TRANSPARENT_ACTIVE_BUTTON)
        self.btn_connect.grid(column=0, row=0, padx=10,
                              pady=10, sticky='new')
        self.master.current_button = self.btn_connect
        #######
        self.btn_volt = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/volt.png',
                                                                       command=lambda: master.show('volt_frame', self.btn_volt))
        self.btn_volt.grid(column=0, row=1, padx=10,
                           pady=10, sticky='new')
        #######
        self.btn_snail = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/spiral.png',
                                                                        command=lambda: master.show('snail_frame',self.btn_snail))
        self.btn_snail.grid(column=0, row=2, padx=10,
                            pady=10, sticky='new')
        #######
        self.btn_hand = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/hand.png',
                                                                       command=lambda: master.show('hand_frame', self.btn_hand))
        self.btn_hand.grid(column=0, row=3, padx=10,
                           pady=10, sticky='new')
        #######
        self.btn_vfd = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/vfd.png',
                                                                       command=lambda: master.show('control_frame', self.btn_vfd))
        self.btn_vfd.grid(column=0, row=4, padx=10,
                           pady=10, sticky='new')
