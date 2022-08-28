import re

class Cliente:

    #Variaveis de Objeto:
    def __init__(self, nomeC, enderecoC, cpfC):
        self.nome     = nomeC
        self.endereco = enderecoC
        self.cpf      = cpfC

    @property
    def get_Cpf(self):
        return self.cpf

    def validaCpf(self, cpfAnalise):

        cpf_Entrada_Em_String = re.split("[.-]", cpfAnalise)

        cpf_Entrada_Em_Int = list(map(int, cpf_Entrada_Em_String))
        cpf_Saida = cpf_Entrada_Em_Int[:9]

        soma = 0
        multiplicador = 10
        for i in cpf_Saida:
            soma += i * multiplicador
            multiplicador -= 1

        if ((soma % 11) < 2):
            cpf_Saida.append(0)
        else:
            cpf_Saida.append(11 - (soma % 11))

        soma = 0
        multiplicador = 11
        for i in cpf_Saida:
            soma += i * multiplicador
            multiplicador -= 1

        if ((soma % 11) < 2):
            cpf_Saida.append(0)
        else:
            cpf_Saida.append(11 - (soma % 11))

        if (cpf_Saida == cpf_Entrada_Em_Int):
            print("O CPF {} do cliente {} não válido!".format(cpfAnalise, self.nome))
        else:
            print("O CPF {} do cliente {} não invalido!".format(cpfAnalise, self.nome))