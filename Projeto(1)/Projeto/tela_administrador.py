import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd

from janela_cadastro_alterar import Alterar_Cadastro_Cliente
from janela_de_cliente import Cliente
from cadastro_m import Cadastrar
from PIL import Image
image = Image.open("431895.png")




class Tela_Verificacao:
    def __init__(self, master):
        self.janela_verificador = master
        self.logo = tk.PhotoImage(file="sla.png")
        self.janela_verificador.iconphoto(False, self.logo)
        self.janela_verificador.title("Aplicação Projeto V.8.4.1")
        #image = Image.open("431895.png")


        '''
        Função para tela cheia
        como não vejo utilizade real para ela
        esta desativada
        '''
        # self.janela_verificador.attributes('-fullscreen', True)
        # self.janela_verificador.bind("<F11>",lambda event: self.janela_verificador.attributes("-fullscreen", not self.janela_verificador.attributes("-fullscreen")))
        # self.janela_verificador.bind("<Escape>",lambda event: self.janela_verificador.attributes("-fullscreen", False))
        # # self.janela_verificador.minsize(200, 80)

        '''
        Frames para o posicionamento 
        das caracteristicas do projeto
        '''
        # Containers
        self.container_left = tk.Frame(self.janela_verificador, bg='#a8ab9b')
        self.container_right = tk.Frame(self.janela_verificador, bg='#a8ab9b')
        self.container_left.pack(side=tk.LEFT, fill=tk.Y)
        self.container_right.pack(side=tk.RIGHT, fill=tk.Y)
        self.container_0 = tk.Frame(self.janela_verificador)
        self.container_0.pack(side=tk.TOP, fill=tk.X)
        self.container_1 = tk.Frame(self.janela_verificador)
        self.container_1.pack(side=tk.TOP)
        self.container_2 = tk.Frame(self.janela_verificador)
        self.container_2.pack(side=tk.TOP)
        self.container_3 = tk.Frame(self.janela_verificador, highlightbackground="black",highlightthickness=2)
        self.container_3.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.container_6 = tk.Frame(self.janela_verificador, bg='#00c9d2')
        self.container_6.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=30)
        self.container_4 = tk.Frame(self.container_0, bg='#f1c15d')
        self.container_4.pack(side=tk.TOP, fill=tk.BOTH)
        self.container_5 = tk.Frame(self.container_0)
        self.container_5.pack(side=tk.BOTTOM, fill=tk.BOTH)


        '''
        Função Menu para o registro de novo cliente
        pode ser alterado e para botão
        '''
        #Menu
        self.barra = tk.Menu(self.janela_verificador)
        self.menu1 = tk.Menu(self.barra, tearoff=0)
        self.barra.add_cascade(label='Registros', menu=self.menu1)
        self.menu1.add_command(label='Inserir Cliente', command=self.Cadastro)
        self.menu1.add_command(label='Atualizar Cliente', command=self.Atualizar)
        self.janela_verificador.config(menu=self.barra)

        '''
        Labels para cabeçalho e magens
        '''
        #LBL cabeçalho
        self.lbl_cabecalho = tk.Label(self.container_4, text='APLICAÇÃO DE TABULAÇÃO E INFORMAÇÃO DE SERVIÇOS', font=('Rockwell Extra Bold', 20, 'bold'), bg='#f1c15d')
        self.lbl_cabecalho.pack(pady=30, padx=30)

        # LBL para margem
        self.lbl_margem_L = tk.Label(self.container_left, text='', bg='#a8ab9b')
        self.lbl_margem_L.pack(pady=70, padx=70)
        self.lbl_margem_R = tk.Label(self.container_right, text='', bg='#a8ab9b')
        self.lbl_margem_R.pack(pady=70, padx=70)

        '''
        treview para apresentar os cliente por nome e id
        '''
        # Treview
        colunas = ['id', 'nome', 'cpf', 'email', 'celular','vinculo']
        self.treview_janela = ttk.Treeview(self.container_2, show='headings', columns=colunas, height=10)
        self.treview_janela.pack(side=tk.LEFT, fill=tk.BOTH)

        # cabeçalho
        self.treview_janela.heading('id', text="ID")
        self.treview_janela.heading('nome', text="Nome")
        self.treview_janela.heading('cpf', text="CPF/CNPJ")
        self.treview_janela.heading('email', text="E-mail")
        self.treview_janela.heading('celular', text="Celular")
        self.treview_janela.heading('vinculo', text="Vinculo")

        self.treview_janela.column('id', minwidth=0, width=50)
        self.treview_janela.column('nome', minwidth=0, width=150)
        self.treview_janela.column('cpf', minwidth=0, width=160)
        self.treview_janela.column('email', minwidth=0, width=300)
        self.treview_janela.column('celular', minwidth=0, width=200)
        self.treview_janela.column('vinculo', minwidth=0, width=180)

        self.scr = ttk.Scrollbar(self.container_2, command=self.treview_janela.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.treview_janela.configure(yscroll=self.scr.set)

        '''
        Parte do Banco de Dados que vai trazer
        as informações a respeito desse cliente
        '''
        for i in bd.consultar_tabela(bd.sql_consulta):

            self.treview_janela.insert('', 'end', values=(i[0], i[1], i[2], i[10], i[12], i[16]))

        self.treview_janela.bind('<Double-1>', self.Clique_Duplo)

        '''
        Labels para a procupa por Nome de Cliente, CPF, ou ID
        e procura Por Veiculo atraves da Placa ou ID
        
        '''
        self.lbl_nome_procura = tk.Label(self.container_5, text='Procura por ID, NOME OU CPF:', font=('arial', 12, 'bold'))
        self.lbl_nome_procura.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.E)


        '''
        Entrys para digitar a pesquisa
        '''
        self.ent_nome_procura = tk.Entry(self.container_5, width=50)
        self.ent_nome_procura.grid(row=0, column=1)


        '''
        Butão para fazer o check o item pesquisado
        '''
        self.btn_nome_procura = tk.Button(self.container_5, text='Procurar', command=self.Procurar_Nome)
        self.btn_nome_procura.grid(row=0, column=2, ipadx=20, padx=5)




    '''
    Função para a atualização das informações
    a respeito de um determinado cliente
    '''

    def Atualizar(self):
        # Função do Treview
        self.selecionado = self.treview_janela.selection()
        lista = self.treview_janela.item(self.selecionado, 'values')
        if (len(self.selecionado) == 1):

            #Parametros ==
            id = lista[0]
            self.Nova_Janela_Atualizar_Cliente = tk.Toplevel(self.janela_verificador)
            self.Nova_Janela_Atualizar_Cliente.grab_set()
            Alterar_Cadastro_Cliente(self.Nova_Janela_Atualizar_Cliente, id)

        elif (len(self.selecionado) > 1):
            messagebox.showwarning("Aviso", "Selecione apenas um!")
        else:
            messagebox.showwarning("Aviso", "Selecione um cliente!")

    '''
    Função de confimação das informações
    que foram alteradas anteriormente
    '''

    def Confirmar_Atualizacao(self):
        id = self.ent_id_cli.get()
        nome = self.ent_nome_cli.get()
        cpf = self.ent_cpf_cli.get()
        selecionado = self.treview_janela.selection()
        sql_atualizar = f'UPDATE cliente SET nome="{nome}", cpf="{cpf}" WHERE id="{id}";'
        bd.atualizar_id(sql_atualizar)
        messagebox.showinfo('Aviso', 'Cliente Atualizado com sucesso')

        self.treview_janela.item(self.selecionado, values=[id, nome, cpf])
        self.Top_Atualiza.destroy()


    def atualiza(self):
        for i in bd.consultar_tabela(bd.sql_consulta):
            self.treview_janela.insert('', 'end', values=(i))

    '''
    Função que ao clicar 2x ira abrir uma janela
    onde ira mostrar quais veiculos estão atrelados
    a determinado cliente
    '''

    def Clique_Duplo(self, event):
        self.selecionado = self.treview_janela.selection()
        if (len(self.selecionado) == 1):
            lista = self.treview_janela.item(self.selecionado, 'values')
            id = (0, lista[0])
            nome = (1, lista[1])
            cpf = (2, lista[2])
            email = (3, lista[3])
            celular = (4, lista[4])
            vinculo = (5, lista[5])
            self.novaJanela1 = tk.Toplevel(self.janela_verificador)
            self.novaJanela1.grab_set()
            Cliente(self.novaJanela1, id, nome, cpf, email, celular, vinculo)

    '''
    Janela dos cadastros para novos clientes
    '''

    def Cadastro(self):
        self.novaJanela = tk.Toplevel(self.janela_verificador)
        self.novaJanela.grab_set()
        Cadastrar(self.novaJanela)


        '''
        Função que vai retornar uma pesquisa
        
        '''
    def Procurar_Nome(self):
        if self.ent_nome_procura.get() == '':
            messagebox.showwarning('ATENÇÃO', 'Digite um dos itens requerido, Nome, CPF ou Email!')
            # for i in bd.consultar_tabela(bd.sql_consulta):
            #     id_procura = i[0]
            #     if id_procura != self.ent_nome_procura.get():
            #         pass
            #     else:
            # for i in bd.consultar_tabela(bd.sql_consulta):
            #     nome_procura = i[1]
            #     if nome_procura != self.ent_nome_procura.get():
            #         pass
            # for i in bd.consultar_tabela(bd.sql_consulta):
            #     cpf_procura = i[2]
            #     if cpf_procura != self.ent_nome_procura.get():
            #         pass
            #     # nome_procura = i[1]
            #     # cpf_procura = i[2]
            #     # if id_procura != self.ent_nome_procura.get() or nome_procura != self.ent_nome_procura.get() or cpf_procura != self.ent_nome_procura.get():
            #     #     messagebox.showwarning('Atenção','Cliente não encontrado!!')
            #     #     break
        else:
            lista = []
            for i in bd.consultar_tabela(bd.sql_consulta):
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[2])
                if self.ent_nome_procura.get() == i[0] or self.ent_nome_procura.get() == i[1] or self.ent_nome_procura.get() == i[2]:
                    self.id = str(i[0])
                    self.lbl_info = tk.Label(self.container_6, text='INFORMAÇÕES A RESPEITO DA PESQUISA', font=('arial', 12, 'bold'), bg='#00c9d2')
                    self.lbl_info.pack()
                    #Labels
                    self.lbl_procura_nome = tk.Label(self.container_3, text='Nome', font=('arial', 12, 'bold'))
                    self.lbl_procura_nome.grid(row=0, column=0, ipadx=10, ipady=10)
                    self.lbl_procura_cpf = tk.Label(self.container_3, text='CPF', font=('arial', 12, 'bold'))
                    self.lbl_procura_cpf.grid(row=1, column=0)
                    self.lbl_procura_vinculo = tk.Label(self.container_3, text='Vinculo', font=('arial', 12, 'bold'))
                    self.lbl_procura_vinculo.grid(row=2, column=0, ipadx=10, ipady=10)
                    self.lbl_procura_rua = tk.Label(self.container_3, text='Rua', font=('arial', 12, 'bold'))
                    self.lbl_procura_rua.grid(row=3, column=0)
                    self.lbl_procura_bairro = tk.Label(self.container_3, text='Bairro', font=('arial', 12, 'bold'))
                    self.lbl_procura_bairro.grid(row=4, column=0, ipadx=10, ipady=10)
                    self.lbl_procura_cidade = tk.Label(self.container_3, text='Cidade', font=('arial', 12, 'bold'))
                    self.lbl_procura_cidade.grid(row=0, column=2, ipadx=10, ipady=10)
                    self.lbl_procura_numero = tk.Label(self.container_3, text='Numero', font=('arial', 12, 'bold'))
                    self.lbl_procura_numero.grid(row=1, column=2)
                    self.lbl_procura_complemento = tk.Label(self.container_3, text='Complemento', font=('arial', 12, 'bold'))
                    self.lbl_procura_complemento.grid(row=2, column=2, ipadx=10, ipady=10)
                    self.lbl_procura_Email = tk.Label(self.container_3, text='Email', font=('arial', 12, 'bold'))
                    self.lbl_procura_Email.grid(row=3, column=2)
                    self.lbl_procura_celular = tk.Label(self.container_3, text='Celular', font=('arial', 12, 'bold'))
                    self.lbl_procura_celular.grid(row=4, column=2, ipadx=10, ipady=10)

                    #Entrys
                    self.ent_procura_nome = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_nome.grid(row=0, column=1)
                    self.ent_procura_cpf = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_cpf.grid(row=1, column=1)
                    self.ent_procura_vinculo = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_vinculo.grid(row=2, column=1)
                    self.ent_procura_rua = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_rua.grid(row=3, column=1)
                    self.ent_procura_bairro = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_bairro.grid(row=4, column=1)
                    self.ent_procura_cidade = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_cidade.grid(row=0, column=3)
                    self.ent_procura_numero = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_numero.grid(row=1, column=3)
                    self.ent_procura_complemento = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_complemento.grid(row=2, column=3)
                    self.ent_procura_email = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_email.grid(row=3, column=3)
                    self.ent_procura_celular = tk.Entry(self.container_3, width=40, font=('arial', 12, 'bold'))
                    self.ent_procura_celular.grid(row=4, column=3)


                    self.ent_procura_nome.insert('end', i[1])
                    self.ent_procura_cpf.insert('end', i[2])
                    self.ent_procura_vinculo.insert('end', i[16])
                    self.ent_procura_rua.insert('end', i[5])
                    self.ent_procura_bairro.insert('end', i[7])
                    self.ent_procura_cidade.insert('end', i[15])
                    self.ent_procura_numero.insert('end', i[9])
                    self.ent_procura_complemento.insert('end', i[8])
                    self.ent_procura_email.insert('end', i[10])
                    self.ent_procura_celular.insert('end', i[12])

                    #Disableds
                    self.ent_procura_nome.config(state='disabled')
                    self.ent_procura_cpf.config(state='disabled')
                    self.ent_procura_vinculo.config(state='disabled')
                    self.ent_procura_rua.config(state='disabled')
                    self.ent_procura_bairro.config(state='disabled')
                    self.ent_procura_cidade.config(state='disabled')
                    self.ent_procura_numero.config(state='disabled')
                    self.ent_procura_complemento.config(state='disabled')
                    self.ent_procura_email.config(state='disabled')
                    self.ent_procura_celular.config(state='disabled')

                    #Butão para verificar info dos clientes pesquisados
                    self.btn_ver = tk.Button(self.container_3, text="Ver INFO", command=self.Click_Info)
                    self.btn_ver.grid(row=5, column=3)
                




    def Click_Info(self):
        for i in bd.consultar_tabela(bd.sql_consulta):
            if self.ent_nome_procura.get() == i[1]:
                lista = (i[0], i[1], i[2], i[10], i[12], i[16])
                id = (0, lista[0])
                nome = (1, lista[1])
                cpf = (2, lista[2])
                email = (3, lista[3])
                celular = (4, lista[4])
                vinculo = (5, lista[5])
                self.janela_info = tk.Toplevel(self.janela_verificador)
                self.janela_info.grab_set()
                Cliente(self.janela_info, id, nome, cpf, email, celular, vinculo)

    # def Atualizar_Tvw(self):
    #     for i in self.treview_janela.get_children():
    #         self.treview_janela.delete(i)
    #
    #     for i in bd.consultar_tabela_obs(bd.sql_consulta_obs):
    #         lista = i
    #         aux = int(lista[0])
    #         aux1 = int(self.id)
    #         print(self.id)
    #         if aux == aux1:
    #             self.treview_janela.insert('', 'end', values=(i))


variavel = tk.Tk()
Tela_Verificacao(variavel)
variavel.configure(bg='#00c9d2')
variavel.mainloop()
