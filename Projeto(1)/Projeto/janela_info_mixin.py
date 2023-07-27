

class Janela_Info_Mixin():
    '''
    Fazemos o init teceber as informações necessarias
    '''
    def __init__(self, master):
        pass
        '''
        Colocamos container para definicao
        das bordas da janela
        
        '''

    def Atualizar_Tvw(self):
        for i in self.treview_janela.get_children():
            self.treview_janela.delete(i)

        for i in bd.consultar_tabela_obs(bd.sql_consulta_obs):
            lista = i
            aux = int(lista[0])
            aux1 = int(self.id)
            print(self.id)
            if aux == aux1:
                self.treview_janela.insert('', 'end', values=(i))