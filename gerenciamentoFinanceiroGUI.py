import tkinter as tk
from tkinter import messagebox, simpledialog

class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.receitas = []
        self.despesas = []

    def adicionar_receita(self, descricao, valor):
        self.receitas.append({'descricao': descricao, 'valor': valor})
        self.saldo += valor

    def adicionar_despesa(self, descricao, valor):
        self.despesas.append({'descricao': descricao, 'valor': valor})
        self.saldo -= valor

    def calcular_total_receitas(self):
        total = 0
        for receita in self.receitas:
            total += receita['valor']
        return total

    def calcular_total_despesas(self):
        total = 0
        for despesa in self.despesas:
            total += despesa['valor']
        return total

    def calcular_saldo_atual(self):
        return self.saldo

    def calcular_saldo_final(self):
        return self.saldo + self.calcular_total_receitas() - self.calcular_total_despesas()

    def calcular_ebitda(self):
        return self.calcular_total_receitas() - self.calcular_total_despesas()

    def calcular_dre(self):
        return self.calcular_total_receitas() - self.calcular_total_despesas()

    def calcular_fluxo_caixa(self):
        return self.calcular_total_receitas() - self.calcular_total_despesas()

    def calcular_indice_liquidez(self):
        return self.calcular_total_receitas() / self.calcular_total_despesas()

    def calcular_indice_seca(self):
        return self.calcular_total_receitas() / (self.calcular_total_despesas() - self.calcular_total_receitas())

    def calcular_indice_corrente(self):
        return self.calcular_total_receitas() / self.calcular_total_despesas()


class ContaGUI:
    def __init__(self):
        self.conta = Conta(0)

        self.root = tk.Tk()
        self.root.title("Controle Financeiro")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Controle Financeiro")
        self.label.pack()

        self.receita_button = tk.Button(self.root, text="Adicionar Receita", command=self.adicionar_receita)
        self.receita_button.pack()

        self.despesa_button = tk.Button(self.root, text="Adicionar Despesa", command=self.adicionar_despesa)
        self.despesa_button.pack()

        self.total_receitas_button = tk.Button(self.root, text="Calcular Total de Receitas", command=self.calcular_total_receitas)
        self.total_receitas_button.pack()

        self.total_despesas_button = tk.Button(self.root, text="Calcular Total de Despesas", command=self.calcular_total_despesas)
        self.total_despesas_button.pack()

        self.saldo_atual_button = tk.Button(self.root, text="Calcular Saldo Atual", command=self.calcular_saldo_atual)
        self.saldo_atual_button.pack()

        self.saldo_final_button = tk.Button(self.root, text="Calcular Saldo Final", command=self.calcular_saldo_final)
        self.saldo_final_button.pack()

        self.ebitda_button = tk.Button(self.root, text="Calcular EBITDA", command=self.calcular_ebitda)
        self.ebitda_button.pack()

        self.dre_button = tk.Button(self.root, text="Calcular DRE", command=self.calcular_dre)
        self.dre_button.pack()

        self.fluxo_caixa_button = tk.Button(self.root, text="Calcular Fluxo de Caixa", command=self.calcular_fluxo_caixa)
        self.fluxo_caixa_button.pack()

        self.indice_liquidez_button = tk.Button(self.root, text="Calcular Índice de Liquidez", command=self.calcular_indice_liquidez)
        self.indice_liquidez_button.pack()

        self.indice_seca_button = tk.Button(self.root, text="Calcular Índice Seca", command=self.calcular_indice_seca)
        self.indice_seca_button.pack()

        self.indice_corrente_button = tk.Button(self.root, text="Calcular Índice Corrente", command=self.calcular_indice_corrente)
        self.indice_corrente_button.pack()

    def adicionar_receita(self):
        descricao = simpledialog.askstring("Adicionar Receita", "Digite a descrição da receita:")
        valor = float(simpledialog.askstring("Adicionar Receita", "Digite o valor da receita:"))
        self.conta.adicionar_receita(descricao, valor)
        messagebox.showinfo("Adicionar Receita", "Receita adicionada com sucesso!")

    def adicionar_despesa(self):
        descricao = simpledialog.askstring("Adicionar Despesa", "Digite a descrição da despesa:")
        valor = float(simpledialog.askstring("Adicionar Despesa", "Digite o valor da despesa:"))
        self.conta.adicionar_despesa(descricao, valor)
        messagebox.showinfo("Adicionar Despesa", "Despesa adicionada com sucesso!")

    def calcular_total_receitas(self):
        total_receitas = self.conta.calcular_total_receitas()
        messagebox.showinfo("Total de Receitas", "Total de Receitas: {}".format(total_receitas))

    def calcular_total_despesas(self):
        total_despesas = self.conta.calcular_total_despesas()
        messagebox.showinfo("Total de Despesas", "Total de Despesas: {}".format(total_despesas))

    def calcular_saldo_atual(self):
        saldo_atual = self.conta.calcular_saldo_atual()
        messagebox.showinfo("Saldo Atual", "Saldo Atual: {}".format(saldo_atual))

    def calcular_saldo_final(self):
        saldo_final = self.conta.calcular_saldo_final()
        messagebox.showinfo("Saldo Final", "Saldo Final: {}".format(saldo_final))

    def calcular_ebitda(self):
        ebitda = self.conta.calcular_ebitda()
        messagebox.showinfo("EBITDA", "EBITDA: {}".format(ebitda))

    def calcular_dre(self):
        dre = self.conta.calcular_dre()
        messagebox.showinfo("DRE", "DRE: {}".format(dre))

    def calcular_fluxo_caixa(self):
        fluxo_caixa = self.conta.calcular_fluxo_caixa()
        messagebox.showinfo("Fluxo de Caixa", "Fluxo de Caixa: {}".format(fluxo_caixa))

    def calcular_indice_liquidez(self):
        indice_liquidez = self.conta.calcular_indice_liquidez()
        messagebox.showinfo("Índice de Liquidez", "Índice de Liquidez: {}".format(indice_liquidez))

    def calcular_indice_seca(self):
        indice_seca = self.conta.calcular_indice_seca()
        messagebox.showinfo("Índice Seca", "Índice Seca: {}".format(indice_seca))

    def calcular_indice_corrente(self):
        indice_corrente = self.conta.calcular_indice_corrente()
        messagebox.showinfo("Índice Corrente", "Índice Corrente: {}".format(indice_corrente))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    conta_gui = ContaGUI()
    conta_gui.run()
