import customtkinter as ctk
from conversor import conversoes

class Conversor_Frame():
    
    def __init__(self, master) -> None:
        options = ("Binário", "Decimal", "Octal", "Hexadecimal")
        self.placed = False

        self.frame = ctk.CTkFrame(master=master, width=520, height=320)

        ctk.CTkLabel(master=self.frame, text="Conversor de base",font=("Comic Sans MS", 21)).place(x=175,y=5)
        ctk.CTkLabel(master=self.frame, text="De",font=("Comic Sans MS", 18)).place(x=150,y=35)
        ctk.CTkLabel(master=self.frame, text="Para",font=("Comic Sans MS", 18)).place(x=330,y=35)

        self.conversor1_cbox = ctk.CTkOptionMenu(values=options, master=self.frame, fg_color='#484c4d', button_color='#484c4d')
        self.conversor1_cbox.place(x=90,y=65)

        self.conversor2_cbox = ctk.CTkOptionMenu(values=options, master=self.frame, fg_color='#484c4d', button_color='#484c4d')
        self.conversor2_cbox.place(x=290,y=65)
        self.conversor2_cbox.set(options[1])

        ctk.CTkLabel(master=self.frame, text="Digite o número a ser convertido",font=("Comic Sans MS", 11)).place(x=180,y=95)
        self.numero_entry = ctk.CTkEntry(master=self.frame)
        self.numero_entry.place(x=190, y=120)

        self.converter_btn = ctk.CTkButton(master=self.frame, command=self.execute_function, text="Converter", font=("Roboto",15), width=60)
        self.converter_btn.place(x=220,y=160)


        self.resultado_label = ctk.CTkLabel(master=self.frame, text='Resultado', fg_color='gray',
                                            corner_radius=10, width= 150, font=('Roboto', 16)) 
        self.resultado_label.place(x=185, y=200)
        

    def show(self) -> None:
        self.frame.place(x=120,y=15) 
        self.placed = True

    def hide(self) -> None:
        self.frame.place_forget()
        self.placed = False

    def _get_conversor1(self) -> str:
        return self.conversor1_cbox.get()
    
    def _get_conversor2(self) -> str:
        return self.conversor2_cbox.get()

    def _get_numero(self) -> str:
        return self.numero_entry.get()

    def teste(self, event=None) -> None:
        print(self._get_conversor1(),self._get_conversor2(),self._get_numero())

    def _choice_function(self):
        b_i = self._get_conversor1()
        b_f = self._get_conversor2()
        if b_i == b_f: return None
        if b_i == "Decimal": return conversoes.convert_dec
        if b_f == "Decimal": return conversoes.convert_to_dec 
        if (b_i == "Octal" or b_i == "Hexadecimal") and (b_f == "Hexadecimal" or b_f == "Octal"): return conversoes.convert_hex_oct
        if b_i == "Binário" and (b_f == "Hexadecimal" or b_f == "Octal"): return conversoes.convert_bin
        if b_f == "Binário" and (b_i == "Hexadecimal" or b_i == "Octal"): return conversoes.convert_to_bin
           
    def _choice_base(self) -> int:
        base_inicial = self._get_conversor1()
        base_final = self._get_conversor2()
        
        match base_inicial:
            case "Octal":base_i = 8
            case "Binário":base_i = 2
            case "Hexadecimal":base_i = 16
            case "Decimal":base_i = 10

        match base_final:
            case "Octal":base_f = 8
            case "Binário":base_f = 2
            case "Hexadecimal":base_f = 16
            case "Decimal":base_f = 10

        return (base_i,base_f)
    
    def execute_function(self,event=None) -> None:
        funcao_converter = self._choice_function()
        base_i = self._choice_base()[0]
        base_f = self._choice_base()[1]
        numero = self._get_numero()
        match funcao_converter:
            case conversoes.convert_dec: num_conv = funcao_converter(numero,base_f)
            case conversoes.convert_to_dec: num_conv = funcao_converter(numero,base_i)
            case conversoes.convert_to_bin: num_conv = funcao_converter(numero,base_i)
            case conversoes.convert_bin: num_conv = funcao_converter(numero,base_f)
            case conversoes.convert_hex_oct: num_conv = funcao_converter(numero,base_i,base_f)
            case None: num_conv = numero
        self.resultado_label.configure(text=num_conv)
