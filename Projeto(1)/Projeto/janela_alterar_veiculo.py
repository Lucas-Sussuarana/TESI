import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd


class Alterar_Dados_Veiculo:
    def __init__(self, master, id, nome, cpf, modelo, placa, cor, ano, combustivel, tipo, especie, nacionalidade, uf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.tipo = tipo
        self.especie = especie
        self.nacionalidade = nacionalidade
        self.uf = uf
        self.janela_alterar_veiculo = master
        self.janela_alterar_veiculo.title("Alterar Dados de Veiculos")
        # self.janela1.resizable(False, False)

        # Containers
        self.container_0 = tk.Frame(self.janela_alterar_veiculo, bg='#f1c15d')  # , bg='#e6e6e6'
        self.container_1 = tk.Frame(self.janela_alterar_veiculo, bg='#00c9d2')
        self.container_2 = tk.Frame(self.janela_alterar_veiculo)
        self.container_3 = tk.Frame(self.janela_alterar_veiculo, bg='#00c9d2')
        self.container_4 = tk.Frame(self.janela_alterar_veiculo, bg='#e6e6e6')
        self.container_5 = tk.Frame(self.container_2, bg='#e6e6e6')
        self.container_6 = tk.Frame(self.container_2, bg='#e6e6e6')
        self.container_esquerdo = tk.Frame(self.janela_alterar_veiculo, bg='#a8ab9b')  # highlightbackground="black",highlightthickness=10
        self.container_direito = tk.Frame(self.janela_alterar_veiculo, bg='#a8ab9b')
        self.container_inferior = tk.Frame(self.janela_alterar_veiculo, bg='#a8ab9b')

        self.container_esquerdo.pack(side=tk.LEFT, fill=tk.Y)
        self.container_direito.pack(side=tk.RIGHT, fill=tk.Y)
        self.container_inferior.pack(side=tk.BOTTOM, fill=tk.X)
        self.container_0.pack(side=tk.TOP, fill=tk.X)
        self.container_1.pack(side=tk.TOP, fill=tk.X)
        self.container_2.pack(side=tk.TOP, fill=tk.X)
        self.container_3.pack(side=tk.TOP, fill=tk.X)
        self.container_4.pack(side=tk.TOP, fill=tk.X)
        self.container_5.pack(side=tk.LEFT, fill=tk.X, ipadx=100, ipady=40)
        self.container_6.pack(side=tk.RIGHT, fill=tk.X, ipadx=100, ipady=40)

        # imagem bordas
        self.logo_l = tk.PhotoImage(file="lateral.png")
        self.lbl_logo_l = tk.Label(self.container_esquerdo, image=self.logo_l, relief=tk.SOLID)
        self.lbl_logo_l.image = self.logo_l
        self.lbl_logo_l.pack()

        self.logo_dir = tk.PhotoImage(file="lateral.png")
        self.lbl_logo_dir = tk.Label(self.container_direito, image=self.logo_dir, relief=tk.SOLID)
        self.lbl_logo_dir.image = self.logo_dir
        self.lbl_logo_dir.pack()

        self.logo_i = tk.PhotoImage(file="retraido.png")
        self.lbl_logo_i = tk.Label(self.container_inferior, image=self.logo_i, relief=tk.SOLID)
        self.lbl_logo_i.image = self.logo_i
        self.lbl_logo_i.pack(side=tk.BOTTOM)

        self.lbl_logo_0 = tk.Label(self.container_0, text='APLICAÇÃO DE TABULAÇÃO E INFORMAÇÃO DE SERVIÇOS', font=('Rockwell Extra Bold', 20, 'bold'), bg='#f1c15d')
        self.lbl_logo_0.pack(side=tk.LEFT, ipady=20)

        # LBL para margem
        self.lbl_margem_L = tk.Label(self.container_esquerdo, text='', bg='#a8ab9b')
        self.lbl_margem_L.pack(pady=65, padx=65)
        self.lbl_margem_R = tk.Label(self.container_direito, text='', bg='#a8ab9b')
        self.lbl_margem_R.pack(pady=65, padx=65)
        self.lbl_titulo = tk.Label(self.container_1, text='ALTERAR DADOS SOBRE UM VEICULO', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_titulo.pack()

        # Entrys & Labels
        '''

        Aqui fazemos as entrys e labels 
        para cada item necessario na triagem das informações

        '''
        # Nome do Cliente retornado
        self.lbl_cliente = tk.Label(self.container_5, text='Cliente:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cliente.grid(row=0, column=0, sticky=tk.E, ipadx=10, ipady=10)
        self.ent1_cliente = tk.Entry(self.container_5, width=28, font=('arial', 12))
        self.ent1_cliente.grid(row=0, column=1)

        # CPF do cliente retornado
        self.lbl_cpf = tk.Label(self.container_5, text='CPF:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cpf.grid(row=1, column=0)
        self.ent1_cpf = tk.Entry(self.container_5, width=28, font=('arial', 12))
        self.ent1_cpf.grid(row=1, column=1)

        # Modelo do veiculo
        self.lbl_modelo = tk.Label(self.container_5, text='Modelo:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_modelo.grid(row=2, column=0, sticky=tk.E, ipadx=10, ipady=10)
        self.ent1_modelo = tk.Entry(self.container_5, width=28, font=('arial', 12))
        self.ent1_modelo.grid(row=2, column=1)

        # Placa do veiculo
        self.lbl_placa = tk.Label(self.container_5, text='Placa:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_placa.grid(row=3, column=0)

        self.lbl_ponto = tk.Label(self.container_5, text='          -', font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_ponto.grid(row=3, column=1, sticky=tk.W)
        self.ent1_placa = tk.Entry(self.container_5, width=4, font=('arial', 12))
        self.ent1_placa.grid(row=3, column=1, sticky=tk.W)
        self.ent1_ponto = tk.Entry(self.container_5, width=4, font=('arial', 12))
        self.ent1_ponto.grid(row=3, column=1, sticky=tk.W, padx=50)

        # Cor do veiculo
        self.lbl_cor = tk.Label(self.container_5, text='Cor:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cor.grid(row=4, column=0, sticky=tk.E, ipadx=10, ipady=10)

        self.v = tk.StringVar
        lista_cores = ['', 'BRANCO', 'PRETO', 'AZUL', 'LARANJA', 'AMARELO', 'ROXO', 'VERMELHO', 'PRATA', 'DOURADO',
                       'CINZA', 'MARROM', 'CYANO', 'VERDE']
        self.cbx = ttk.Combobox(self.container_5, font=('arial', 12, 'bold'))
        self.cbx['values'] = (
        '', 'BRANCO', 'PRETO', 'AZUL', 'LARANJA', 'AMARELO', 'ROXO', 'VERMELHO', 'PRATA', 'DOURADO', 'CINZA', 'MARROM',
        'CYANO', 'VERDE')
        self.cbx.current(0)
        self.cbx.grid(row=4, column=1, ipadx=16, sticky=tk.W)
        self.test = self.cbx.get()

        # Ano do modelo do veiculo
        self.lbl_ano = tk.Label(self.container_5, text='Ano/Mod:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_ano.grid(row=5, column=0)
        self.ent_ano = tk.Entry(self.container_5, width=24, font=('arial', 12))
        self.ent_ano.grid(row=5, column=1, ipadx=16, sticky=tk.W)

        self.lbl_nacionalidade = tk.Label(self.container_6, text='Combustivel:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_nacionalidade.grid(row=0, column=0, ipadx=10, ipady=10)
        self.combustivel = tk.StringVar
        self.cbx_combustivel = ttk.Combobox(self.container_6, font=('arial', 12, 'bold'))
        self.cbx_combustivel['values'] = ('', 'GASOLINA', 'DIESEL', 'ALCOOL', 'GAS NATURAL', 'BIO DIESEL', 'OUTRO')
        self.cbx_combustivel.current(0)
        self.cbx_combustivel.grid(row=0, column=1, ipadx=16)

        self.lbl_tipo = tk.Label(self.container_6, text='Tipo:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_tipo.grid(row=1, column=0)
        self.tipo = tk.StringVar
        self.cbx_tipo = ttk.Combobox(self.container_6, font=('arial', 12, 'bold'))
        self.cbx_tipo['values'] = (
        '', 'CICLOMOTOR', 'MOTOCICLETA', 'TRICICLO', 'QUADRICICLO', 'MICRO ONIBUS', 'REBOQUE', 'SEMI-REBOQUE',
        'MOTONETA', 'ONIBUS', 'AUTOMOVEL', 'CAMINHAO', 'CAMINHONETE', 'OUTRO')
        self.cbx_tipo.current(0)
        self.cbx_tipo.grid(row=1, column=1, ipadx=16)

        self.lbl_especie = tk.Label(self.container_6, text='Especie:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_especie.grid(row=2, column=0, ipadx=10, ipady=10)
        self.especie = tk.StringVar
        self.cbx_especie = ttk.Combobox(self.container_6, font=('arial', 12, 'bold'))
        self.cbx_especie['values'] = ('', 'PASSAGEIRO', 'CARGA', 'MISTO', 'COMPETICAO', 'TRACAO', 'OUTRO')
        self.cbx_especie.current(0)
        self.cbx_especie.grid(row=2, column=1, ipadx=16)

        self.lbl_nacionalidade = tk.Label(self.container_6, text='Nacionalidade:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_nacionalidade.grid(row=3, column=0)
        self.nacionalidade = tk.StringVar
        self.cbx_nacionalidade = ttk.Combobox(self.container_6, font=('arial', 12, 'bold'))
        self.cbx_nacionalidade['values'] = ('', 'NACIONAL', 'IMPORTADO')
        self.cbx_nacionalidade.current(0)
        self.cbx_nacionalidade.grid(row=3, column=1, ipadx=16)

        self.lbl_uf = tk.Label(self.container_6, text='UF do Veiculo:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_uf.grid(row=4, column=0, ipadx=10, ipady=10)
        self.unidade = tk.StringVar
        self.cbx_unidade = ttk.Combobox(self.container_6, font=('arial', 12, 'bold'))
        self.cbx_unidade['values'] = (
        '', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
        'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')
        self.cbx_unidade.current(0)
        self.cbx_unidade.grid(row=4, column=1, ipadx=16)

        self.lbl_obs = tk.Label(self.container_3, text='OBSERVAÇÕES', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_obs.grid(row=1, column=0)

        # Painel de avisos
        self.lbl_controle_aviso = tk.Label(self.container_4, text='                                     ',
                                           font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_controle_aviso.pack()

        self.lbl_aviso_0 = tk.Label(self.container_4, text='PREENCHA CORRETAMENTE CADA UM DOS CAMPOS',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_0.pack()

        self.lbl_aviso_1 = tk.Label(self.container_4,
                                    text='CASO A PLACA SEJA DO MERCOSUL, O SISTEMA O ACEITARA NORMALMENTE',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_1.pack()

        self.lbl_aviso_2 = tk.Label(self.container_4,
                                    text='UM VEICULO QUE SE ENQUADRA EM 2 OU MAIS CATEGORIAS PODE SER ENQUADRADO NAQUELE QUE MELHOR O DESCREVE',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_2.pack()

        self.lbl_aviso_3 = tk.Label(self.container_4, text='SERA ADICIONADO SOMENTE UM UNICO VEICULO POR VEZ!',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_3.pack()

        self.lbl_aviso_3 = tk.Label(self.container_4,
                                    text='CASO A COR NÃO ESTEJA DISPONIVEL, SELECIONE AQUELA QUE MAIS SE APROXIMA DA VERIFICADA!',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_3.pack()

        self.lbl_aviso_3 = tk.Label(self.container_4,
                                    text='SE POR ACASO O VEICULO FOR IMPORTADO, NÃO ESQUEÇA DE REGISTRAR ISSO NA O.S!',
                                    font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_aviso_3.pack()

        self.lbl_controle_aviso_1 = tk.Label(self.container_4, text='                                     ',
                                             font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_controle_aviso_1.pack()

        self.lbl_controle_aviso_2 = tk.Label(self.container_4, text='                                     ',
                                             font=('arial', 12, 'bold'), bg='#e6e6e6')
        self.lbl_controle_aviso_2.pack()



        '''
        Inserção das caracteristicas informadas
        '''

        self.ent1_cliente.insert('end', nome)
        self.ent1_cpf.insert('end', cpf)
        self.ent1_modelo.insert(1, modelo)

        #Repartição das placas para adicionar a cada entry distinto
        list_letra = []
        for i in self.placa[1]:
            list_letra.append(i)
        list_let = (list_letra[0] + list_letra[1] + list_letra[2])
        list_num = (list_letra[4] + list_letra[5] + list_letra[6] + list_letra[7])
        self.ent1_placa.insert('end', list_let)
        self.ent1_ponto.insert('end', list_num)
        self.placa_aux = (self.ent1_placa.get() + "-" + self.ent1_ponto.get())


        #Lista de cores
        lista_cor = self.cbx['values']
        list = lista_cor.index(cor)
        self.cbx.current(list)

        #Ano do Modelo
        self.ent_ano.insert('end', ano)


        # Lista de combustiveis
        lista_combustivel = self.cbx_combustivel['values']
        list_combustivel = lista_combustivel.index(combustivel)
        self.cbx_combustivel.current(list_combustivel)


        # Lista de Tipo
        lista_tipo = self.cbx_tipo['values']
        list_tipo = lista_tipo.index(tipo)
        self.cbx_tipo.current(list_tipo)

        # Lista de especie
        lista_especie = self.cbx_especie['values']
        list_especie = lista_especie.index(especie)
        self.cbx_especie.current(list_especie)

        # Lista de nacionalidade
        lista_nacionalidade = self.cbx_nacionalidade['values']
        list_nacionalidade = lista_nacionalidade.index(nacionalidade)
        self.cbx_nacionalidade.current(list_nacionalidade)

        # Lista de unidade
        lista_unidade = self.cbx_unidade['values']
        list_unidade = lista_unidade.index(uf)
        self.cbx_unidade.current(list_unidade)

        self.ent1_cliente.config(state='disabled')
        self.ent1_cpf.config(state='disabled')
        self.ent1_modelo.config(state='disabled')
        self.ent_ano.config(state='disabled')

        '''
    
        Aqui fazemos o banco de dados
        receber sa informações coletadas
        e registrar essas informações
    
        '''

        # BUTAO 2
        self.btn = tk.Button(self.container_6, text='GRAVAR', command=self.Inserir_informes)
        self.btn.grid(columnspan=2, sticky=tk.SE, ipadx=50)


    def Inserir_informes(self):
        if self.ent1_placa.get() == '' or self.ent1_ponto.get() == '' or self.ent1_modelo.get() == '' or self.cbx.get() == '' or self.ent_ano.get() == '' or self.cbx_combustivel.get() == '' or self.cbx_tipo.get() == '' or self.cbx_especie.get() == '' or self.cbx_nacionalidade.get() == '' or self.cbx_unidade.get() == '':
            messagebox.showinfo('ATENÇÃO', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        else:
            self.placa = (self.ent1_placa.get() + "-" + self.ent1_ponto.get())
            ano = self.ent_ano.get()
            modelo = self.ent1_modelo.get()
            placa = self.placa_aux
            placa_1 = self.placa
            cor = self.cbx.get()
            combustivel = self.cbx_combustivel.get()
            tipo = self.cbx_tipo.get()
            especie = self.cbx_especie.get()
            nacionalidade = self.cbx_nacionalidade.get()
            uf = self.cbx_unidade.get()

            sql_atualizar = f'UPDATE veiculo SET modelo="{modelo}", placa="{placa_1}", cor="{cor}", ano="{ano}", combustivel="{combustivel}", tipo="{tipo}", especie="{especie}", nacionalidade="{nacionalidade}", uf="{uf}" WHERE placa="{placa}";'
            bd.atualizar_id(sql_atualizar)
            messagebox.showinfo('Aviso', 'Informações do Veiculo Atualizadas com sucesso')
            self.janela_alterar_veiculo.destroy()
