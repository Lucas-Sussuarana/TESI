import re
from conta import Conta
from cliente import Cliente



class Banco:
    # Variaveis de Objeto
    def __init__(self, numeroC, nomeC):
        self._numero = numeroC
        self._nome = nomeC
        self._contas = []
        self._clientes = []
        self.transacoesBanco = Conta.transacoes_Banco()

    # Metodos de Objeto
    def add_Conta(self, contaAdd):
        if ((contaAdd in self._contas) == False):
            self._contas.append(contaAdd)
            print("Conta N°: 000{} adicionada com sucesso!".format(contaAdd.get_Numero))
        else:
            print("Operação invalida: Conta N°: 000{} já está no banco!!".format(contaAdd.get_Numero))

    def remove_Conta(self, contaRemove):
        if ((contaRemove in self._contas) == True):
            self._contas.remove(contaRemove)
            print("Conta N°: 000{} removida com sucesso! ;-;".format(contaRemove.get_Numero))
        else:
            print("Operação invalida: Conta N°: 000{} não existe no banco!!".format(contaRemove.get_Numero))

    @property
    def lista_Contas(self):
        if (len(self._contas) != 0):
            print("Contas atualmente ativas:")
            for i in self._contas:
                print("Conta N°: 000{}".format(i.get_Numero))
        else:
            print("O banco {} ainda não possui nenhuma conta!".format(self._nome))

    @property
    def imprime(self):
        for i in self.transacoesBanco:
            print(i)
        for i in self.transacoesEmprestimo:
            print(i)
        print("Saldo Total do Banco: %.2f$" % (Conta.get_Total_Saldo_Banco()))

    def atualizarContas(self, taxa):
        for i in self._contas:
            i.atualiza(taxa)

    def get_contas(self):
        return self._contas

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_numero(self):
        return str(self._numero)

    def set_nome(self, newNome):
        self._nome = newNome

    def set_numero(self, newNumero):
        self._numero = newNumero

    def criar_cliente(self, nomeC, enderecoC, cpfC, senha):
        clienteAUX = Cliente(nomeC, enderecoC, cpfC, senha)
        self._clientes.append(clienteAUX)
        return clienteAUX

    @property
    def get_clientes(self):
        return self._clientes

