import customtkinter as ctk
from ui.conversor_frame import Conversor_Frame
from ui.calculadora_frame import Calculadora_frame

class App():

    def __init__(self) -> None:
        self.frames = []
        self.root = ctk.CTk()
        self.root.geometry('700x400+550+200')
        self.root.title("Introdução à Programação Estruturada")
        self.root.resizable(False,False)

        self.main_label = ctk.CTkLabel(master=self.root, text="Atividades extras de Introdução à Programação Estruturada", 
                                       font=('Comic Sans MS', 16))
        self.main_label.place(x=140, y=10)

        self.main_frame = ctk.CTkFrame(master=self.root, width=650, height=350)
        self.main_frame.place(x=25, y=35)

        self.choice_frame = ctk.CTkFrame(master=self.main_frame, height=320, width=100)
        self.choice_frame.place(x=15,y=15)

        self.conversor_btn = ctk.CTkButton(master=self.choice_frame, text='Conversor', 
                                           width=80,command=self.conversor_btn_func)
        self.conversor_btn.place(x=10,y=10)

        self.conversor_frame = Conversor_Frame(master=self.main_frame)
        self.frames.append(self.conversor_frame)
        self.conversor_frame.show()

        self.calculadora_btn = ctk.CTkButton(master=self.choice_frame, text='Calculadora', 
                                             width=80, command=self.calculadora_btn_func)
        self.calculadora_btn.place(x=10,y=50)

        self.calculadora_frame = Calculadora_frame(master=self.main_frame)
        self.frames.append(self.calculadora_frame)
        # self.calculadora_frame.show()

        self.root.mainloop()


    def hide_all(self)->None:
        for frame in self.frames: 
            frame.hide()

    def conversor_btn_func(self, event = None) -> None:
        if not self.conversor_frame.placed: 
            self.hide_all()
            self.conversor_frame.show()
        else: self.conversor_frame.hide()

    def calculadora_btn_func(self, event = None) -> None:
        if not self.calculadora_frame.placed: 
            self.hide_all()
            self.calculadora_frame.show()
        else: self.calculadora_frame.hide()


