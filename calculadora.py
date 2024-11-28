import tkinter as tk
import math  # Importa a biblioteca para cálculos matemáticos

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")  # Título da janela
        self.root.geometry("417x400")  # Tamanho da janela
        self.root.configure(bg="#a9a9a9")  # Cor de fundo
        self.root.overrideredirect(False)  # Remove a barra de título da janela
        self.root.attributes("-topmost", True)  # Deixa a janela sempre no topo
        self.root.resizable(False, False)  # Impede o redimensionamento da janela

        # Tela de entrada (Display)
        self.resultado_var = tk.StringVar()

        # Validação para permitir apenas números, operadores e caracteres permitidos
        vcmd = (self.root.register(self.validar_entrada), '%P')

        # Aumento do tamanho da área de entrada, sem alterar a fonte
        self.resultado_entry = tk.Entry(self.root, textvariable=self.resultado_var, font=("Arial", 20), 
                                        bg="#000000", fg="white", bd=10, relief="sunken", justify="right",
                                        validate="key", validatecommand=vcmd, width=25)  # Aumentando o espaço
        self.resultado_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

        # Botões da calculadora com tamanho reduzido
        botoes = [
            ("C", 1, 0),  ("7", 1, 1), ("8", 1, 2), ("9", 1, 3), ("/", 1, 4),
            ("√", 2, 0),  ("4", 2, 1), ("5", 2, 2), ("6", 2, 3), ("*", 2, 4),
            ("^", 3, 0),  ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("-", 3, 4),
            ("π", 4, 0),  (".", 4, 1), ("0", 4, 2), ("=", 4, 3), ("+", 4, 4)
        ]

        # Criação dos botões com tamanho reduzido e com efeito de clique (mouse)
        for (texto, linha, coluna) in botoes:
            tk.Button(self.root, text=texto, width=3, height=2, font=("Arial", 16), 
                      bg="#000000", fg="white", activebackground="#993399", 
                      relief="raised", bd=2, 
                      command=lambda t=texto: self.botao_click(t)).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

        # Configura o clique do mouse para selecionar números no display
        self.resultado_entry.bind("<Button-1>", self.selecionar_entrada)

    def validar_entrada(self, valor):
        """Permite apenas números, operadores e caracteres permitidos, com limite de caracteres."""
        if valor == "":  # Permite apagar
            return True
        # Verifica se o valor é um número, operador ou ponto
        if valor[-1].isdigit() or valor[-1] in "+-*/^√.π":
            # Verifica se o número de caracteres não excede o limite
            if len(valor) <= 1000:  # Limite de caracteres
                return True
        return False

    def botao_click(self, texto):
        # Limpar a tela quando pressionado o botão "C"
        if texto == "C":
            self.limpar()
        # Calcular o resultado quando pressionado o botão "="
        elif texto == "=":
            self.calcular()
        # Calcular raiz quadrada quando pressionado o botão "√"
        elif texto == "√":
            self.calcular_raiz()
        # Inserir pi quando pressionado o botão "π"
        elif texto == "π":
            self.resultado_var.set(self.resultado_var.get() + str(math.pi))
        else:
            # Adiciona o texto ao campo de entrada
            if self.resultado_var.get() == "ERRO":
                self.resultado_var.set("")
            self.resultado_var.set(self.resultado_var.get() + texto)

    def limpar(self):
        """Limpa o campo de entrada."""
        self.resultado_var.set("")

    def calcular(self):
        """Calcula a expressão no campo de entrada."""
        try:
            expressao = self.resultado_var.get()
            # Substitui "^" por "**" para realizar a exponenciação no Python
            expressao = expressao.replace("^", "**")
            resultado = eval(expressao)  # Calcula a expressão
            self.resultado_var.set(resultado)
        except Exception:
            # Exibe mensagem de erro se a expressão for inválida
            self.resultado_var.set("ERRO")

    def calcular_raiz(self):
        """Calcula a raiz quadrada do valor no campo de entrada."""
        try:
            valor = float(self.resultado_var.get())
            resultado = math.sqrt(valor)  # Calcula a raiz quadrada
            self.resultado_var.set(resultado)
        except Exception:
            # Exibe mensagem de erro se a entrada for inválida
            self.resultado_var.set("ERRO")
    
    def selecionar_entrada(self, event):
        """Permite selecionar a entrada no display com o clique do mouse."""
        # Obtém o texto selecionado
        texto_selecionado = self.resultado_var.get()
        # Insere o texto selecionado no display ao clicar
        if texto_selecionado:
            self.resultado_var.set(texto_selecionado)

# Configura a janela principal
root = tk.Tk()
calculadora = Calculadora(root)

# Exibe a janela
root.mainloop()
