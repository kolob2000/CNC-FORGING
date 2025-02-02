import customtkinter as ctk

from frame.MainFrame import MainFrame
from utils.constants import ORANGE
from widgets import CommonCTkEntry, CommonCTkButton
from utils.Utils import Utils
from utils.ModbusInteraction import ModbusInteraction as mbi


class HandFrame(MainFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        validate_command = self.register(Utils.validate_digit_input)
        self.master = master
        #############################################################################
        self.id_label = ctk.CTkLabel(self, text="ID Устройства:", text_color=ORANGE,
                                     font=('Roboto', 16, 'bold', 'italic'))
        self.id_label.grid(row=0, column=0, padx=10, pady=(20, 10))
        self.id_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='ID Устройства:',
                                                      width=250)
        self.id_entry.configure(validate='key', validatecommand=(validate_command, '%P'))
        self.id_entry.grid(row=0, column=1, sticky='w', padx=10, pady=(20, 10))
        self.id_entry.insert(0, '1')

        ################################### BUTTONS ##############################
        self.update_port_button = CommonCTkButton.CommonCTkButton(border_color=ORANGE, master=self,
                                                                  text='Прочитать',

                                                                  command=self.on_read_register)
        self.update_port_button.grid(row=0, column=2, padx=10, pady=(20, 10))

        self.connect_button = CommonCTkButton.CommonCTkButton(master=self, text='Записать',
                                                              border_color=ORANGE,
                                                              command=self.on_write_register)
        self.connect_button.grid(row=0, column=23, padx=10, pady=(20, 10))
        #############################################################################
        self.address_label = ctk.CTkLabel(self, text="Адрес регистра:", text_color=ORANGE,
                                          font=('Roboto', 16, 'bold', 'italic'))
        self.address_label.grid(row=1, column=0, padx=10, pady=(20, 10))
        self.address_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='Адрес регистра', width=250)
        self.address_entry.configure(validate='key', validatecommand=(validate_command, '%P'))
        self.address_entry.grid(row=1, column=1, sticky='w', padx=10, pady=(20, 10))
        #############################################################################
        self.value_label = ctk.CTkLabel(self, text="Значение:", text_color=ORANGE,
                                        font=('Roboto', 16, 'bold', 'italic'))
        self.value_label.grid(row=2, column=0, padx=10, pady=(20, 10))
        self.value_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='Значение', width=250)
        self.value_entry.configure(validate='key', validatecommand=(validate_command, '%P'))
        self.value_entry.grid(row=2, column=1, sticky='w', padx=10, pady=(20, 10))

    def on_read_register(self):
        address = self.address_entry.get()
        unit_id = self.id_entry.get()
        if len(address) and len(unit_id):
            response = mbi.read_modbus_register(client=self.master.client,
                                                register=int(address), unit_id=int(unit_id))
            print(response)
        else:
            print('no address or unit_id')

    def on_write_register(self):
        address = self.address_entry.get()
        unit_id = self.id_entry.get()
        value = self.value_entry.get()
        if len(address) and len(unit_id) and len(value):
            response = mbi.write_modbus_register(client=self.master.client, value=int(value),
                                                 register=int(address), unit_id=int(unit_id))
            print(response)
        else:
            print('no address or unit_id or value')
