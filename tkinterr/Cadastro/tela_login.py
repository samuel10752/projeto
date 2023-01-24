from tkinter import *
from tkinter import messagebox
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('750x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#NSEW
#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 0 / Widgets --------------------------#

#frX = LabelFrame(root, background='#fff', text='text', fg="gray", font='Georgia 15')
# X é o numero a ser substiuido pelo numero da sua flame

#lb0_frX = Label(frX, text="text", font='Georgia 15')
#Label padronizado
#bt0_frX = Button(frX, text="text", font='Georgia 15')
#Botão padronizado
#in0_frX = Entry(frX, font='Georgia 15')
#Entrada de dados (input) padronizado

#-------------------------- Frame 1 / Apresentar --------------------------#

#frX.grid()
#grid / para mostrar o flame
#lb0_frX.grid()
#grid / para mostrar o Label
#in0_frX.grid()
#grid / para mostrar a entrada de dados

#-------------------------- Mostrar tela --------------------------#

#root.mainloop()

#INÍCIO DO CÓDIGO

#Frame 0 - Gustavo

fr0 = LabelFrame (bg='#8a37cc')

lb0_fr0 = Label(fr0, text='Seja Muito Bem-Vindo', font = ("Mongolian Baiti", "32"),bg='#8a37cc', fg='#f5f5f5',).grid(row=0,column=0,columnspan=3, sticky=W,padx=165,ipady=120)
bt0_fr0 = Button(fr0, text='Funcionário', font=('Mongolian Baiti' ,'26', "bold"), bg='#eb8334',fg='#fff', width=10, command= lambda: [fr0.grid_remove(), fr1.grid(row=0, column=0, sticky=NSEW)]).grid(row=1, column=0,columnspan=1, sticky=W, padx=150)
bt1_fr0 = Button(fr0, text='Usuario', font= ('Mongolian Baiti' ,'26', "bold"),bg='#eb8334',fg='#fff',width=8, command= lambda: [fr0.grid_remove(), fr4.grid(row=0, column=0)]).grid(row=1, column=0,columnspan=2,sticky=W, padx=400)

fr0.grid(row=0, column=0, sticky=NSEW)

#Frame 1 - Samuel

#criar janela

fr1 = LabelFrame(bg= '#8a37cc',pady=90)

#criar os widgets

lb0_fr1 = Label(fr1, text='Login do Funcionário', font= ('Mongolian Baiti', '32'),bg='#8a37cc',fg='#f5f5f5').grid(row=0,column=1,sticky=W,padx=180,pady=30)
lb1_fr1 = Label(fr1, text='Usuário:', font=('Mongolian Baiti', '22'),bg='#8a37cc',fg='#f5f5f5').grid(row=1, column=1,sticky=W, padx=50)
lb2_fr1 = Label(fr1, text='Senha:', font=('Mongolian Baiti', "22" ),bg='#8a37cc',fg='#f5f5f5',width=7).grid(row=2, column=1,sticky=W, padx=50)

#--Entrada ---
int0_fr1 = Entry(fr1, font='Arial 18', width=35).grid(row=1,column=1,sticky=W,padx=154)
int1_fr1 = Entry(fr1, font='Arial 18', width=35,show="*").grid(row=2,column=1,sticky=W,padx=154)
#--Button ---
bt0_fr1 = Button(fr1,text='Entrar', font= ('Mongolian Baiti', "18", "bold") ,width=15,bg='#eb8334', fg='#fff').grid(row=4, column=1, sticky=W, padx=155)
bt1_fr1 = Button(fr1, text='Voltar', font=('Mongolian Baiti', "18", "bold"),width=15,bg='#eb8334', fg='#fff', command= lambda: [fr1.grid_remove(),fr0.grid(row=0, column=0)]).grid(row=4, column=1, sticky=E,padx=153)


#---Configuração do Frame---
#fr1.grid(row=0, column=0, sticky=NSEW)

#organizar os widgets

#--Entrada --

#---Butoon Função---

#executar a janel4

#Frame 2 - Breno

#fr2 = LabelFrame(root, background='#fff', text='Cadastro de fúncionarios', fg="gray", font='Georgia 15')
#lb0_fr2 = Label(fr2, text="Insira a seguir todos os dados requisitados para cadastro", font='Georgia 10')
#
##nome
#lb1_fr2 = Label(fr2, text="Nome:", font='Georgia 15')
#in0_frX = Entry(fr2, font='Georgia 15')
#
##cpf
#lb2_fr2 = Label(fr2, text="CPF:")
#in1_frX = Entry(fr2, font='Georgia 15')
#
##telefoneu
#lb3_fr2 = Label(fr2, text="Telefone:")
#in2_frX = Entry(fr2, font='Georgia 15')
#
##data de nascimento
#lb4_fr2 = Label(fr2, text="Data de Nasc:")
#in3_frX = Entry(fr2, font='Georgia 15')
#
##endereço 
#lb5_fr2 = Label(fr2, text="Endereço:")
#in4_frX = Entry(fr2, font='Georgia 15')
#
##cidade
#lb6_fr2 = Label(fr2, text="Cidade:")
#in5_frX = Entry(fr2, font='Georgia 15')
#
##numero da casa
#lb7_fr2 = Label(fr2, text="N°:")
#in6_frX = Entry(fr2, font='Georgia 15')
#
##Conclusão do formulario
#bt0_frX = Button(fr2, text="Salvar dados", font='Georgia 15')
#bt1_frX = Button(fr2, text="Voltar", font='Georgia 15')
#
##-------------------------- Frame 2 / Apresentar --------------------------#
#
#fr2.grid()
#
##Linha 0 
#lb0_fr2.grid(row=0, column=0)
#
##linha 1 
#lb1_fr2.grid()
#lb2_fr2.grid()
#lb3_fr2.grid()
#lb4_fr2.grid()
#lb5_fr2.grid()
#lb6_fr2.grid()
#lb7_fr2.grid()

#Frame 3 - Felipe

#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Usuário', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Ewerson Ribeiro Brandina', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#49A').grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=5, column=0, sticky=W)
bt6_fr4 = Button(fr4, text='Pix', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=6, column=0, sticky=W)
bt7_fr4 = Button(fr4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=14).grid(row=7, column=2, sticky=E)
#fr4.grid(row=0, column=0, sticky=NSEW)
#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Depósito', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_1 = Entry(fr4_1,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=38).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_1 = Button(fr4_1, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_1.grid()
#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Saque', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_2 = Button(fr4_2, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_2.grid()
#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Transferência', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_3 = Button(fr4_3, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_3.grid()
#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Extrato', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_4 = Label(fr4_4, text='PERIODO', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#49A').grid(row=0, column=1)
lb1_fr4_4 = Entry(fr4_4, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=27).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_4 = Button(fr4_4, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_4 = Button(fr4_4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_4.grid()















#Looping para tudo
root.mainloop()