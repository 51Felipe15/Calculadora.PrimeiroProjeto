import tkinter as tk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("417x400")
        self.root.configure(bg="#a9a9a9")
        self.root.resizable(True, True)  # Permitir redimensionamento da janela

        # Tela de entrada (Display)
        self.resultado_var = tk.StringVar()

        # Validação para permitir apenas números, operadores e caracteres permitidos
        vcmd = (self.root.register(self.validar_entrada), '%P')

        # Display (Entrada) com fundo escuro e texto branco
        self.resultado_entry = tk.Entry(self.root, textvariable=self.resultado_var, font=("Arial", 16), 
                                        fg="white", bg="#000000", bd=10, relief="sunken", justify="right", 
                                        validate="key", validatecommand=vcmd)
        self.resultado_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Botões da calculadora
        botoes = [
            ("C", 1, 0),  ("7", 1, 1), ("8", 1, 2), ("9", 1, 3), ("/", 1, 4),
            ("√", 2, 0),  ("4", 2, 1), ("5", 2, 2), ("6", 2, 3), ("*", 2, 4),
            ("^", 3, 0),  ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("-", 3, 4),
            ("π", 4, 0),  (".", 4, 1), ("0", 4, 2), ("=", 4, 3), ("+", 4, 4)
        ]

        # Criação dos botões com ajuste para redimensionamento
        for (texto, linha, coluna) in botoes:
            tk.Button(self.root, text=texto, width=3, height=2, font=("Arial", 16), 
                      bg="#000000", fg="white", activebackground="#993399", 
                      relief="raised", bd=2, 
                      command=lambda t=texto: self.botao_click(t)).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

        # Permite que a janela redimensione os widgets corretamente
        self.root.grid_rowconfigure(0, weight=1)  # Row para o display
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

    def validar_entrada(self, valor):
        """Permite apenas números, operadores e caracteres permitidos."""
        if valor == "":  # Permite apagar
            return True
        # Verifica se o valor é um número, operador ou ponto
        if valor[-1].isdigit() or valor[-1] in "+-*/^√.π":
            return True
        return False

    def botao_click(self, texto):
        """Função chamada quando um botão é pressionado."""
        if texto == "C":
            self.limpar()
        elif texto == "=":
            self.calcular()
        elif texto == "√":
            self.calcular_raiz()
        elif texto == "π":
            self.resultado_var.set(self.resultado_var.get() + str(math.pi))
        else:
            if self.resultado_var.get() == "ERRO":
                self.resultado_var.set("")
            self.resultado_var.set(self.resultado_var.get() + texto)

    def limpar(self):
        """Limpa a tela."""
        self.resultado_var.set("")

    def calcular(self):
        """Calcula a expressão no campo de entrada."""
        try:
            expressao = self.resultado_var.get()
            expressao = expressao.replace("^", "**")
            resultado = eval(expressao)
            self.resultado_var.set(resultado)
        except Exception:
            self.resultado_var.set("ERRO")

    def calcular_raiz(self):
        """Calcula a raiz quadrada do valor no campo de entrada."""
        try:
            valor = float(self.resultado_var.get())
            resultado = math.sqrt(valor)
            self.resultado_var.set(resultado)
        except Exception:
            self.resultado_var.set("ERRO")

# Configura a janela principal
root = tk.Tk()
calculadora = Calculadora(root)

# Exibe a janela
root.mainloop()
