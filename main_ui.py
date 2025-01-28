import customtkinter as ctk
from frame import ConnectFrame, HandFrame, SideFrame, TopFrame


class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('CNC FORGING')
        self.resizable(True, True)
        self.geometry('1000x600')
        self.configure(padx=10, pady=10)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('theme/dark-blue.json')
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, weight=1)
        ######################################################################################
        self.top_frame = TopFrame.TopFrame(self)
        ######################################################################################
        self.side_frame = SideFrame.SideFrame(self)
        ######################################################################################
        self.current_frame = None
        self.frames = {}  # Пустой словарь для фреймов
        self.show('connect_frame')

    def show(self, frame_name):
        # Проверяем, создан ли фрейм. Если нет — создаём
        if frame_name not in self.frames:
            if frame_name == 'connect_frame':
                self.frames[frame_name] = ConnectFrame.ConnectFrame(self)
            elif frame_name == 'hand_frame':
                self.frames[frame_name] = HandFrame.HandFrame(self)

        # Меняем текущий фрейм
        new_frame = self.frames[frame_name]
        if self.current_frame != new_frame:
            if self.current_frame is not None:
                self.current_frame.grid_remove()
            self.current_frame = new_frame
            self.current_frame.grid(row=1, column=1, sticky='nsew')




