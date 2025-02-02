import customtkinter as ctk
import tkinter
from frame import ConnectFrame, HandFrame, SideFrame, TopFrame, VFDSettingFrame, SnailFrame, VFDControlFrame
from utils.DBConnect import DBConnect
from utils.constants import TRANSPARENT_ACTIVE_BUTTON
from utils.global_variables import global_variables


class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('CNC FORGING')
        self.resizable(True, True)
        self.geometry('1000x600')
        self.iconbitmap('theme/img/hammer.ico')
        self.configure(padx=10, pady=10)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('theme/dark-blue.json')
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, weight=1)
        self.client = None
        self.db_connection = DBConnect.get_db('db/identifier.sqlite')
        ######################################################################################
        self.top_frame = TopFrame.TopFrame(self)
        ######################################################################################
        self.current_button = None
        self.side_frame = SideFrame.SideFrame(self)
        ######################################################################################
        self.current_frame = None

        # self.current_button = global_variables['active']
        self.frames = {}  # Пустой словарь для фреймов
        self.show('connect_frame')

    def show(self, frame_name, button_object=None):
        print(self.client, 'this mainui')
        # Проверяем, создан ли фрейм. Если нет — создаём
        if frame_name not in self.frames:
            match frame_name:
                case 'connect_frame':
                    self.frames[frame_name] = ConnectFrame.ConnectFrame(self)
                case 'hand_frame':
                    self.frames[frame_name] = HandFrame.HandFrame(self)
                case 'volt_frame':
                    self.frames[frame_name] = VFDSettingFrame.VFDSettingFrame(self)
                case 'snail_frame':
                    self.frames[frame_name] = SnailFrame.SnailFrame(self)
                case 'control_frame':
                    self.frames[frame_name] = VFDControlFrame.VFDControlFrame(self)

        # Меняем текущий фрейм
        new_frame = self.frames[frame_name]
        if self.current_frame != new_frame:
            if self.current_frame is not None:
                self.current_frame.grid_remove()
            self.current_frame = new_frame
            self.current_frame.grid(row=1, column=1, sticky='nsew')
        if button_object is not None:
            if self.current_button is not None:
                self.current_button.configure(fg_color='transparent')
            self.current_button = button_object
            self.current_button.configure(fg_color=TRANSPARENT_ACTIVE_BUTTON)
