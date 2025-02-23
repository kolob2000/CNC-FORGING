import customtkinter as ctk

from frame.MainFrame import MainFrame
from utils.constants import  GREEN, RED
from widgets import  TransparentCTkButton
from utils.ModbusInteraction import ModbusInteraction


class VFDControlFrame(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.master = master
        #################
        self.forward_button = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/forward.png',
                                                                             command=lambda: self.on_button_click(
                                                                                 'forward'))
        self.forward_button.configure(width=50, height=50)
        self.forward_button.grid(row=1, column=3, padx=10, pady=(20, 10))
        #################
        self.reverse_button = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/reverse.png',
                                                                             command=lambda: self.on_button_click(
                                                                                 'reverse'))
        self.reverse_button.configure(width=50, height=50)
        self.reverse_button.grid(row=1, column=1, padx=(50, 10), pady=(20, 10))
        #################
        self.stop_button = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/stop.png',
                                                                          command=lambda: self.on_button_click(
                                                                              'deceleration_stop'))
        self.stop_button.configure(width=50, height=50)
        self.stop_button.grid(row=1, column=2, padx=10, pady=(20, 10))
        #################
        self.increase_button = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/increase.png',
                                                                              command=lambda: self.set_frequency(
                                                                                  increase=True))
        self.increase_button.configure(width=50, height=50)
        self.increase_button.grid(row=0, column=2, padx=10, pady=(20, 10))
        #################
        self.decrease_button = TransparentCTkButton.TransparentImageCTkButton(master=self, img='theme/img/decrease.png',
                                                                              command=lambda: self.set_frequency(
                                                                                  increase=False))
        self.decrease_button.configure(width=50, height=50)
        self.decrease_button.grid(row=2, column=2, padx=10, pady=(20, 10))
        #################
        self.frequency_label = ctk.CTkLabel(master=self, text='- -', font=('Roboto', 45), fg_color=GREEN,
                                            text_color=RED)
        self.frequency_label.configure(width=150, height=150, corner_radius=15)
        self.frequency_label.grid(row=0, column=4, padx=10, rowspan=3, pady=(20, 10))

    def on_button_click(self, command):
        if self.master.client is None or not self.master.client.connected:
            return 'Отсутствует соединение с клиентом.'
        if command == 'forward' or command == 'reverse':
            self.frequency_label.configure(text=self.current_frequency() / 100)
        response = ModbusInteraction.write_modbus_command_sql(self.master.client, self.master.db_connection,
                                                              command=command)

    def set_frequency(self, increase=True):
        if self.master.client is None or not self.master.client.connected:
            return 'Отсутствует соединение с клиентом.'
        try:
            max_frequency = ModbusInteraction.get_modbus_param_sql(self.master.client, self.master.db_connection,
                                                                   'max_frequency', for_set=True)
            current_frequency = ModbusInteraction.get_modbus_param_sql(self.master.client, self.master.db_connection,
                                                                       'current_frequency', for_set=True)
            if increase and current_frequency < max_frequency:
                ModbusInteraction.set_modbus_param_sql(self.master.client, self.master.db_connection,
                                                       'frequency_setting', current_frequency * 2 + 200)
                self.frequency_label.configure(text=f'{(current_frequency + 100) / 100}')
            elif not increase and current_frequency > 0:
                ModbusInteraction.set_modbus_param_sql(self.master.client, self.master.db_connection,
                                                       'frequency_setting', current_frequency * 2 - 200)
                self.frequency_label.configure(text=f'{(current_frequency - 100) / 100}')
        except Exception as e:
            print(e)

    def current_frequency(self):
        return ModbusInteraction.get_modbus_param_sql(self.master.client, self.master.db_connection,
                                                      'current_frequency', for_set=True)

