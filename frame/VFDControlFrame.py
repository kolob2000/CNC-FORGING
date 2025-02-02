import customtkinter as ctk

from frame.MainFrame import MainFrame
from utils.constants import ORANGE, GREEN, RED
from widgets import CommonCTkButton
from utils.ModbusInteraction import ModbusInteraction


class VFDControlFrame(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.master = master
        #################
        self.forward_button = CommonCTkButton.CommonCTkButton(master=self, text='Вперед',
                                                              command=lambda: self.on_button_click('forward'))
        self.forward_button.configure(border_color=GREEN, text_color=GREEN)
        self.forward_button.grid(row=0, column=1, padx=10, pady=(20, 10))
        #################
        self.reverse_button = CommonCTkButton.CommonCTkButton(master=self, text='Назад',
                                                              command=lambda: self.on_button_click('reverse'))
        self.reverse_button.configure(border_color=ORANGE)
        self.reverse_button.grid(row=0, column=2, padx=10, pady=(20, 10))
        #################
        self.connect_button = CommonCTkButton.CommonCTkButton(master=self, text='Стоп',
                                                              command=lambda: self.on_button_click('deceleration_stop'))
        self.connect_button.configure(border_color=RED, text_color=RED)
        self.connect_button.grid(row=0, column=3, padx=10, pady=(20, 10))

    def on_button_click(self, command):
        # response = ModbusInteraction.write_modbus_register(self.master.client, address, value, unit_id=1)
        response = ModbusInteraction.write_modbus_command_sql(self.master.client, self.master.db_connection,
                                                              command=command)
        print(response)
