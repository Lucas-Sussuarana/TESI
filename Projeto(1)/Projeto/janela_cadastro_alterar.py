import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd
import awesometkinter as atk


class Alterar_Cadastro_Cliente:
    def __init__(self, master, id):
        self.id = id
        self.janela1 = master
        self.janela1.title("Alterar Dados de Clientes")


        #Containers
        self.container_left = tk.Frame(self.janela1, bg='#a8ab9b')
        self.container_right = tk.Frame(self.janela1, bg='#a8ab9b')
        self.container_botton = tk.Frame(self.janela1, bg='#a8ab9b')
        self.container_0 = tk.Frame(self.janela1, bg='#f1c15d')
        self.container_1 = tk.Frame(self.janela1, bg='#e6e6e6')
        self.container_2 = tk.Frame(self.janela1, bg='#e6e6e6')
        self.container_3 = tk.Frame(self.janela1, bg='#e6e6e6')
        self.container_4 = tk.Frame(self.janela1, bg='#00c9d2')
        self.container_5 = tk.Frame(self.janela1, bg='#00c9d2')
        self.container_6 = tk.Frame(self.janela1, bg='#00c9d2')
        self.container_7 = tk.Frame(self.janela1, bg='#00c9d2')
        self.container_8 = tk.Frame(self.janela1, bg='#00c9d2')
        self.container_left.pack(side=tk.LEFT, fill=tk.Y)
        self.container_right.pack(side=tk.RIGHT, fill=tk.Y)
        self.container_botton.pack(side=tk.BOTTOM, fill=tk.X)
        self.container_0.pack(side=tk.TOP, fill=tk.X)
        self.container_4.pack(side=tk.TOP, fill=tk.X)
        self.container_1.pack(side=tk.TOP, ipady=20, anchor=tk.W, fill=tk.X)
        self.container_5.pack(side=tk.TOP, fill=tk.X)
        self.container_2.pack(side=tk.TOP, ipady=30, anchor=tk.W, fill=tk.X)
        self.container_6.pack(side=tk.TOP, fill=tk.X)
        self.container_3.pack(side=tk.TOP, ipady=30, anchor=tk.W, fill=tk.X)
        # self.container_botton.pack(side=tk.BOTTOM, fill=tk.X)
        # self.container_7.pack(side=tk.TOP, fill=tk.X)
        # self.container_8.pack(side=tk.TOP, ipady=40, anchor=tk.W, fill=tk.X)



        #Logo da empresa ####Arrumar
        self.logo_2 = tk.PhotoImage(file="sla.png")
        self.lbl_logo_1 = tk.Label(self.container_0, text='APLICAÇÃO DE TABULAÇÃO E INFORMAÇÃO DE SERVIÇOS', font=('    Rockwell Extra Bold', 20, 'bold'), bg='#f1c15d')
        #self.lbl_logo_1.image = self.logo_1
        self.lbl_logo_1.pack(side=tk.LEFT, ipady=20)

        #imagem bordas
        self.logo_1 = tk.PhotoImage(file="lateral.png")
        self.lbl_logo_1 = tk.Label(self.container_left, image=self.logo_1, relief=tk.SOLID)#raised, ridge, solid, or sunken
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

        #LBL para margem
        self.lbl_margem_L = tk.Label(self.container_left, text='', bg='#a8ab9b')
        self.lbl_margem_L.pack(pady=65, padx=65)
        self.lbl_margem_R = tk.Label(self.container_right, text='', bg='#a8ab9b')
        self.lbl_margem_R.pack(pady=65, padx=65)




        #Entrys & Labels
        #Dados Pessoais
        self.lbl_dados = tk.Label(self.container_4, text='DADOS PESSOAIS:', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_dados.grid(row=0, columnspan=2)

        self.lbl_nome = tk.Label(self.container_1, text='*Nome:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_nome.grid(row=0, ipadx=10, ipady=10)
        self.ent_nome = tk.Entry(self.container_1, width=70, font=('arial', 10))
        self.ent_nome.grid(row=0, column=1)

        #Data de nascimento
        self.lbl_data = tk.Label(self.container_1, text='Data de Nascimento:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_data.grid(row=0, column=2)
        self.ent_data = tk.Entry(self.container_1, width=30, font=('arial', 10))
        self.ent_data.grid(row=0, column=3)

        # CPF
        self.lbl_cpf = tk.Label(self.container_1, text='*Cpf/CNPJ:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cpf.grid()
        self.ent_cpf = tk.Entry(self.container_1, width=30, font=('arial', 10))
        self.ent_cpf.grid(row=1, column=1, sticky=tk.W)

        #Genero
        self.lbl_genero = tk.Label(self.container_1, text='*Genero:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_genero.grid(ipadx=10, ipady=10)
        self.v = tk.StringVar
        self.cbx = ttk.Combobox(self.container_1)
        self.cbx['values'] = ('', 'MASCULINO', 'FEMININO')
        self.cbx.current(0)
        self.cbx.grid(row=2, column=1, sticky=tk.W)


        #Endereço do Cliente
        #Rua
        self.lbl_endereco = tk.Label(self.container_5, text='ENDEREÇO:', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_endereco.grid(row=0)

        self.lbl_rua = tk.Label(self.container_2, text='*Rua:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_rua.grid(ipadx=10, ipady=10)
        self.ent_rua = tk.Entry(self.container_2, width=40, font=('arial', 10))
        self.ent_rua.grid(row=0, column=1)

        #Endereço
        self.lbl_bairro = tk.Label(self.container_2, text='*Bairro:', font=('arial', 12),bg='#e6e6e6')
        self.lbl_bairro.grid(row=0, column=2)
        self.ent_bairro = tk.Entry(self.container_2, width=60, font=('arial', 10))
        self.ent_bairro.grid(row=0, column=3)

        #Cep
        self.lbl_cep = tk.Label(self.container_2, text='*Cep:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cep.grid()
        self.ent_cep = tk.Entry(self.container_2, width=30, font=('arial', 10))
        self.ent_cep.grid(row=1, column=1, sticky=tk.W)

        # Cidade
        self.lbl_cidade = tk.Label(self.container_2, text='*Estado:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_cidade.grid(ipadx=10, ipady=10)
        self.ent_cidade = tk.Entry(self.container_2, width=40, font=('arial', 10))
        self.ent_cidade.grid(row=2, column=1)


        #Complemento
        self.lbl_complemento = tk.Label(self.container_2, text='Complemento:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_complemento.grid(row=1, column=2)
        self.ent_complemento = tk.Entry(self.container_2, width=60, font=('arial', 10))
        self.ent_complemento.grid(row=1, column=3)

        #Numero
        self.lbl_numero = tk.Label(self.container_2, text='*Numero:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_numero.grid(row=0, column=4, ipadx=10, ipady=10)
        self.ent_numero = tk.Entry(self.container_2, width=10, font=('arial', 10))
        self.ent_numero.grid(row=0, column=5)

        # Estado
        self.lbl_estado = tk.Label(self.container_2, text='*Cidade:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_estado.grid(row=2, column=2)
        self.ent_estado = tk.Entry(self.container_2, width=40, font=('arial', 10))
        self.ent_estado.grid(row=2, column=3, sticky=tk.W)

        #Formas de contato com o cliente
        #Email
        self.lbl_contato = tk.Label(self.container_6, text='CONTATO:', font=('arial', 12, 'bold'), bg='#00c9d2')
        self.lbl_contato.grid(row=0)

        self.lbl_email = tk.Label(self.container_3, text='*Email:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_email.grid(ipadx=10, ipady=10)
        self.ent_email = tk.Entry(self.container_3, width=30, font=('arial', 10))
        self.ent_email.grid(row=0, column=1)
        self.lbl_emailnovo = tk.Label(self.container_3, text='*Email(Novamente):', font=('arial', 12), bg='#e6e6e6')
        self.lbl_emailnovo.grid()
        self.ent_emailnovo = tk.Entry(self.container_3, width=30, font=('arial', 10))
        self.ent_emailnovo.grid(row=1, column=1)

        #Telefones
        self.lbl_telefone= tk.Label(self.container_3, text='Telefone:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_telefone.grid(row=0, column=3, ipadx=10, ipady=10)
        self.ent_telefone = tk.Entry(self.container_3, width=30, font=('arial', 10))
        self.ent_telefone.grid(row=0, column=4)
        self.lbl_celular = tk.Label(self.container_3, text='*Celular:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_celular.grid(row=1, column=3)
        self.ent_celular = tk.Entry(self.container_3, width=30, font=('arial', 10))
        self.ent_celular.grid(row=1, column=4)
        self.lbl_celular_terceiro = tk.Label(self.container_3, text='Celular Secundario:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_celular_terceiro.grid(row=0, column=5, ipadx=10, ipady=10)
        self.ent_celular_terceiro = tk.Entry(self.container_3, width=30, font=('arial', 10))
        self.ent_celular_terceiro.grid(row=0, column=6)

        self.lbl_teste_terceiro = tk.Label(self.container_3, text='(DDD) + numero', font=('Arial', 10), fg='red', bg='#e6e6e6')
        self.lbl_teste_terceiro.grid(row=1, column=5)

        #vinculo
        self.lbl_vinculo= tk.Label(self.container_1, text='*Vinculo:', font=('arial', 12), bg='#e6e6e6')
        self.lbl_vinculo.grid(column=2, row=1)
        self.vinculo = tk.StringVar
        self.cbx_V = ttk.Combobox(self.container_1)
        self.cbx_V['values'] = ('', 'PARTICULAR', 'EMPRESARIAL')
        self.cbx_V.current(0)
        self.cbx_V.grid(row=1, column=3, sticky=tk.W)

        # BUTAO 2
        self.btn = tk.Button(self.container_3, text='Registrar', anchor=tk.S, command=self.Atualizar_cli)
        self.btn.grid(sticky=tk.S, ipadx=15)

        '''
        Pegamos somente o ID unico para
        selecionar qual cliente no banco
        de dados sofrera as alterações
        e usamos essas informações
        '''
        for i in bd.consultar_tabela(bd.sql_consulta):
            lista = i
            aux = int(lista[0])
            aux1 = int(id[0])

            if aux == aux1:
                self.id_auxiliar = aux
                #Inserção dos valores retornado do banco de dados
                self.ent_nome.insert('end', i[1])
                self.ent_cpf.insert('end', i[2])

                #Genero
                lista_genero = self.cbx['values']
                list = lista_genero.index(i[3])
                self.cbx.current(list)

                self.ent_data.insert('end', i[4])
                self.ent_rua.insert('end', i[5])
                self.ent_cep.insert('end', i[6])
                self.ent_bairro.insert('end', i[7])
                self.ent_complemento.insert('end', i[8])
                self.ent_numero.insert('end', i[9])
                self.ent_email.insert('end', i[10])
                self.ent_emailnovo.insert('end', i[10])
                self.ent_telefone.insert('end', i[11])
                self.ent_celular.insert('end', i[12])
                self.ent_celular_terceiro.insert('end', i[13])
                self.ent_cidade.insert('end', i[14])
                self.ent_estado.insert('end', i[15])

                # Vinculo
                lista_vinculo = self.cbx_V['values']
                list_v = lista_vinculo.index(i[16])
                self.cbx_V.current(list_v)
                break
    '''
    Nessa função nos atualizamos as informações
    do cliente
    '''
    def Atualizar_cli(self):
        id_id = self.id_auxiliar
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        genero = self.cbx.get()
        vinculo = self.cbx_V.get()
        data = self.ent_data.get()
        if data == '':
            data = ("Não Informado")
        estado = self.ent_estado.get()
        cidade = self.ent_cidade.get()
        rua = self.ent_rua.get()
        cep = self.ent_cep.get()
        bairro = self.ent_bairro.get()
        complemento = self.ent_complemento.get()
        if complemento == '':
            complemento = ("Não informado")
        numero = self.ent_numero.get()
        email = self.ent_email.get()
        email_n = self.ent_emailnovo.get()
        telefone = self.ent_telefone.get()
        if telefone == '':
            telefone = ("Não informado")
        celular = self.ent_celular.get()
        celular_o = self.ent_celular_terceiro.get()
        if celular_o == '':
            celular_o = ("Não informado")
        if nome == '':
            messagebox.showwarning('AVISO', 'O campo Nome precisa ser preenchido!')

        elif cpf == '':
            messagebox.showwarning('AVISO', 'O campo Cpf precisa ser preenchido!')

        elif genero == '':
            messagebox.showwarning('AVISO', 'O campo Genero precisa ser preenchido!')

        elif rua == '':
            messagebox.showwarning('AVISO', 'O campo Rua precisa ser preenchido!')

        elif cep == '':
            messagebox.showwarning('AVISO', 'O campo Cep precisa ser preenchido!')

        elif bairro == '':
            messagebox.showwarning('AVISO', 'O campo Bairro precisa ser preenchido!')

        elif numero == '':
            messagebox.showwarning('AVISO', 'O campo Numero precisa ser preenchido!')

        elif email == '':
            messagebox.showwarning('AVISO', 'O campo Email precisa ser preenchido!')

        elif email_n == '':
            messagebox.showwarning('AVISO', 'O campo Email(Novamente) precisa ser preenchido!')

        elif email != email_n:
            messagebox.showwarning('AVISO', 'Os Emails descritos não são iguais!')

        elif celular == '':
            messagebox.showwarning('AVISO', 'O campo Celular precisa ser preenchido!')

        elif estado == '':
            messagebox.showwarning('AVISO', 'O campo Estado precisa ser preenchido!')

        elif cidade == '':
            messagebox.showwarning('AVISO', 'O campo Cidade precisa ser preenchido!')

        elif vinculo == '':
            messagebox.showwarning('AVISO', 'O campo Vinculo não pode estar vazio!')
        else:
            sql_atualizar = f'UPDATE cliente SET nome="{nome}", cpf="{cpf}", genero="{genero}", data="{data}", rua="{rua}", cep="{cep}", bairro="{bairro}", complemento="{complemento}", numero="{numero}", email="{email}", telefone="{telefone}", celular="{celular}", celular_o="{celular_o}", estado="{estado}", cidade="{cidade}", vinculo="{vinculo}" WHERE id="{id_id}";'
            bd.atualizar_id(sql_atualizar)
            messagebox.showinfo('Aviso', 'Informações do Cliente Atualizadas com Sucesso')
            self.janela1.destroy()

