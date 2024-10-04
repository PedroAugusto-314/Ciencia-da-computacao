import customtkinter as ctk
from calculadora import calculadora

class Calculadora_frame():
    def __init__(self, master) -> None:
        self.placed = False

        self.frame = ctk.CTkFrame(master=master, width=520, height=320)

        ctk.CTkLabel(master=self.frame, text="Calculadora binária",font=("Comic Sans MS", 21)).place(x=170,y=5)

        self.operador_cbox = ctk.CTkOptionMenu(master=self.frame, values=('Soma','Subtração','Multiplicação'),
                                               dynamic_resizing=True, font=('Comic Sans MS', 16), width=130,
                                                fg_color='#484c4d', button_color='#484c4d')
        self.operador_cbox.place(x=195,y=40)

        ctk.CTkLabel(master=self.frame, text="Primeiro número", font=("Comic Sans MS", 15)).place(x=100, y=75)
        self.num1_entry = ctk.CTkEntry(master=self.frame)
        self.num1_entry.place(x=90,y=100)

        ctk.CTkLabel(master=self.frame, text="Segundo número", font=("Comic Sans MS", 15)).place(x=300, y=75)
        self.num2_entry = ctk.CTkEntry(master=self.frame)
        self.num2_entry.place(x=290,y=100)

        self.resulta_btn = ctk.CTkButton(master=self.frame, text='Calcular', 
                                         command=self.mostrar_resultado,
                                         width=60)
        self.resulta_btn.place(x=230,y=140)

        self.resultado_label = ctk.CTkLabel(master=self.frame, text='Resultado', fg_color='gray',
                                            corner_radius=10, width= 150, font=('Roboto', 16)) 
        self.resultado_label.place(x=185, y=190)

    def show(self) -> None:
        self.frame.place(x=120,y=15) 
        self.placed = True

    def hide(self) -> None:
        self.frame.place_forget()
        self.placed = False
    
    def _get_operador(self):
        match self.operador_cbox.get():
            case 'Soma': return '+'
            case 'Subtração': return '-'
            case 'Multiplicação': return '*'

    def _get_valor1(self):
        return self.num1_entry.get()
    def _get_valor2(self):
        return self.num2_entry.get()
    def executar_operacao(self):
        operacao = self._get_operador()
        if operacao == "*": return calculadora.multi(self._get_valor1(), self._get_valor2())
        else: return calculadora.soma_sub_bin(self._get_valor1(),self._get_valor2(), operacao)

    def mostrar_resultado(self,event=None):
        self.resultado_label.configure(text=self.executar_operacao())
