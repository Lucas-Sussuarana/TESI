import tkinter as tk
from tkinter import messagebox, ttk
import banco_servicos as bd
import awesometkinter as atk

class Cadastrar:
    def __init__(self, master):


        self.janela1 = master
        self.janela1.title("Cadastro")
        self.janela1.minsize(220, 70)
        #self.janela1.resizable(False, False)

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
        # self.lbl_margem_B = tk.Label(self.container_botton, text='', bg='#a8ab9b')
        # self.lbl_margem_B.pack(pady=50, padx=50)



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
        self.btn = tk.Button(self.container_3, text='Registrar', anchor=tk.S, command=self.Inserir_cli)
        self.btn.grid(sticky=tk.S, ipadx=15)

    def Inserir_cli(self):
        for i in bd.consultar_tabela(bd.sql_consulta):
            if self.ent_cpf.get() == i[2]:
                messagebox.showwarning('Atenção', 'Esse CPF ja esta cadastrado!')
            else:
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
                cont_IDs = []
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
                    for i in bd.consultar_tabela('SELECT * FROM cliente;'):
                        cont_IDs.append(i[0])
                    sql_inserir = f'INSERT INTO cliente VALUES("{len(cont_IDs)}","{nome}","{cpf}", "{genero}", "{data}", "{rua}", "{cep}", "{bairro}", "{complemento}", "{numero}", "{email}", "{telefone}", "{celular}", "{celular_o}", "{estado}", "{cidade}", "{vinculo}");'
                    bd.inserir(sql_inserir)
                    self.janela1.destroy()



