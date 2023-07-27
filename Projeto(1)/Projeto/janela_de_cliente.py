import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd
from janela_alterar_veiculo import Alterar_Dados_Veiculo
from janela_inserir_servico import Inserir_Servico
from janela_inserir_veiculo import Inserir_Veiculo


class Cliente:
    def __init__(self, master, id, nome, cpf, email, celular, vinculo):
        self.janela_de_clientes = master
        self.janela_de_clientes.title("Informações do Cliente")
        self.janela_de_clientes.minsize(400, 400)
        #self.janela_de_clientes.resizable(False, False)
        self.janela_de_clientes.grab_set()
        self.id = id
        self.nome = nome
        self.cpf = cpf


        # Containers
        self.container_left = tk.Frame(self.janela_de_clientes, bg='#a8ab9b')#highlightbackground="black",highlightthickness=10
        self.container_right = tk.Frame(self.janela_de_clientes, bg='#a8ab9b')
        self.container_botton = tk.Frame(self.janela_de_clientes, bg='#a8ab9b')
        self.container_1 = tk.Frame(self.janela_de_clientes, bg='#00c9d2')
        self.container_0 = tk.Frame(self.janela_de_clientes, bg='#f1c15d')
        self.container_4 = tk.Frame(self.janela_de_clientes, bg='#e6e6e6')
        self.container_5 = tk.Frame(self.janela_de_clientes, bg='#e6e6e6')
        self.container_7 = tk.Frame(self.container_4, bg='#e6e6e6')
        self.container_l1 = tk.Frame(self.container_7, bg='#e6e6e6')
        self.container_center = tk.Frame(self.container_7, bg='#e6e6e6')

        self.container_left.pack(side=tk.LEFT, fill=tk.Y)
        self.container_right.pack(side=tk.RIGHT, fill=tk.Y)
        self.container_botton.pack(side=tk.BOTTOM, fill=tk.X)
        self.container_0.pack(side=tk.TOP, fill=tk.X)
        self.container_1.pack(side=tk.TOP, fill=tk.X)
        self.container_4.pack(side=tk.LEFT, fill=tk.Y)
        self.container_5.pack(side=tk.RIGHT, fill=tk.Y, anchor=tk.E)
        self.container_7.grid(row=7, sticky=tk.E, ipadx=7, columnspan=2, ipady=70)
        self.container_center.pack(side=tk.TOP, fill=tk.X)
        self.container_l1.pack(side=tk.LEFT, anchor=tk.NE)


        #imagem bordas
        self.logo_1 = tk.PhotoImage(file="lateral.png")
        self.lbl_logo_1 = tk.Label(self.container_left, image=self.logo_1, relief=tk.SOLID)
        self.lbl_logo_1.image = self.logo_1
        self.lbl_logo_1.pack()

        self.logo_2 = tk.PhotoImage(file="lateral.png")
        self.lbl_logo_2 = tk.Label(self.container_right, image=self.logo_2, relief=tk.SOLID)
        self.lbl_logo_2.image = self.logo_2
        self.lbl_logo_2.pack()

        self.logo_3 = tk.PhotoImage(file="retraido.png")
        self.lbl_logo_3 = tk.Label(self.container_botton, image=self.logo_3, relief=tk.SOLID)
        self.lbl_logo_3.image = self.logo_3
        self.lbl_logo_3.pack(side=tk.BOTTOM)

        self.lbl_logo_0 = tk.Label(self.container_0, text='APLICAÇÃO DE TABULAÇÃO E INFORMAÇÃO DE SERVIÇOS', font=('    Rockwell Extra Bold', 20, 'bold'), bg='#f1c15d')
        self.lbl_logo_0.pack(side=tk.LEFT, ipady=20)


        # LBL para margem
        self.lbl_margem_L = tk.Label(self.container_left, text='', bg='#a8ab9b')
        self.lbl_margem_L.pack(pady=65, padx=65)
        self.lbl_margem_R = tk.Label(self.container_right, text='', bg='#a8ab9b')
        self.lbl_margem_R.pack(pady=65, padx=65)
        self.lbl_titulo = tk.Label(self.container_1, text='INFORMAÇÕES SOBRE O CLIENTE E SEUS VEICULOS', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_titulo.pack()

        # Treview de veiculos desse cliente
        colunas = ['id', 'placa', 'modelo', 'cor', 'ano']
        self.treview_cli_veiculo = ttk.Treeview(self.container_5, show='headings', columns=colunas, height=9)
        self.treview_cli_veiculo.grid(sticky=tk.NW, ipadx=10)

        # cabeçalho
        self.treview_cli_veiculo.heading('id', text="ID")
        self.treview_cli_veiculo.heading('placa', text="Placa")
        self.treview_cli_veiculo.heading('modelo', text="Modelo")
        self.treview_cli_veiculo.heading('cor', text="Cor")
        self.treview_cli_veiculo.heading('ano', text="Ano")


        self.treview_cli_veiculo.column('id', minwidth=0, width=0)
        self.treview_cli_veiculo.column('placa', minwidth=0, width=70)
        self.treview_cli_veiculo.column('modelo', minwidth=0, width=230)
        self.treview_cli_veiculo.column('cor', minwidth=0, width=90)
        self.treview_cli_veiculo.column('ano', minwidth=0, width=65)


        self.scr = ttk.Scrollbar(self.container_5, command=self.treview_cli_veiculo.yview)
        self.scr.grid(row=0,column=1, sticky=tk.NE, ipady=78)
        self.treview_cli_veiculo.configure(yscroll=self.scr.set)

        for i in bd.consultar_tabela_obs(bd.sql_consulta_obs):
            lista = i
            aux = int(lista[0])
            aux1 = int(id[1])
            if aux == aux1:
                self.treview_cli_veiculo.insert('', 'end', values=(i))

        self.treview_cli_veiculo.bind('<Double-1>', self.Info)

        # Labels da janela Top_Inserir_Veiculo
        self.lbl_id_v = tk.Label(self.container_4, text='ID:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_id_v.grid(row=0, column=0, ipadx=10, ipady=10)
        self.lbl_nome_v = tk.Label(self.container_4, text='Nome:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_nome_v.grid(row=1, column=0)
        self.lbl_cpf_v = tk.Label(self.container_4, text='CPF:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cpf_v.grid(row=2, column=0, ipadx=10, ipady=10)
        self.lbl_email = tk.Label(self.container_4, text='E-mail:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_email.grid(row=3, column=0)
        self.lbl_contato = tk.Label(self.container_4, text='Contato:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_contato.grid(row=4, column=0, ipadx=10, ipady=10)
        self.lbl_vinculo = tk.Label(self.container_4, text='Vinculo:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_vinculo.grid(row=5, column=0)

        #Entrys da janela Top_Inserir_Veiculo
        self.ent_id_v = tk.Entry(self.container_4, width=30, font=('arial', 10))
        self.ent_id_v.grid(row=0, column=1, sticky=tk.W)
        self.ent_nome_v = tk.Entry(self.container_4, width=40, font=('arial', 10))
        self.ent_nome_v.grid(row=1, column=1, sticky=tk.W)
        self.ent_cpf_v = tk.Entry(self.container_4, width=40, font=('arial', 10))
        self.ent_cpf_v.grid(row=2, column=1, sticky=tk.W)
        self.ent_email = tk.Entry(self.container_4, width=40, font=('arial', 10))
        self.ent_email.grid(row=3, column=1, sticky=tk.W)
        self.ent_contato = tk.Entry(self.container_4, width=40, font=('arial', 10))
        self.ent_contato.grid(row=4, column=1, sticky=tk.W)
        self.ent_vinculo = tk.Entry(self.container_4, width=40, font=('arial', 10))
        self.ent_vinculo.grid(row=5, column=1, sticky=tk.W)


        # ???
        self.ent_id_v.insert(0, id[1])
        self.ent_nome_v.insert(1, nome[1])
        self.ent_cpf_v.insert(1, cpf[1])
        self.ent_email.insert(0, email[1])
        self.ent_contato.insert(1, celular[1])
        self.ent_vinculo.insert(1, vinculo[1])
        self.ent_id_v.config(state='disabled')
        self.ent_nome_v.config(state='disabled')
        self.ent_cpf_v.config(state='disabled')
        self.ent_email.config(state='disabled')
        self.ent_contato.config(state='disabled')
        self.ent_vinculo.config(state='disabled')

        #Controle dos frames
        self.lbl = tk.Label(self.container_center, text='OPÇÕES DISPONIVEIS', bg='#00c9d2', font=('arial', 12, 'bold'))
        self.lbl.pack(fill=tk.X)
        self.lbl_control = tk.Label(self.container_l1, text='                                                      ', font=('arial', 10), bg='#e6e6e6')
        self.lbl_control.grid(row=0, columnspan=3, sticky=tk.N, pady=3)


        #Botoes
        self.logo_b = tk.PhotoImage(file="add_veic.png")
        self.lbl_logo_b = tk.Label(self.container_l1, image=self.logo_b)
        self.btn_inserir_veiculo = tk.Button(self.container_l1, image=self.logo_b, command=self.Inserir_Veiculo)
        self.btn_inserir_veiculo.grid(row=1, column=0)
        self.lbl_add_veiculo = tk.Label(self.container_l1, text='Adicionar Veiculo', font=('arial', 10), bg='#e6e6e6')
        self.lbl_add_veiculo.grid(row=1, column=1, sticky=tk.W)

        self.logo_c = tk.PhotoImage(file="rem_veic.png")
        self.lbl_logo_c = tk.Label(self.container_l1, image=self.logo_c)
        self.btn_remover_veiculo = tk.Button(self.container_l1, image=self.logo_c, command=self.Remover_Veiculo)
        self.btn_remover_veiculo.grid(row=2, column=0, pady=25, padx=25)
        self.lbl_rem_veiculo = tk.Label(self.container_l1, text='Remover Veiculo     ', font=('arial', 10), bg='#e6e6e6')
        self.lbl_rem_veiculo.grid(row=2, column=1, sticky=tk.W)

        self.logo_d = tk.PhotoImage(file="add_serv.png")
        self.lbl_logo_d = tk.Label(self.container_l1, image=self.logo_d)
        self.btn_inserir_servico = tk.Button(self.container_l1, image=self.logo_d, command=self.inserir_servico)
        self.btn_inserir_servico.grid(row=1, column=2)
        self.lbl_add_serv = tk.Label(self.container_l1, text='      Adicionar Serviço', font=('arial', 10), bg='#e6e6e6')
        self.lbl_add_serv.grid(row=1, column=3, sticky=tk.W)

        self.logo_e = tk.PhotoImage(file='alt_veiculo.png')
        self.lbl_logo_ce = tk.Label(self.container_l1, image=self.logo_e)
        self.btn_alterar_veiculo = tk.Button(self.container_l1, image=self.logo_e, command=self.Alterar_Dados)
        self.btn_alterar_veiculo.grid(row=2, column=2)
        self.lbl_alt_veiculo = tk.Label(self.container_l1, text='      Alterar Dados de Veiculos   ', font=('arial', 10), bg='#e6e6e6')
        self.lbl_alt_veiculo.grid(row=2, column=3)

    '''
    Função para inserir veiculos no registro de um 
    determinado cliente
    '''
    def Inserir_Veiculo(self):
        id = self.ent_id_v.get()
        nome = self.ent_nome_v.get()
        cpf = self.ent_cpf_v.get()
        self.novaJanela_inserir_veiculo = tk.Toplevel(self.janela_de_clientes)
        self.novaJanela_inserir_veiculo.grab_set()
        Inserir_Veiculo(self.novaJanela_inserir_veiculo, id, nome, cpf)

    '''
    Aqui sao inseridos os serviços atrasves da
    seleção do veiculo no treview
    '''
    def inserir_servico(self):
        self.selecionado = self.treview_cli_veiculo.selection()
        if len(self.selecionado) == 1:
            lista = self.treview_cli_veiculo.item(self.selecionado, 'values')
            placa = (1, lista[1])
            modelo = (2, lista[2])

            self.novaJanela_inserir_servico = tk.Toplevel(self.janela_de_clientes)
            self.novaJanela_inserir_servico.grab_set()
            Inserir_Servico(self.novaJanela_inserir_servico, placa, modelo)


        elif len(self.selecionado) > 1:
            messagebox.showwarning("Atenção", "Escolha apenas 1 veiculo por serviço!")
        else:
            messagebox.showwarning("Aviso", "Selecione um veiculo!")

        '''
        Aqui sao registrados os serviços 
        em outra tela
        '''
    def Registro_de_Servico(self):
        result = self.text.get("1.0", "end")
        # print(result)
        sql_inserir = f'UPDATE observacoes SET obs="{result}" WHERE id="{self.id[1]}";'
        bd.inserir_obs(sql_inserir)
        messagebox.showinfo("Aviso", "Registro efetuado com exito!!")
        self.Top_Inserir_Servico.destroy()

    '''
    Aqui e visto os serviços que fopram efetuados naquele veiculo
    '''
    def Info(self, event):
        self.selecionado = self.treview_cli_veiculo.selection()
        lista_1 = self.treview_cli_veiculo.item(self.selecionado, 'values')
        for i in bd.consultar_tabela_obs(bd.sql_consulta_servico):
            lista = i
            aux = lista[0]
            aux_1 = lista[8]
            aux_2 = lista_1[1]
            if aux == aux_2:
                self.lbl = tk.Label(self.container_5, text='                     Informações de Serviço desse Veiculo                       ', font=('arial', 12, 'bold'), bg='#00c9d2')
                self.lbl.grid()
                self.scrollbar_texto = tk.Scrollbar(self.container_5)
                self.text_servicos = tk.Text(self.container_5, height=15, width=59, yscrollcommand=self.scrollbar_texto.set)
                self.text_servicos.grid()
                self.scrollbar_texto.grid(row=2, column=1, ipady=95)
                self.scrollbar_texto.config(command=self.text_servicos.yview)
                self.text_servicos.insert('end', aux_1)

    '''
    Função para remover o veiculo se necessario
    '''
#Verificar funcionalidade (Não funciona)
    def Remover_Veiculo(self):
        self.selecionado = self.treview_cli_veiculo.selection()
        if len(self.selecionado) == 1:
            placa = self.treview_cli_veiculo.item(self.selecionado, 'values')
            aux = placa[1]
            quarry = f'DELETE FROM veiculo WHERE placa="{aux}";'
            bd.delete_id_obs(quarry)
            messagebox.showinfo("Atenção", "O Veiculo do referido foi removido dos registros!")
            self.treview_cli_veiculo.delete(self.selecionado)
        elif len(self.selecionado) > 1:
            messagebox.showwarning("Atenção", "Escolha apenas 1 veiculo!")
        else:
            messagebox.showwarning("Aviso", "Selecione um veiculo!")

    '''
    função que altera os dados sobre aquele veiculo
    '''
    def Alterar_Dados(self):
        self.selecionado = self.treview_cli_veiculo.selection()
        if len(self.selecionado) == 1:
            lista = self.treview_cli_veiculo.item(self.selecionado, 'values')
            placa = (1, lista[1])

            for i in bd.consultar_tabela_obs(bd.sql_consulta_obs):
                if i[1] == placa[1]:
                    placa = i
                    id = self.id
                    nome = self.nome
                    cpf = self.cpf
                    modelo = i[2]
                    cor = i[3]
                    ano = i[4]
                    combustivel = i[5]
                    tipo = i[6]
                    especie = i[7]
                    nacionalidade = i[8]
                    uf = i[9]
                    self.Nova_Janela_alterar = tk.Toplevel(self.janela_de_clientes)
                    self.Nova_Janela_alterar.grab_set()
                    Alterar_Dados_Veiculo(self.Nova_Janela_alterar, id, nome, cpf, modelo, placa, cor, ano, combustivel, tipo, especie, nacionalidade, uf)
        else:
                    messagebox.showinfo('AVISO', 'Selecione um veiculo para alterar seus dados!!')



