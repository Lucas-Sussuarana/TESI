import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd
class Inserir_Servico:
    def __init__(self, master, placa, modelo):
        self.placa = placa[1]
        self.modelo = modelo[1]
        self.janela_inserir_servico = master
        self.janela_inserir_servico.title("Inserção de veiculo do TESTE DE AIDS 2")
        self.aux = []
        self.lista_geral = []
        lista_p = []

        '''
        
        Containers para controle de bordas e itens internos
        
        '''

        # Containers
        self.container_0 = tk.Frame(self.janela_inserir_servico, bg='#f1c15d')  # , bg='#e6e6e6'
        self.container_1 = tk.Frame(self.janela_inserir_servico, bg='#00c9d2')
        self.container_2 = tk.Frame(self.janela_inserir_servico)
        self.container_3 = tk.Frame(self.janela_inserir_servico, bg='#00c9d2')
        self.container_4 = tk.Frame(self.janela_inserir_servico, bg='#e6e6e6')
        self.container_5 = tk.Frame(self.container_2, bg='#e6e6e6')
        self.container_6 = tk.Frame(self.container_2, bg='#e6e6e6')
        self.container_esquerdo = tk.Frame(self.janela_inserir_servico, bg='#a8ab9b')  # highlightbackground="black",highlightthickness=10
        self.container_direito = tk.Frame(self.janela_inserir_servico, bg='#a8ab9b')
        self.container_inferior = tk.Frame(self.janela_inserir_servico, bg='#a8ab9b')

        self.container_esquerdo.pack(side=tk.LEFT, fill=tk.Y)
        self.container_direito.pack(side=tk.RIGHT, fill=tk.Y)
        self.container_inferior.pack(side=tk.BOTTOM, fill=tk.X)
        self.container_0.pack(side=tk.TOP, fill=tk.X)
        self.container_1.pack(side=tk.TOP, fill=tk.X)
        self.container_2.pack(side=tk.TOP, fill=tk.X)
        self.container_3.pack(side=tk.TOP, fill=tk.X)
        self.container_4.pack(side=tk.TOP, fill=tk.X)
        self.container_5.pack(side=tk.LEFT, fill=tk.X, ipadx=20, ipady=10, anchor=tk.N)
        self.container_6.pack(side=tk.RIGHT, fill=tk.X, ipadx=100, ipady=10)

        # Treview das pecas
        colunas = ['id', 'nome', 'valor']
        self.treview_janela = ttk.Treeview(self.container_5, show='headings', columns=colunas, height=4)
        self.treview_janela.grid(row=6, column=1, columnspan=2, ipadx=60, sticky=tk.S, pady=10)

        # cabeçalho
        self.treview_janela.heading('id', text="ID")
        self.treview_janela.heading('nome', text="Nome")
        self.treview_janela.heading('valor', text="Valor")

        self.treview_janela.column('id', minwidth=0, width=50)
        self.treview_janela.column('nome', minwidth=0, width=150)
        self.treview_janela.column('valor', minwidth=0, width=70)

        self.scr = ttk.Scrollbar(self.container_5, command=self.treview_janela.yview)
        self.scr.grid(row=6, sticky=tk.W, column=3, ipady=30)
        self.treview_janela.configure(yscroll=self.scr.set)

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

        self.lbl_logo_0 = tk.Label(self.container_0, text='TESTE DE AIDS 2', font=('    Rockwell Extra Bold', 20, 'bold'), bg='#f1c15d')
        self.lbl_logo_0.pack(side=tk.LEFT, ipady=20)

        # LBL para margem
        self.lbl_margem_L = tk.Label(self.container_esquerdo, text='', bg='#a8ab9b')
        self.lbl_margem_L.pack(pady=65, padx=65)
        self.lbl_margem_R = tk.Label(self.container_direito, text='', bg='#a8ab9b')
        self.lbl_margem_R.pack(pady=65, padx=65)

        #Labels das informações
        self.lbl_1 = tk.Label(self.container_1, text=self.modelo, font=('arial', 12, 'bold'), fg='white', bg='#00c9d2')
        self.lbl_1.grid(row=0, column=3)

        self.lbl_2 = tk.Label(self.container_1, text=self.placa, font=('arial', 12, 'bold'), fg='white', bg='#00c9d2')
        self.lbl_2.grid(row=0, column=5)

        self.lbl_titulo = tk.Label(self.container_1, text=f'ADICIONAR SERVIÇOS PARA O VEICULO', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_titulo.grid(row=0)

        self.lbl_titulo_1 = tk.Label(self.container_1, text=f'DE PLACA ', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_titulo_1.grid(row=0, column=4)

        '''
        
        Aqui iniciamos os tipos de serviços e
        as caracteristicas de cada item
        
        '''
        #Labels e Entrys das especificações a cerca dos serviços praticados
        self.lbl_info = tk.Label(self.container_5, text='INFOMAÇÕES ADICIONAIS DE SERVIÇO:', font=('arial', 12, 'bold'), bg='#e6e6e6', fg='red')
        self.lbl_info.grid(row=0, ipadx=10, ipady=10, columnspan=2)

        self.lbl_seguro = tk.Label(self.container_5, text='Possui Seguro?', font=('arial', 12), bg='#e6e6e6')
        self.lbl_seguro.grid(row=1)
        self.seguro = tk.StringVar
        self.cbx_seguro = ttk.Combobox(self.container_5, font=('arial', 12, 'bold'))
        self.cbx_seguro['values'] = ('', 'SIM', 'NÃO')
        self.cbx_seguro.current(0)
        self.cbx_seguro.grid(row=1, column=1, ipadx=16)


        self.lbl_guincho = tk.Label(self.container_5, text='Veio de Guincho?', font=('arial', 12), bg='#e6e6e6')
        self.lbl_guincho.grid(row=2, ipadx=10, ipady=10)
        self.guincho = tk.StringVar
        self.cbx_guincho = ttk.Combobox(self.container_5, font=('arial', 12, 'bold'))
        self.cbx_guincho['values'] = ('', 'SIM', 'NÃO')
        self.cbx_guincho.current(0)
        self.cbx_guincho.grid(row=2, column=1, ipadx=16)

        self.lbl_requerente = tk.Label(self.container_5, text='Requerente', font=('arial', 12), bg='#e6e6e6')
        self.lbl_requerente.grid(row=3)
        self.requerente= tk.StringVar
        self.cbx_requerente = ttk.Combobox(self.container_5, font=('arial', 12, 'bold'))
        self.cbx_requerente['values'] = ('', 'PROPRIETARIO', 'TERCEIRO')
        self.cbx_requerente.current(0)
        self.cbx_requerente.grid(row=3, column=1, ipadx=16)

        #pecas vindas do BD.
        lista_pecas = []
        for i in bd.consultar_tabela(bd.sql_consulta_pecas):
            lista_pecas.append(i[1])

        self.pecas = tk.StringVar()
        self.lbl_pecas = tk.Label(self.container_5, text='Peças', font=('arial', 12), bg='#e6e6e6')
        self.lbl_pecas.grid(row=4, ipadx=10, ipady=10)
        self.cbx_pecas = ttk.Combobox(self.container_5, font=('arial', 12, 'bold'), textvariable=self.pecas)
        self.lista_pecas = []
        for i in bd.consultar_tabela(bd.sql_consulta_pecas):
            self.lista_pecas.append(i[1])


        for i in self.lista_pecas:
            self.cbx_pecas.insert('', '')
        self.cbx_pecas['values'] = (self.lista_pecas)
        self.cbx_pecas.grid(row=4, column=1, ipadx=16)
        self.btn_add = tk.Button(self.container_5, text="Inserir", command=self.Inserir)
        self.btn_add.grid(row=4, column=2, ipadx=20)



        #Labels e Entrys das caracteristicas desse serviço
        self.lbl_check_service = tk.Label(self.container_6, text='TIPO DE SERVIÇO:', font=('arial', 12, 'bold'), width=20, wraplength=200, anchor=tk.W, bg='#e6e6e6', fg='red')
        self.lbl_check_service.grid()
        self.radiobutton = tk.StringVar(self.container_6, "0")
        self.v4 = tk.IntVar
        self.v5 = tk.IntVar
        self.rbt_1 = tk.Radiobutton(self.container_6, text='REVISÃO BASICA', value='1', variable=self.radiobutton, bg='#e6e6e6')
        self.rbt_2 = tk.Radiobutton(self.container_6, text='REVISÃO INTERMEDIARIA', value='2', variable=self.radiobutton, bg='#e6e6e6')
        self.rbt_3 = tk.Radiobutton(self.container_6, text='REVISÃO COMPLETA', value='3', variable=self.radiobutton, bg='#e6e6e6')
        self.ckb_4 = tk.Checkbutton(self.container_6, text='SERVIÇOS PONTUAIS', variable=self.v4, command=self.texto, bg='#e6e6e6')
        self.ckb_5 = tk.Checkbutton(self.container_6, text='ORÇAMENTO', variable=self.v5, bg='#e6e6e6')
        self.rbt_1.grid(sticky=tk.W)
        self.rbt_2.grid(sticky=tk.W)
        self.rbt_3.grid(sticky=tk.W)
        self.ckb_4.grid(sticky=tk.W)
        self.ckb_5.grid(sticky=tk.W)
        self.scrollbar_text_especifico = tk.Scrollbar(self.container_6)
        self.text_especifico = tk.Text(self.container_6, height=8, width=55, yscrollcommand=self.scrollbar_text_especifico.set)
        self.text_especifico.grid(columnspan=5, sticky=tk.W)
        self.scrollbar_text_especifico.grid(row=6, column=6, ipady=40)
        self.scrollbar_text_especifico.config(command=self.text_especifico.yview)
        self.text_especifico.insert('end', self.cbx_guincho.get())
        self.text_especifico.config(state='disabled')

        self.btn_servico = tk.Button(self.container_6, text="Registrar", command=self.Registrar_Servico, bg='#e6e6e6')
        self.btn_servico.grid(column=2, ipadx=10)


        #Label co Container para a checagem dos itens que vão ser adicionados a Ordem de Serviço "O.S"
        self.lbl_inbformacoes_gerais = tk.Label(self.container_3, text='INFORMAÇÕES GERAIS', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_inbformacoes_gerais.grid()


    '''
    
    Aqui inserimos no final um relatorio 
    sobre as informações da O.S
    
    '''


    def Registrar_Servico(self):
        if self.cbx_seguro.get() == '' or self.cbx_guincho.get() == '' or self.cbx_requerente.get() == '':
            messagebox.showinfo('ATENCAO','Verifique Se todos os parametros estao preenchidos!!')
        else:
            list = []
            self.conteudo = self.text_especifico.get("1.0", "end")
            self.lista_geral.append(" Possui seguro? " + self.cbx_seguro.get())
            self.lista_geral.append(" Veio de Guincho? " + self.cbx_guincho.get())
            self.lista_geral.append(" Requerente? " + self.cbx_requerente.get())
            self.lista_geral.append(" Peças utilizadas? ")
            for i in self.aux:
                self.lista_geral.append(i)

            if self.radiobutton.get() == '0':
                self.lista_geral.append(" Serviço inicial Solicitado? NENHUM, ")

            elif self.radiobutton.get() == '1':
                self.lista_geral.append(" Serviço inicial Solicitado? REVISAO BASICA, ")

            elif self.radiobutton.get() == '2':
                self.lista_geral.append(" Serviço inicial Solicitado? REVISAO INTERMEDIARIA, ")

            elif self.radiobutton.get() == '3':
                self.lista_geral.append(" Serviço inicial Solicitado?  REVISAO COMPLETA, ")


            self.lista_geral.append(" Houve serviços adicionais? " + self.conteudo)
            self.btn_servico.config(state='disabled')
            # # Caixa para verificacao dos serviços
            self.scrollbar_texto = tk.Scrollbar(self.container_4)
            self.texto_1 = tk.Text(self.container_4, height=6, width=132, yscrollcommand=self.scrollbar_texto.set)
            self.texto_1.grid(columnspan=5, sticky=tk.W)
            self.scrollbar_texto.grid(row=0, column=6, ipady=25)
            self.scrollbar_texto.config(command=self.texto_1.yview)
            for i in self.lista_geral:
                self.texto_1.insert('end', i)

            self.btn_servico = tk.Button(self.container_4, text="Gravar", command=self.Gravar, bg='grey')
            self.btn_servico.grid(pady=12, padx=12, ipadx=15,  columnspan=5, sticky=tk.E)

    def texto(self):
        self.ckb_4.config(state='disabled')
        self.text_especifico.config(state='normal')
        self.text_especifico.insert('end', 'INSIRA OS SERVIÇOS')

    def Inserir(self):

        item = self.cbx_pecas.get()
        for i in bd.consultar_tabela(bd.sql_consulta_pecas):
            if i[1] == item:
                self.treview_janela.insert('', 'end', values=(i))
                self.aux.append(i[1] + ', ')


    def Gravar(self):
        placa = self.placa
        modelo = self.modelo
        seguro = self.cbx_seguro.get()
        guincho = self.cbx_guincho.get()
        requerente = self.cbx_requerente.get()
        lista_de_pecas = []

        #peças
        for i in self.aux:
            lista_de_pecas.append(i)

        #tipo dp serviço
        if self.radiobutton.get() == 0:
            servico = ("Serviço inicial Solicitado? NENHUM, ")

        elif self.radiobutton.get() == 1:
            servico = ("Serviço inicial Solicitado? REVISAO BASICA, ")

        elif self.radiobutton.get() == 2:
            servico = ("Serviço inicial Solicitado? REVISAO INTERMEDIARIA, ")

        else:
            servico = ("Serviço inicial Solicitado?  REVISAO COMPLETA, ")

        conteudo = self.conteudo
        conteudo_geral = self.texto_1.get("1.0", "end")
        sql_inserir = f'INSERT INTO servico VALUES("{placa}","{modelo}","{seguro}","{guincho}","{requerente}","{lista_de_pecas}","{servico}","{conteudo}","{conteudo_geral}");'
        bd.inserir_obs(sql_inserir)
        messagebox.showinfo('Aviso', 'Serviços registrados!')
        self.janela_inserir_servico.destroy()



