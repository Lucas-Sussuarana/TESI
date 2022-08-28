import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conta import Conta
from cliente import Cliente
from banco import Banco

class Painel:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Banco X (Menu principal)")
        self.janela.geometry('460x300')
        self.janela.configure(bg='gray')
        self.container_1 = tk.Frame(self.janela)
        self.container_1.pack(side=tk.LEFT)
#Menu dos Clientes =====================================================================================================
        self.barra = tk.Menu(self.janela)
        self.menu1 = tk.Menu(self.barra, tearoff=0)
        self.barra.add_cascade(label='Cliente', menu=self.menu1)    #Feito
        self.menu1.add_command(label='Cadastrar Cliente', command=self.Cadastrar_Cliente)   #Ajeitar a funcionalidade command=self.tela_cadastrar_conta, para um particula
        self.menu1.add_command(label='Atualizar Cliente', command=self.Atualizar_Cliente)   #Ajeitar a funcionalidade command=self.atualizar_conta, para um particular
        self.menu1.add_command(label='Ver lista de Clientes') #Adicionar Funcionalidade que ainda não tem
        self.janela.config(menu=self.barra)

#Menu das Contas =======================================================================================================
        self.menu2 = tk.Menu(self.barra, tearoff=0)
        self.barra.add_cascade(label='Contas', menu=self.menu2) #Feito
        self.menu2.add_command(label='Cadastrar Conta', command=self.tela_cadastrar_conta) #Falta adicionar a funcionalidade
        self.menu2.add_command(label='Atualizar Conta', command=self.atualizar_conta) #Ajeitar a funcionalidade
        self.menu2.add_command(label='Ver Lista de Contas') #Adicionar Funcionalidade que ainda não tem

#Menu das Transacoes ===================================================================================================
        self.menu3 = tk.Menu(self.barra, tearoff=0)
        self.barra.add_cascade(label='Transações', menu=self.menu3) #Feito
        self.menu3.add_command(label='Depositos', command=self.Conta_Depositar) #Falta adicionar funcionalidades
        self.menu3.add_command(label='Saques', command=self.Conta_Sacar)    #Falta adicionar funcionalidades
        self.menu3.add_command(label='Extratos') #Adicionar Funcionalidade que ainda não tem

#Cadastrar Cliente =====================================================================================================
    #cli1 = Cliente('Manoel', 'L.', 000000000000)
    def Cadastrar_Cliente(self):
        self.Top_Cadastrar_Cliente = tk.Toplevel()
        self.Top_Cadastrar_Cliente.grab_set()
        self.Top_Cadastrar_Cliente.title('Cadastro de Novo Cliente')
        self.Top_Cadastrar_Cliente.geometry('300x200')
        self.lbl_Nome_Novo_Cliente = tk.Label(self.Top_Cadastrar_Cliente, text='Nome:')
        self.lbl_Nome_Novo_Cliente.grid(row=0, column=0)
        self.lbl_Segundo_Nome_Novo_Cliente = tk.Label(self.Top_Cadastrar_Cliente, text='Segundo Nome:')
        self.lbl_Segundo_Nome_Novo_Cliente.grid(row=1, column=0)
        self.lbl_Cpf = tk.Label(self.Top_Cadastrar_Cliente, text='CPF:')
        self.lbl_Cpf.grid(row=2, column=0)

        self.ent_Nome_Novo_Cliente = tk.Entry(self.Top_Cadastrar_Cliente, width=30)
        self.ent_Nome_Novo_Cliente.grid(row=0, column=1)
        self.ent_Segundo_Nome_Novo_Cliente = tk.Entry(self.Top_Cadastrar_Cliente, width=30)
        self.ent_Segundo_Nome_Novo_Cliente.grid(row=1, column=1)
        self.ent_Cpf = tk.Entry(self.Top_Cadastrar_Cliente, width=30)
        self.ent_Cpf.grid(row=2, column=1)

        self.btn_confirmar = tk.Button(self.Top_Cadastrar_Cliente, text='Confirmar Cadastro', command=self.confirmar_cadastro_cliente)
        self.btn_confirmar.grid(row=3, column=1)
############### Ajeitar ################################################################################################
    def confirmar_cadastro_cliente(self):
        nome = self.ent_Nome_Novo_Cliente.get()
        S_Nome= self.ent_Segundo_Nome_Novo_Cliente.get()
        cpf = self.ent_Cpf.get()
        lista_contas = []
        if nome == '' or S_Nome == '' or cpf == '':
            messagebox.showinfo('Aviso', 'Todos campos são obrigatórios', parent=self.Top_Cadastrar_Cliente)
        else:
            print(type(cpf))
            lista = []
            for i in cpf:
                lista.append(i)
            if len(lista) < 11 or len(lista) >11:
                messagebox.showinfo('Aviso', 'Preencha corretamente o campo do CPF!', parent=self.Top_Cadastrar_Cliente)
            else:
                pass


