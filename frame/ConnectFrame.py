import customtkinter as ctk
from pymodbus.client import ModbusSerialClient
from utils.constants import *
from widgets import CommonCTkButton, CommonCTkEntry, CommonCTkComboBox
import frame.MainFrame as MainFrame
from serial.tools import list_ports
from utils.Utils import Utils

class ConnectFrame(MainFrame.MainFrame):

    def __init__(self, master):
        MainFrame.MainFrame.__init__(self, master)
        validate_command = self.register(Utils.validate_digit_input)

        #############
        self.port_combo_box_frame = ctk.CTkFrame(master=self, width=250,height=38)
        self.port_combo_box_frame.configure(border_width=1, border_color=ORANGE,fg_color='#343638')
        self.port_combo_box_frame.grid(row=0, column=1, sticky='w', padx=10, pady=(20, 10))

        self.port_label = ctk.CTkLabel(self, text="Порт:", text_color=ORANGE,
                                       font=('Roboto', 16, 'bold', 'italic'))
        self.port_label.grid(row=0, column=0, padx=10, pady=(20, 10))
        self.port_combo_box = CommonCTkComboBox.CommonCTkComboBox(master=self.port_combo_box_frame,  command=self.pick_port)
        self.port_combo_box.grid(row=0, column=0, sticky='w', padx=2, pady=2)

        self.update_ports()
        self.update_port_button = CommonCTkButton.CommonCTkButton( border_color=ORANGE,master=self, text='Обновить порты',

                                                                  command=self.update_ports)
        self.update_port_button.grid(row=0, column=2, padx=10, pady=(20, 10))

        self.connect_button = CommonCTkButton.CommonCTkButton(master=self, text='Подключиться',
                                                              state='disabled', border_color='#999999',
                                                              command=self.connect_client)
        self.connect_button.grid(row=0, column=23, padx=10, pady=(20, 10))
        #############
        self.speed_label = ctk.CTkLabel(self, text="Скорость:", text_color=ORANGE,
                                        font=('Roboto', 16, 'bold', 'italic'))
        self.speed_label.grid(row=1, column=0, padx=10, pady=(20, 10))
        self.speed_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='скорость', width=250)
        self.speed_entry.grid(row=1, column=1, sticky='w', padx=10, pady=(20, 10))
        self.speed_entry.configure(validate='key',validatecommand=(validate_command, '%P'))
        self.speed_entry.insert(0, '9600')
        #############
        self.stop_bit_label = ctk.CTkLabel(self, text="Стоп-бит:", text_color=ORANGE,
                                           font=('Roboto', 16, 'bold', 'italic'))
        self.stop_bit_label.grid(row=2, column=0, padx=10, pady=(20, 10))
        self.stop_bit_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='стоп-бит', width=250)
        self.stop_bit_entry.grid(row=2, column=1, sticky='w', padx=10, pady=(20, 10))
        self.stop_bit_entry.configure(validate='key',validatecommand=(validate_command, '%P'))
        self.stop_bit_entry.insert(0, '1')
        #############
        self.byte_size_label = ctk.CTkLabel(self, text="Размер байта:", text_color=ORANGE,
                                            font=('Roboto', 16, 'bold', 'italic'))
        self.byte_size_label.grid(row=3, column=0, padx=10, pady=(20, 10))
        self.byte_size_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='размер байт', width=250)
        self.byte_size_entry.configure(validate='key',validatecommand=(validate_command, '%P'))
        self.byte_size_entry.grid(row=3, column=1, sticky='w', padx=10, pady=(20, 10))
        self.byte_size_entry.insert(0, '8')
        #############
        self.paritet_label = ctk.CTkLabel(self, text="Паритет:", text_color=ORANGE,
                                          font=('Roboto', 16, 'bold', 'italic'))
        self.paritet_label.grid(row=4, column=0, padx=10, pady=(20, 10))
        self.paritet_entry = CommonCTkEntry.CommonCTkEntry(master=self, placeholder_text='паритет', width=250)
        self.paritet_entry.grid(row=4, column=1, sticky='w', padx=10, pady=(20, 10))
        self.paritet_entry.insert(0, 'N')

    def update_ports(self):
        ports = [port.device for port in list_ports.comports()]
        if ports:
            self.port_combo_box.configure(values=ports)
            self.port_combo_box.set('выберите устройство')
            if hasattr(self, "connect_button"):  # Проверяем, что connect_button уже существует
                self.connect_button.configure(state='disabled', border_color='#999999')

        else:
            self.port_combo_box.set('устройства отсутствуют')
            self.port_combo_box.configure(values=[])
            if hasattr(self, "connect_button"):  # Проверяем, что connect_button уже существует
                self.connect_button.configure(state='disabled', border_color='#999999')

    def connect_client(self):
        if self.master.client is not None:
            self.master.client.close()
            self.master.client = None
            print("Соединение разорвано!")
            self.connect_button.configure(border_color=GREEN, text_color=GREEN, text='Подключиться')
            self.port_combo_box.configure(state='normal')
            self.update_port_button.configure(state='normal', text_color=ORANGE, border_color=ORANGE)

        else:
            try:
                port = self.port_combo_box.get()

                if not port or port not in self.port_combo_box.cget('values'):
                    raise ValueError("Не выбран порт!")

                self.master.client = ModbusSerialClient(
                    # method="rtu",
                    port=port,
                    baudrate=int(self.speed_entry.get()),
                    stopbits=int(self.stop_bit_entry.get()),
                    bytesize=int(self.byte_size_entry.get()),
                    parity=self.paritet_entry.get(),
                    timeout=1
                )
                if self.master.client.connect():
                    print("Успешное соединение с Modbus устройством!")
                    self.connect_button.configure(text_color=RED, border_color=RED, text='Отключиться')
                    self.port_combo_box.configure(state='disabled')
                    self.update_port_button.configure(border_color='#999999', text_color='#999999',
                                                      state='disabled')
                else:
                    print("Не удалось подключиться к устройству.")
            except Exception as e:
                print(f"Ошибка подключения: {str(e)}")

    def pick_port(self, event):
        if event in self.port_combo_box.cget('values'):
            self.connect_button.configure(border_color=GREEN, text_color=GREEN, state='normal')
