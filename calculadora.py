import tkinter as tk

class calculadora:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculadora") # Título da janela
        self.root.geometry("380x400") # Tamanha da janela
        self.root.configure(bg="#f0f0f0")
        self.root.overrideredirect(False) # Remove a barra de título da janela
        self.root.attributes("-topmost", True) #deixa a janela sempre no topo

        # Tela de entrada
        self.resultado_var = tk.StringVar()
        self.resultado_entry = tk.Entry(self.root, textvariable=self.resultado_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.resultado_entry.grid(row=0, column=0, columnspan=4)

        # Botoes da calculadora
        botoes = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (texto, linha, coluna) in botoes:
            tk.Button(self.root, text=texto, width=5, height=2, font=("Arial", 20), command=lambda t=texto: self.botao_click(t)).grid(row=linha, column=coluna)

    def botao_click(self, texto):
        current = self.resultado_var.get()
        if texto == "=":
           try:
               resultado = eval(current) # Avalia a expressão matemática
               self.resultado_var.set(resultado)
           except Exception as e:
               self.resultado_var.set("ERRO")
        else:
            self.resultado_var.set(current + texto)
    def fechar(self):
        self.root.quit()

#configura a janela principal
root = tk.Tk()
calculadora = calculadora(root)

# Exibe a janela
root.mainloop()