########################################################################################################################
#Atualização de Cliente ================================================================================================
    def Atualizar_Cliente(self):
        colunas = ['nome', 'segundo_nome', 'cpf']
        self.tvw = ttk.Treeview(self.janela, show='headings', columns=colunas, height=5)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text="Nome")
        self.tvw.heading('segundo_nome', text="Segundo Nome")
        self.tvw.heading('cpf', text="CPF")

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('segundo_nome', minwidth=0, width=150)
        self.tvw.column('cpf', minwidth=0, width=180)

        self.scr = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)
        self.tvw.insert('', 'end', values=(self.lista_de_nome, self.lista_de_S_nome, self.lista_de_cpf))
#Atulização de conta ===================================================================================================
    def atualizar_conta(self):
        self.top_atualizar_conta = tk.Toplevel()
        self.top_atualizar_conta.grab_set()
        self.top_atualizar_conta.title('Atualizar')
        self.top_atualizar_conta.geometry('300x200')
        self.lbl_nome = tk.Label(self.top_atualizar_conta, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_cpf = tk.Label(self.top_atualizar_conta, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0)


        self.ent_nome = tk.Entry(self.top_atualizar_conta, width=30)
        self.ent_nome.grid(row=0, column=1)

        self.ent_cpf = tk.Entry(self.top_atualizar_conta, width=30)
        self.ent_cpf.grid(row=1, column=1)


        self.btn_confirmar = tk.Button(self.top_atualizar_conta, text='Atualizar', command=self.confirmar_cadastro)
        self.btn_confirmar.grid(row=3, column=1)
############## Ajeitar ##################################################################################################
#Selecionando conta para atualizar
        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(self.janela, show='headings', columns=colunas, height=5)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text="Nome")
        self.tvw.heading('cpf', text="CPF")
        self.tvw.heading('email', text="Email")

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('email', minwidth=0, width=180)
        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, 'values')
        self.ent_nome.insert(0, lista[0])
        self.ent_cpf.insert(1, lista[1])

        self.btn_confirmar = tk.Button(self.top_atualizar_conta, text='Confirmar', command=self.confirmar_atualiza)
        self.btn_confirmar.grid(row=3, column=1)

    def confirmar_atualiza(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        saldo = 0
        selecionado = self.tvw.selection()
        self.tvw.item(selecionado, values=(nome, cpf, saldo))

        if self.btn_confirmar == True:
            self.tvw.item(selecionado, values=(nome, cpf, saldo))
            self.top_atualizar_conta.destroy()
            self.top_atualiza.destroy()
            self.janela.deiconify()
########################################################################################################################
#Indefinido ============================================================================================================
    def deletar_todos(self):
        todos = self.tvw.get_children()
        var = messagebox.askquestion('Cuidado','voce esta certo disso?')
        if var == 'yes':
            for t in todos:
                self.tvw.delete(t)

#Saques ================================================================================================================
    def Conta_Sacar(self):
        self.Conta_Sacar = tk.Toplevel()
        self.Conta_Sacar.grab_set()
        self.Conta_Sacar.title('Sacar')
        self.Conta_Sacar.geometry('300x150')

        self.lbl_saldo_sacar = tk.Label(self.Conta_Sacar, text='Saldo atual:')
        self.lbl_saldo_sacar.grid(row=0, column=0)
        self.lbl_info = tk.Label(self.Conta_Sacar, text='Atenção, sua conta estara sujeita a taxação!!!')
        self.lbl_info.grid(row=3, columnspan=2)

        self.lbl_ent_saldo_sacar = tk.Label(self.Conta_Sacar, text='Valor do Saque:')
        self.lbl_ent_saldo_sacar.grid(row=1, columnspan=1)
        self.ent_saldo_sacar = tk.Entry(self.Conta_Sacar, width=30)
        self.ent_saldo_sacar.grid(row=1, column=1)

# Selecionando a conta para depositar ==================================================================================
        selecionado = self.tvw.selection()
        if selecionado == '' or selecionado == 0:
            messagebox.showinfo('Aviso', 'O aaque não pode ser efetuado!!', parent=self.Conta_Sacar)
        else:
            lista = self.tvw.item(selecionado, 'values')
            self.teste = tk.Label(self.Conta_Sacar, text=f'{lista[2]}')
            self.teste.grid(row=0, column=1, sticky=tk.W)
            # self.ent_saldo_c.insert(2, lista[2])

        self.btn_confirmar = tk.Button(self.Conta_Sacar, text='Confirmar Saque', command=self.Confirmar_Saque)
        self.btn_confirmar.grid(row=4, column=1)

    def Confirmar_Saque(self):
        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, 'values')

        if self.btn_confirmar == True:
            lista = self.tvw.item(selecionado, 'values')
            self.ent_saldo_c.insert(self.ent_saldo_saque, lista[2])
            self.top_atualizar_conta.destroy()
            self.Conta_Sacar.destroy()
            self.janela.deiconify()

