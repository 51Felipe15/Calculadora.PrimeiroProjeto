import tkinter as tk
import math
import re  # Para expressões regulares


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("417x400")
        self.root.configure(bg="#a9a9a9")
        self.root.resizable(True, True)

        # Variável para armazenar o valor do display
        self.resultado_var = tk.StringVar()

        # Configuração do display
        self.configurar_display()

        # Configuração dos botões
        self.configurar_botoes()

        # Configuração do layout responsivo
        self.configurar_layout()

    def configurar_display(self):
        """Configura o campo de entrada da calculadora."""
        vcmd = (self.root.register(self.validar_entrada), '%P')  # Validação do campo
        self.resultado_entry = tk.Entry(
            self.root,
            textvariable=self.resultado_var,
            font=("Arial", 16),
            fg="white",
            bg="#000000",
            bd=10,
            relief="sunken",
            justify="right",
            validate="key",
            validatecommand=vcmd,
        )
        self.resultado_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    def configurar_botoes(self):
        """Configura os botões da calculadora."""
        botoes = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("π", 1, 3), ("*", 1, 4),
            ("^", 2, 0), ("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("/", 2, 4),
            ("√", 3, 0), ("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("+", 3, 4),
            ("!", 4, 0), ("1", 4, 1), ("2", 4, 2), ("3", 4, 3), ("-", 4, 4),
            (" ", 5, 0), (" ", 5, 1), ("0", 5, 2), (".", 5, 3), ("=", 5, 4),
        ]

        for (texto, linha, coluna) in botoes:
            tk.Button(
                self.root,
                text=texto,
                width=3,
                height=2,
                font=("Arial", 16),
                bg="#000000",
                fg="white",
                activebackground="#993399",
                relief="raised",
                bd=2,
                command=lambda t=texto: self.botao_click(t),
            ).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

    def configurar_layout(self):
        """Configura o layout responsivo da calculadora."""
        for i in range(6):  # 5 linhas de botões + 1 linha para o display
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):  # 5 colunas
            self.root.grid_columnconfigure(i, weight=1)

    def validar_entrada(self, valor):
        """Permite apenas números, operadores e caracteres permitidos no display."""
        if valor == "":
            return True
        if valor[-1].isdigit() or valor[-1] in "+-*/^√.!π":
            return True
        return False

    def botao_click(self, texto):
        """Executa ações com base no botão pressionado."""
        if texto == "C":
            self.limpar()
        elif texto == "=":
            self.calcular()
        elif texto == "π":
            self.resultado_var.set(self.resultado_var.get() + str(math.pi))
        elif texto in "!√":
            self.resultado_var.set(self.resultado_var.get() + texto)
        else:
            if self.resultado_var.get() == "ERRO":
                self.resultado_var.set("")
            self.resultado_var.set(self.resultado_var.get() + texto)

    def limpar(self):
        """Limpa o display."""
        self.resultado_var.set("")

    def calcular(self):
        """Calcula a expressão no display, processando fatores especiais."""
        try:
            expressao = self.resultado_var.get()
            expressao = expressao.replace("^", "**")  # Substituir ^ por **

            # Processar operações especiais antes de avaliar
            expressao = self.processar_fatoriais(expressao)
            expressao = self.processar_raizes(expressao)

            resultado = eval(expressao)  # Avaliar a expressão resultante
            self.resultado_var.set(resultado)
        except Exception:
            self.resultado_var.set("ERRO")

    def processar_fatoriais(self, expressao):
        """Substitui expressões de fatoriais (!) pelos resultados."""
        padrao = r"(\d+)!+"
        correspondencias = re.finditer(padrao, expressao)

        for match in correspondencias:
            numero_str = match.group(1)
            numero = int(numero_str)

            if numero < 0:
                raise ValueError("Fatorial de número negativo não é definido")

            resultado = math.factorial(numero)
            expressao = expressao.replace(f"{numero_str}!", str(resultado), 1)

        return expressao

    def processar_raizes(self, expressao):
        """Substitui expressões de raiz quadrada (√) pelos resultados."""
        padrao = r"√(\d+)"
        correspondencias = re.finditer(padrao, expressao)

        for match in correspondencias:
            numero_str = match.group(1)
            numero = float(numero_str)

            if numero < 0:
                raise ValueError("Raiz quadrada de número negativo não é suportada")

            resultado = math.sqrt(numero)
            expressao = expressao.replace(f"√{numero_str}", str(resultado), 1)

        return expressao


# Configuração da janela principal
root = tk.Tk()
calculadora = Calculadora(root)

# Iniciar o loop principal da aplicação
root.mainloop()