#Depositos =============================================================================================================
    def Conta_Depositar(self):
        self.Conta_Deposito = tk.Toplevel()
        self.Conta_Deposito.grab_set()
        self.Conta_Deposito.title('Depositar')
        self.Conta_Deposito.geometry('300x150')

        self.lbl_saldo_c = tk.Label(self.Conta_Deposito, text='Saldo atual:')
        self.lbl_saldo_c.grid(row=0, column=0)
        self.lbl_info = tk.Label(self.Conta_Deposito, text='Atenção Sua conta estara sujeita a taxação!!!')
        self.lbl_info.grid(row=3, columnspan=2)

        self.lbl_ent_saldo_c = tk.Label(self.Conta_Deposito, text='Valor de Deposito:')
        self.lbl_ent_saldo_c.grid(row=1, columnspan=1)
        self.ent_saldo_c = tk.Entry(self.Conta_Deposito, width=30)
        self.ent_saldo_c.grid(row=1, column=1)


        # Selecionando a conta para depositar
        selecionado = self.tvw.selection()
        if selecionado == '' or selecionado == 0:
            messagebox.showinfo('Aviso', 'O deposito não pode ser efetuado!!', parent=self.Conta_Deposito)
        else:
            lista = self.tvw.item(selecionado, 'values')
            self.teste = tk.Label(self.Conta_Deposito, text=f'{lista[2]}')
            self.teste.grid(row=0, column=1, sticky=tk.W)
            #self.ent_saldo_c.insert(2, lista[2])

        self.btn_confirmar = tk.Button(self.Conta_Deposito, text='Depositar', command=self.Confirmar_Deposito)
        self.btn_confirmar.grid(row=4, column=1)

    def Confirmar_Deposito(self):
        #nome = self.ent_nome.get()
        #cpf = self.ent_cpf.get()
        #saldo = self.ent_saldo_c.get()
        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, 'values')
        #=self.ent_saldo_c.insert(2, lista[2])

        if self.btn_confirmar == True:
            lista = self.tvw.item(selecionado, 'values')
            self.ent_saldo_c.insert(self.ent_saldo_c, lista[2])
            self.top_atualizar_conta.destroy()
            self.top_atualiza.destroy()
            self.janela.deiconify()

#Cadastro de Nova Conta ================================================================================================
    def tela_cadastrar_conta(self):
        self.top_cadastro_nova_conta = tk.Toplevel()
        self.top_cadastro_nova_conta.grab_set()
        self.top_cadastro_nova_conta.title('Cadastro de Nova Conta')
        self.top_cadastro_nova_conta.geometry('300x200')


        # Containers para utilizacao do .place e .grid
        self.container_1 = tk.Frame(self.top_cadastro_nova_conta)
        self.container_2 = tk.Frame(self.top_cadastro_nova_conta)

        self.container_1.grid(sticky=tk.N)
        self.container_2.grid(sticky=tk.S)

        self.radiobutton = tk.StringVar(self.container_2, "1")

        self.lbl_nome = tk.Label(self.container_1, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_cpf = tk.Label(self.container_1, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0)
        self.lbl_cpf = tk.Label(self.container_1, text='SENHA:')
        self.lbl_cpf.grid(row=2, column=0)

        self.lbl_cpf = tk.Label(self.container_2, text='Escolha o tipo de conta:')
        self.lbl_cpf.grid(row=3, column=0)
        self.rbt_1 = tk.Radiobutton(self.container_2, text='Conta Corrente', value='1', variable=self.radiobutton)
        self.rbt_2 = tk.Radiobutton(self.container_2, text='Conta Poupança', value='2', variable=self.radiobutton)
        self.rbt_1.grid()
        self.rbt_2.grid()



        self.ent_nome = tk.Entry(self.container_1, width=30)
        self.ent_nome.grid(row=0, column=1)
        self.ent_cpf = tk.Entry(self.container_1, width=30)
        self.ent_cpf.grid(row=1, column=1)
        self.ent_senha = tk.Entry(self.container_1, width=30)
        self.ent_senha.grid(row=2, column=1)

        self.btn_confirmar = tk.Button(self.top_cadastro_nova_conta, text='Confirmar', command=self.confirmar_cadastro)
        self.btn_confirmar.grid(row=5, column=0)
############### AJEITAR ################################################################################################
#Registro de uma nova conta ============================================================================================
    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        senha = self.ent_senha.get()
        check_1 = float(self.radiobutton.get())

        Saldo = 0
        if nome == '' or cpf == '' or senha == '':
            messagebox.showinfo('Aviso', 'Todos campos são obrigatórios', parent=self.top_cadastro_nova_conta)
        else:

            pass


########################################################################################################################
cli1 = Cliente('Manoel','L.',000000000000)

cli2 = Cliente('Carlos','A',111111111111)
c1 = Conta(1, cli1, 1000,'123')
c2 = Conta(2, cli2, 10,'123456')
c1.depositar(500)

c2.depositar(1200)


c1.sacar(2000)
c2.sacar(1000)
#c1.extrato.imprime()
print('===========')
#c2.extrato.imprime()
print('Saldo:{}'.format(c1.saldo))
print(type(cli1))
print(Conta.get_total_contas())


variavel = tk.Tk()
Painel(variavel)
variavel.mainloop()