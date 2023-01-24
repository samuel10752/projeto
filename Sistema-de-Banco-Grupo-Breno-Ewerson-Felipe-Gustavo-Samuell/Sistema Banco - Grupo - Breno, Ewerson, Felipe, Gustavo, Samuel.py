from operator import ne
from tkinter import *
from classe_cliente import *
from classe_conta import *
from datetime import datetime
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('750x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#8a37cc') #background color
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#Funções

#Deixar primeiras letras maiusculas - Cadastro Funcionário - in0_fr2
var =StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb7_fr2
var1 =StringVar()
def caps_1(*args):
    var1.set(var1.get().title())
var1.trace("w", caps_1)

#Deixar todas as letras maiusculas - lb8_fr2
var2 =StringVar()
def maiusculo(*args):
    var2.set(var2.get().upper())
var2.trace("w", maiusculo)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb6_fr2
var3 =StringVar()
def caps_2(*args):
    var3.set(var3.get().title())
var3.trace("w", caps_2)

#Deixar primeiras letras maiusculas - Cadastro Usuário - lb4_fr2
var4 =StringVar()
def caps_3(*args):
    var4.set(var4.get().title())
var4.trace("w", caps_3)

#Deixar primeiras letras maiusculas - Cadastro Usuário - in7_fr3_1
var5 =StringVar()
def caps_4(*args):
    var5.set(var5.get().title())
var5.trace("w", caps_4)

#Deixar todas as letras maiusculas - Cadastro Usuário - in8_fr3_1
var6 =StringVar()
def caps_5(*args):
    var6.set(var6.get().upper())
var6.trace("w", caps_5)

#Deixar as primeiras letras maiusculas - Cadastro Usuário -
var7 =StringVar()
def caps_6(*args):
    var7.set(var7.get().title())
var7.trace("w", caps_6)

#Tratar a Entrada de Valores em R$
def deposito(event=None):
    x = in0_fr4_1.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_1.delete(0, 'end')
    in0_fr4_1.insert(0, y)
def saque(event=None):
    x = in0_fr4_2.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_2.delete(0, 'end')
    in0_fr4_2.insert(0, y)
def transferencia(event=None):
    x = in0_fr4_3.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    in0_fr4_3.delete(0, 'end')
    in0_fr4_3.insert(0, y)
def extrato(event=None):
    x = in0_fr4_4.get().replace('/', '').replace('--','')[:12]
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1, 7]:
            y += x[i] + '/'
        elif i in [5]:
            y += x[i] + '--'
        else:
            y += x[i]
    in0_fr4_4.delete(0, 'end')
    in0_fr4_4.insert(0, y)
#CADASTRO FEITO PELO FUNCIONÁRIO
def cpf_funcionario(event=None):
    x=in1_fr2_1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in1_fr2_1.delete(0, 'end')
    in1_fr2_1.insert(0, y)
#def cpf_funcionario_login(event=None):
#    x=in0_fr1.get().replace('.','').replace('-', '')[:11]
#    y=''
#    if event.keysym.lower() == "backspace": return
#    for i in range(len(x)):
#        if x[i] in '0123456789':
#            if i in [2,5]:
#                y+=x[i] + '.'
#            elif i == 8:
#                y+=x[i] + '-'
#            else:
#                y+=x[i]
#    in0_fr1.delete(0, 'end')
#    in0_fr1.insert(0, y)
def telefone_funcionario(event=None):
    x=in3_fr2.get().replace('(','').replace(')', '').replace('-', '')[:12]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [0]:
            y+= '(' + x[i]
        elif i in [2]:
            y+= x[i] + ')'
        elif i in [3, 7]:
            y+= x[i] + '-'
        else:
            y+=x[i]
    in3_fr2.delete(0, 'end')
    in3_fr2.insert(0, y)
def data_nasc(event=None):
    x=in2_fr2.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in2_fr2.delete(0, 'end')
    in2_fr2.insert(0, y)
def dois_digitos_funcionario(event=None):
    x=lb8_fr2.get().replace(' ','')[:2]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789':
            y+=x[i]
    lb8_fr2.delete(0, 'end')
    lb8_fr2.insert(0, y)
def numeros_funcionario(event=None):
    x=lb5_fr2.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y+=x[i]
    lb5_fr2.delete(0, 'end')
    lb5_fr2.insert(0, y)

#CADASTRO FEITO PELO USUÁRIO
def cpf_cliente(event=None):
    x=in4_fr3_1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in4_fr3_1.delete(0, 'end')
    in4_fr3_1.insert(0, y)
def cpf_cliente_login(event=None):
    x=in0_fr3.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in0_fr3.delete(0, 'end')
    in0_fr3.insert(0, y)
def data_nasc1(event=None):
    x=in3_fr3_1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in3_fr3_1.delete(0, 'end')
    in3_fr3_1.insert(0, y)
def telefone_cliente(event=None):
    x=in5_fr3_1.get().replace('(','').replace(')', '').replace('-', '')[:12]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [0]:
            y+= '(' + x[i]
        elif i in [2]:
            y+= x[i] + ')'
        elif i in [3, 7]:
            y+= x[i] + '-'
        else:
            y+=x[i]
    in5_fr3_1.delete(0, 'end')
    in5_fr3_1.insert(0, y)
def dois_digitos_cliente(event=None):
    x=in8_fr3_1.get().replace(' ','')[:2]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789':
            y+=x[i]
    in8_fr3_1.delete(0, 'end')
    in8_fr3_1.insert(0, y)
def numeros_cliente(event=None):
    x=in9_fr3_1.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y+=x[i]
    in9_fr3_1.delete(0, 'end')
    in9_fr3_1.insert(0, y)
#Front & Back
V_Cadastro = []
V_Conta = []
V_Cpf = []
V_Senha = []
contagem=0
numero_conta = 0
def confirmar_funcionario():
    global numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if len(in0_fr2.get()) > 0 and len(in1_fr2_1.get()) == 14 and len(in2_fr2.get()) == 10 and len(in3_fr2.get()) == 16 and len(in10_fr2.get()) > 0:
        V_Cadastro.append(Cliente(nome=in0_fr2.get(), cpf=in1_fr2_1.get(), dataNasc=in2_fr2.get(), tel=in3_fr2.get(), uf=lb8_fr2.get(), logradouro=lb4_fr2.get(), numero=lb5_fr2.get(), bairro=lb6_fr2.get(), cidade=lb7_fr2.get(), email=in9_fr2.get(), senha=in10_fr2.get()))
        V_Cpf.append(in1_fr2_1.get())
        V_Senha.append(in10_fr2.get())
        V_Conta.append(Conta(V_Cadastro[contagem], '00'+str(numero_conta+1)))
        contagem += 1
        numero_conta += 1
        lb15_fr2['text'] = 'A Conta Foi Criada Com Sucesso.'
        in0_fr2.delete(0, 'end'), in1_fr2.delete(0, 'end'), in1_fr2_1.delete(0, 'end'), in2_fr2.delete(0,'end'), in3_fr2.delete(0, 'end'), lb4_fr2.delete(0, 'end'), lb5_fr2.delete(0, 'end'), lb6_fr2.delete(0, 'end'), lb7_fr2.delete(0,'end'), lb8_fr2.delete(0, 'end'), in9_fr2.delete(0, 'end'), in10_fr2.delete(0, 'end')
    else:
        lb15_fr2['text']='Erro Ao Preencher Algum Campo.'
login_aprovado=0
def confirmar_usuario():
    global numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    V_Cadastro.append(Cliente(nome=in2_fr3_1.get(), cpf=in4_fr3_1.get(), dataNasc=in3_fr3_1.get(), tel=in5_fr3_1.get(), uf=in8_fr3_1.get(), logradouro=in6_fr3_1.get(), numero=in9_fr3_1.get(), bairro=in14_fr3_1.get(), cidade=in7_fr3_1.get(), email=in10_fr3_1.get(), senha=in15_fr3_1.get()))
    V_Cpf.append(in4_fr3_1.get())
    V_Senha.append(in15_fr3_1.get())
    V_Conta.append(Conta(V_Cadastro[contagem], '00'+str(contagem+1)))
    contagem +=1
login_aprovado=0
def login_cliente():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if len(V_Conta) == 0:
        lb16_fr3['text'] = 'Usuário ou Senha Incorretos'
    for i in range(len(V_Cadastro)):
        if in0_fr3.get() == V_Cpf[i] and in1_fr3.get() == V_Senha[i]:
            in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), lb16_fr3.grid_remove(), fr3.grid_remove(), fr4.grid(row=0, column=0)
            login_aprovado = i
            lb0_fr4['text']=V_Conta[login_aprovado].titular
            lb0_1_fr4['text']='Num. Conta: '+ V_Conta[login_aprovado].num
            lb1_fr4['text']='R$ '+str(V_Conta[login_aprovado].saldo)
            break
        else:
            lb16_fr3['text']='Usuário ou Senha Incorretos'
            print('Usuário ou Senha incorretos')
def login_funcionário():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if in0_fr1.get() == 'adm' and in1_fr1.get() == 'adm':
        in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr2.grid(row=0, column=0)
        print('Usuário e Senha Corretos')
    else:
        print('Usuário e Senha Incorretos')
def mostrar_contas():
    x=''
    for i in range(len(V_Conta)):
        x += f'------------0{i+1}-------------\nTitular: {str(V_Conta[i].titular)}\nConta: {str(V_Conta[i].num)}\nSaldo: {str(V_Conta[i].saldo)}\n'
        lb0_fr2_3['text'] = x
def apagar_conta():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if len(V_Conta) == 0:
        lb3_fr2_2['text'] = 'Conta ou Senha Errada'
    for i in range(len(V_Conta)):
            if V_Conta[i].num == in0_fr2_1.get() and in1_fr2.get() == 'adm':
                   if V_Conta[i].saldo == 0:
                       V_Cpf.pop(i)
                       V_Senha.pop(i)
                       V_Cadastro.pop(i)
                       V_Conta.pop(i)
                       lb3_fr2_2['text']='Conta Excluida Com Sucesso'
                       contagem -= 1
                       break
                   else:
                       lb3_fr2_2['text'] = 'Erro. Conta Contem Saldo'
                       break
            else:
                lb3_fr2_2['text']='Conta ou Senha Errada'
def deposito_calculo():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if V_Senha[login_aprovado] == in1_fr4_1.get():
        data = datetime.now()
        data_em_texto = data.strftime('%d/%m/%Y %H:%M')
        data = data_em_texto
        V_Conta[login_aprovado].deposito(float(in0_fr4_1.get()),str(data))
        V_Conta[login_aprovado].extrato()
        lb3_fr4_1['text']='Depósito de R$ '+ str(in0_fr4_1.get())+ ' Realizado Com Sucesso'
        lb1_fr4['text']='R$ '+str(V_Conta[login_aprovado].saldo)
    else:
        lb3_fr4_1['text'] = 'Senha Errada'
def saque_calculo():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if V_Senha[login_aprovado] == in1_fr4_2.get():
        if V_Conta[login_aprovado].saldo < float(in0_fr4_2.get()):
            lb3_fr4_2['text'] = 'Saldo insuficiente'
        else:
            data = datetime.now()
            data_em_texto = data.strftime('%d/%m/%Y %H:%M')
            data = data_em_texto
            V_Conta[login_aprovado].saque(float(in0_fr4_2.get()),str(data))
            V_Conta[login_aprovado].extrato()
            lb3_fr4_2['text'] = 'Saque de R$ '+ str(in0_fr4_2.get())+ ' Realizado Com Sucesso'
            lb1_fr4['text']='R$ '+str(V_Conta[login_aprovado].saldo)
    else:
        lb3_fr4_2['text'] = 'Senha Errada'
def transfere_calculo():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    if V_Senha[login_aprovado] == in1_fr4_3.get():
        if in0_fr4_3.get().isdigit():
            if V_Conta[login_aprovado].saldo < float(in0_fr4_3.get()):
                lb3_fr4_3['text'] = 'Saldo insuficiente'
            else:
                for i in range (len(V_Conta)):
                        if V_Conta[i].num == in1_1_fr4_3.get():
                            data = datetime.now()
                            data_em_texto = data.strftime('%d/%m/%Y %H:%M')
                            data = data_em_texto
                            V_Conta[login_aprovado].transfere(float(in0_fr4_3.get()),V_Conta[i], data)
                            V_Conta[i].recebe_transferencia(float(in0_fr4_3.get()), V_Conta[login_aprovado], data)
                            V_Conta[login_aprovado].extrato()
                            V_Conta[i].extrato()
                            lb3_fr4_3['text'] = 'Transferência de R$ '+ str(in0_fr4_3.get())+ ' Realizado Com Sucesso'
                            lb1_fr4['text']='R$ '+str(V_Conta[login_aprovado].saldo)
                            break
                        else:
                            lb3_fr4_3['text'] = 'Conta Destino Errada'
        else:
            lb3_fr4_3['text'] = 'Valor Não Inserido'
    else:
        lb3_fr4_3['text'] = 'Senha Errada'
vetor=[]
vetor1=[]
def extrato_calculo():
    global login_aprovado, numero_conta, contagem, V_Cadastro, V_Conta, V_Cpf, V_Senha, nome, cpf, dataNasc, tel, uf, logradouro, numero, bairro, cidade, email, senha
    vetor.append(V_Conta[login_aprovado].extrato())
    vetor1.append(in0_fr4_3.get())
    if len(vetor) != 0:
        if len(vetor1) != 0:
            if V_Senha[login_aprovado] == in1_fr4_4.get():
                lb7_fr4['text']=V_Conta[login_aprovado].historico.msg
                lb3_fr4_4['text'] = 'Extrato Exibido na Tela Inicial'
            else:
                lb3_fr4_4['text'] = 'Senha Errada'
        else:
            lb3_fr4_4['text'] = 'Valor Não Inserido'
    else:
        lb3_fr4_4['text'] = 'Nenhuma Movimentação Realizada'
hello=StringVar()
def mostrar(*args):
    in1_fr1 = Entry(fr1, textvariable=hello, font='Arial 18', width=35).grid(row=2,column=1,sticky=W,padx=154)
    feecho = Button(fr1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=esconder).grid(row=2, column=1, padx=617) #Atualizado
def esconder(*args):
    in1_fr1 = Entry(fr1, textvariable=hello, font='Arial 18', width=35, show="*").grid(row=2,column=1,sticky=W,padx=154)
    bt2_fr1 = Button(fr1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar).grid(row=2, column=1, padx=617) #Atualizado

hello_1=StringVar()
def mostrar_1(*args):
    in1_fr3 = Entry(fr3, textvariable=hello_1, font='Arial 20', bg='#fff').grid(row=3, column=0,sticky=W,padx=240,pady=10)
    feecho = Button(fr3, text='👁', font=('Mongolian Baiti', "15", "bold"),bg='#eb8334', fg='#fff',command=esconder_1).grid(row=3, column=0, sticky=W,padx=550,pady=5)
def esconder_1(*args):
    in1_fr3 = Entry(fr3, textvariable=hello_1, font='Arial 20', bg='#fff',show="*").grid(row=3, column=0,sticky=W,padx=240,pady=10)
    bt7_fr3 = Button(fr3, text='👁', font=('Mongolian Baiti', "15", "bold"),bg='#eb8334', fg='#fff',command=mostrar_1).grid(row=3, column=0, sticky=W,padx=550,pady=5)

hello_2=StringVar()
def mostrar_2(*args):
    in1_fr2 = Entry(fr2_2, textvariable=hello_2, font=('Arial 16'), bg="#f5f5f5", width=30).grid(row=3, column=0,sticky=W,padx=195)
    feecho = Button(fr2_2, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff',command=esconder_2).grid(row=3, column=0, sticky=W,padx=563,pady=5)
def esconder_2(*args):
    in1_fr2 = Entry(fr2_2, textvariable=hello_2, font=('Arial 16'), bg="#f5f5f5", width=30,show="*").grid(row=3, column=0,sticky=W,padx=195)
    bt2_fr2 = Button(fr2_2, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff', command=mostrar_2).grid(row=3, column=0, sticky=W,padx=563,pady=5)

hello_3=StringVar()
def mostrar_3(*args):
    in1_fr4_1 = Entry(fr4_1, textvariable=hello_3,font='Arial 20', bg='#f5f5f5').grid(row=1, column=0,sticky=W,padx=280) #implementado deposito
    feecho = Button(fr4_1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=esconder_3).grid(row=1, column=0, sticky=W,padx=588,pady=5)
def esconder_3(*args):
    in1_fr4_1 = Entry(fr4_1, textvariable=hello_3,font='Arial 20', bg='#f5f5f5',show="*").grid(row=1, column=0,sticky=W,padx=280) #implementado botão deposito
    bt5_fr4_1 = Button(fr4_1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=mostrar_3).grid(row=1, column=0, sticky=W,padx=588,pady=5)

hello_4=StringVar()
def mostrar_4(*args):
    in1_fr4_2 = Entry(fr4_2, font='Arial 20', textvariable=hello_4, bg='#f5f5f5').grid(row=1, column=0,sticky=W,padx=280) #implementado saque
    feecho = Button(fr4_2, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=esconder_4).grid(row=1, column=0, sticky=W,padx=588,pady=5)
def esconder_4(*args):
    in1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#f5f5f5', textvariable=hello_4,show="*").grid(row=1, column=0,sticky=W,padx=280) #implementado botao saque
    bt5_fr4_2 = Button(fr4_2, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_4).grid(row=1, column=0, sticky=W,padx=588,pady=5)

hello_5=StringVar()
def mostrar_5(*args):
    in1_fr4_3 = Entry(fr4_3, textvariable=hello_5, font=('Arial 20'), bg="#f5f5f5").grid(row=2, column=0, sticky=W,padx=280) #implementado transferencia
    feecho = Button(fr4_3, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=esconder_5).grid(row=2, column=0, sticky=W,padx=588,pady=5)
def esconder_5(*args): 
    in1_fr4_3 = Entry(fr4_3, textvariable=hello_5, font=('Arial 20'), bg="#f5f5f5",show="*").grid(row=2, column=0, sticky=W,padx=280) #implementado dbotão transferencia
    bt5_fr4_3 = Button(fr4_3, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=mostrar_5).grid(row=2, column=0, sticky=W,padx=588,pady=5)

hello_6=StringVar()
def mostrar_6(*args):
    in1_fr4_4= Entry(fr4_4, textvariable=hello_6, font=('Arial 20'), bg="#f5f5f5").grid(row=1, column=0,sticky=W,padx=280) #implementado Extrato
    feecho = Button(fr4_4, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff',command=esconder_6).grid(row=1, column=0, sticky=W,padx=588,pady=5)
def esconder_6(*args):
    in1_fr4_4 = Entry(fr4_4, textvariable=hello_6, font=('Arial 20'), bg="#f5f5f5", show="*").grid(row=1, column=0,sticky=W,padx=280) #implementado Botão Extrato
    bt5_fr4_4 = Button(fr4_4, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_6).grid(row=1, column=0, sticky=W,padx=588,pady=5)        



def mensagem():
    lb3_fr4_1['text'] = 'Mensagem de Confirmação'
    lb3_fr4_2['text'] = 'Mensagem de Confirmação'
    lb3_fr4_3['text'] = 'Mensagem de Confirmação'
    lb3_fr4_4['text'] = 'Mensagem de Confirmação'

#Salvar os Usuários e Senhas de cada frame

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

#INÍCIO DO CÓDIGO
#Frame 0 - Gustavo
# Atualizadp toda a tela 

fr0 = LabelFrame (bg='#8a37cc')
lb0_fr0 = Label(fr0, text='Seja muito Bem-Vindo', font = ("Mongolian Baiti", "32"),bg='#8a37cc', fg='#f5f5f5',).grid(row=0,column=0, sticky=W,padx=170,ipady=60)
lb1_fr0 = Label(fr0, text='ao Nubank', font=("Mongolian Baiti", "32"), bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0, sticky=W,ipadx=300) #Atualizado o texto
bt0_fr0 = Button(fr0, text='Funcionário', font=('Mongolian Baiti' ,'26', "bold"), bg='#eb8334',fg='#fff', width=10, command= lambda: [fr0.grid_remove(), fr1.grid(row=0, column=0, sticky=NSEW)]).grid(row=2, column=0,columnspan=1, sticky=W, padx=165,pady=70)
bt1_fr0 = Button(fr0, text='Usuário', font= ('Mongolian Baiti' ,'26', "bold"),bg='#eb8334',fg='#fff',width=8, command= lambda: [fr0.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=2, column=0,columnspan=2,sticky=W, padx=415)
fr0.grid(row=0, column=0, sticky=NSEW)

#Frame 1 - Samuel
#criar janela

fr1 = LabelFrame(bg= '#8a37cc',pady=90)
#criar os widgets
lb0_fr1 = Label(fr1, text='Login do Funcionário', font= ('Mongolian Baiti', '32'),bg='#8a37cc',fg='#f5f5f5').grid(row=0,column=1,sticky=W,padx=180,pady=30)
lb1_fr1 = Label(fr1, text='User:', font=('Mongolian Baiti', '22'),bg='#8a37cc',fg='#f5f5f5').grid(row=1, column=1,sticky=W, padx=83)
lb2_fr1 = Label(fr1, text='Senha:', font=('Mongolian Baiti', "22" ),bg='#8a37cc',fg='#f5f5f5',width=7).grid(row=2, column=1,sticky=W, padx=50)
#--Entrada ---
in0_fr1 = Entry(fr1, font='Arial 18', width=35)
#in0_fr1.bind('<KeyRelease>', cpf_funcionario_login)
in0_fr1.grid(row=1,column=1,sticky=W,padx=154)
in1_fr1 = Entry(fr1, textvariable=hello, font='Arial 18', width=35,show="*")
in1_fr1.grid(row=2,column=1,sticky=W,padx=154)
#--Button ---
bt0_fr1 = Button(fr1,text='Entrar', font= ('Mongolian Baiti', "18", "bold") ,width=15,bg='#eb8334', fg='#fff',command= lambda: [login_funcionário()]).grid(row=4, column=1, sticky=W, padx=155)
bt1_fr1 = Button(fr1, text='Voltar', font=('Mongolian Baiti', "18", "bold"),width=16,bg='#eb8334', fg='#fff', command= lambda: [in0_fr1.delete(0, 'end'), in1_fr1.delete(0, 'end'), fr1.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=4, column=1, sticky=W,padx=380)
bt2_fr1 = Button(fr1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar).grid(row=2, column=1, padx=617) #Atualizado o tamanho do Botão
#---Configuração do Frame---
#fr1.grid()

#Frame 2 - Breno

#-------------------------- Frame 2 --------------------------#

fr2 = LabelFrame(root, bg="#8a37cc")

#Infos
lb0_fr2 = Label(fr2, text="Bem Vindo a Home Dos Funcionarios", font=("Mongolian Baiti", "32"),background="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, columnspan=6, padx=50, sticky=W)
lb1_fr2 = Label(fr2, text="FUNCIONÁRIO", font=("Mongolian Baiti", "20"), background="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, columnspan=6, sticky=W, pady=10,padx=300)
#lb1_fr2 o label acima se possivel é pra ser usado pra mostrar o nome do usuario registrado, ou sej aretirando o nome Breno Depois durante a finalização
lb2_fr2 = Label(fr2, text="Avisos:", font=("Mongolian Baiti", "17", "bold"),background="#8a37cc", fg="#f5f5f5").grid(row=3, column=0,sticky=W,padx=350)
lb3_fr2 = Label(fr2, text="Nenhuma atualização relevante no sistema ", font=("Mongolian Baiti", "15"),background="#8a37cc", fg="#f5f5f5").grid(row=4, column=0, sticky=W,padx=220, pady=10
)
#Botões
bt0_fr2 = Button(fr2, text="Sair", font=("Mongolian Baiti", "16", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda: [fr2.grid_remove(), fr1.grid(row=0, column=0)] ).grid(row=7, column=0,sticky=W,padx=260) #Atualizado o texto 
bt0_1_fr2 = Button(fr2, text="Ver Contas Cadastradas", font=("Mongolian Baiti", "16", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda: [fr2.grid_remove(), fr2_3.grid(row=0,column=0), mostrar_contas()] ).grid(row=6, column=0,sticky=W,padx=100,pady=20)
bt1_fr2 = Button(fr2, text="Cadastrar Novo Cliente", font=("Mongolian Baiti", "16", "bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda:[fr2.grid_remove(), fr2_1.grid(row=0,column=0)] ).grid(row=5,column=0,sticky=W,padx=100)
bt3_fr2 = Button(fr2, text="Excluir Usuários", font=("Mongolian Baiti", "16"," bold"), height=2,width=20, bg="#eb8334", fg="#fff", command= lambda:[fr2.grid_remove(), fr2_2.grid(row=0,column=0)]).grid(row=5, column=0,columnspan=2,sticky=W,padx=400)  #Atualizado o texto
bt0_fr2 = Button(fr2, text="Editar Usuário", font=("Mongolian Baiti", "16", "bold"), height=2,width=20, bg="#eb8334", fg="#fff").grid(row=6, column=0,sticky=W,padx=400,pady=20) #Atualizado o texto e botão
fr2_1 = LabelFrame(root, bg="#8a37cc") #grid(row=0, column=0)
lb0_fr2_1 = Label(fr2_1, text="Faça aqui o cadastro de novos Clientes", font=("Mongolian Baiti", "20"),background="#8a37cc", fg="#f5f5f5").grid(row=0, column=0,sticky=W,pady=60,padx=165)

#Linha 1 Atualizado o texto e a entrar
llb1_fr2 = Label(fr2_1, text="Nome*:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=1, column=0, sticky=W,padx=45)
in0_fr2 = Entry(fr2_1, font=('Arial 15'), textvariable=var,width=52, bg="#f5f5f5")
in0_fr2.grid(row=1, column=0, columnspan=1, sticky=W,padx=122)

#Linha 2 Atualizado o texto e a entrar
b2_fr2 = Label(fr2_1, text="CPF*:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=2, column=0, sticky=W,padx=60)
in1_fr2_1 = Entry(fr2_1, font=('Arial 15'), bg="#f5f5f5",width=22)
in1_fr2_1.bind('<KeyRelease>', cpf_funcionario)
in1_fr2_1.grid(row=2, column=0, sticky=W,padx=122)
lb3_fr2 = Label(fr2_1, text="Data Nasc*:", font=("Mongolian Baiti", "16"),background="#8a37cc", fg="#f5f5f5" )
lb3_fr2.grid(row=2, column=0,sticky=W,padx=369)
in2_fr2 = Entry(fr2_1, font=('Arial 15'),width=20, bg="#f5f5f5", cursor="gobbler")
in2_fr2.bind('<KeyRelease>', data_nasc)
in2_fr2.grid(row=2, column=0, sticky=W,padx=474)

#Linha 3 Atualizado o texto e a entrar
lb4_fr2 = Label(fr2_1, text="Tel*:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column=0, sticky=W,padx=70)
in3_fr2 = Entry(fr2_1, font=('Arial 15'), bg="#f5f5f5",width=22)
in3_fr2.bind('<KeyRelease>', telefone_funcionario)
in3_fr2.grid(row=3, column=0, sticky=W,padx=122)
lb5_fr2 = Label(fr2_1, text="Logradouro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0, sticky=W,padx=0)
lb4_fr2 = Entry(fr2_1, font=('Arial 15'),textvariable=var4, bg="#f5f5f5",width=22)
lb4_fr2.grid(row=4, column=0, sticky=W,padx=122)
lb6_fr2 = Label(fr2_1, text="N°:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=4, column=0,sticky=W,padx=440)
lb5_fr2 = Entry(fr2_1, font=('Arial 15'), bg="#f5f5f5")
lb5_fr2.bind('<KeyRelease>', numeros_funcionario)
lb5_fr2.grid(row=4, column=0,sticky=W,padx=474)

#linha 5 Atualizado o texto e a entrar
lb7_fr2 = Label(fr2_1, text="Bairro:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0, sticky=W,padx=53)
lb6_fr2 = Entry(fr2_1, font=('Arial 15'), textvariable=var3, bg="#f5f5f5",width=22)
lb6_fr2.grid(row=5, column=0, sticky=W,padx=122)
lb8_fr2 = Label(fr2_1, text="Cidade:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=5, column=0,sticky=W,padx=399)
lb7_fr2 = Entry(fr2_1, font=('Arial 15'), textvariable=var1, bg="#f5f5f5")
lb7_fr2.grid(row=5, column=0, sticky=W,padx=474)
lb9_fr2 = Label(fr2_1, text="UF:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=3, column = 0,sticky=W,padx=435)
lb8_fr2 = Entry(fr2_1, font=('Arial 15'), textvariable=var2, bg="#f5f5f5")
lb8_fr2.bind('<KeyRelease>', dois_digitos_funcionario)
lb8_fr2.grid(row=3, column=0, sticky=W,padx=474)
lb10_fr2 = Label(fr2_1, text="Email:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0, sticky=W,padx=58)
in9_fr2 = Entry(fr2_1, font=('Arial 15'), bg="#f5f5f5",width=22)
in9_fr2.grid(row=6, column=0, sticky=W,padx=122)
lb11_fr2 = Label(fr2_1, text="Senha*:", font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" ).grid(row=6, column=0,sticky=W,padx=395)
in10_fr2 = Entry(fr2_1, font=('Arial 15'), bg="#f5f5f5")
in10_fr2.grid(row=6, column=0, sticky=W,padx=474)

# Botões
bt0_fr2 = Button(fr2_1, text="Criar conta ", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[confirmar_funcionario()]).grid(row=8, column=0, sticky=W,pady=20,padx=119)
bt1_fr2 = Button(fr2_1, text="Voltar", font=("Mongolian Baiti", "17", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[in0_fr2.delete(0,'end'),in1_fr2.delete(0,'end'), in1_fr2_1.delete(0,'end'), in2_fr2.delete(0,'end'),in3_fr2.delete(0,'end'),lb4_fr2.delete(0,'end'),lb5_fr2.delete(0,'end'),lb6_fr2.delete(0,'end'),lb7_fr2.delete(0,'end'),lb8_fr2.delete(0,'end'),in9_fr2.delete(0,'end'),in10_fr2.delete(0,'end'), fr2_1.grid_remove(), fr2.grid(row=0, column=0)]).grid(row=8, column=0, sticky=W,padx=455)
lb15_fr2 = Label(fr2_1, text='',font=("Mongolian Baiti", "17"),background="#8a37cc", fg="#f5f5f5" )
lb15_fr2.grid(row=9, column=0, sticky=W,padx=245)
#bt2_fr2 = Button(fr2_1, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff').grid(row=6, column=0, sticky=W,padx=712)
#Frame 2_2

fr2_2 = LabelFrame(root, bg="#8a37cc",padx = 100)
lb0_fr2_2 = Label(fr2_2, text="Faça aqui a exclusão de usuarios", font=("Mongolian Baiti", "25"),bg="#8a37cc", fg="#f5f5f5").grid(row=1, column=0, sticky=W, padx=70,pady=30)
lb1_fr2_2 = Label(fr2_2, text="Numero da conta:", font=("Mongolian Baiti", "17"),bg="#8a37cc", fg="#f5f5f5").grid(row=2, column=0, sticky=W,padx=24)
in0_fr2_1 = Entry(fr2_2, font=('Arial 16'), bg="#f5f5f5", width=30)
in0_fr2_1.grid(row=2, column=0, sticky=W,padx=195)
lb2_fr2_2 = Label(fr2_2, text="Confirme sua senha:", font=("Mongolian Baiti", "17"),bg="#8a37cc", fg="#f5f5f5").grid(row=3, column=0, sticky=W)
in1_fr2 = Entry(fr2_2, textvariable=hello_2, font=('Arial 16'), bg="#f5f5f5", width=30,show="*")
in1_fr2.grid(row=3, column=0,sticky=W,padx=195)
lb3_fr2_2 = Label(fr2_2, text='',font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5')
lb3_fr2_2.grid(row=4, column=0,sticky=W,padx=195)

# Botões
bt0_fr2 = Button(fr2_2, text="Deletar conta ", font=("Mongolian Baiti", "19", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[apagar_conta()]).grid(row=5, column=0, sticky=W, padx=40,pady=30) #Pura Gambiarra e ta tudo bem
bt1_fr2 = Button(fr2_2, text="Voltar", font=("Mongolian Baiti", "19", "bold"),width=18, bg="#eb8334", fg="#fff", command= lambda:[lb3_fr2_2.grid_remove(), in0_fr2.delete(0,'end'),in0_fr2_1.delete(0,'end'),in1_fr2.delete(0,'end'), in1_fr2_1.delete(0,'end'), fr2_2.grid_remove(), fr2.grid(row=0,column=0)]).grid(row=5, column=0, sticky=W, padx=330)
bt2_fr2 = Button(fr2_2, text='👁', font=('Mongolian Baiti', "12", "bold"),bg='#eb8334', fg='#fff',command=mostrar_2).grid(row=3, column=0, sticky=W,padx=563,pady=5) #Atualizado o Botão
#grid(row=0, column=0,pady=50, padx=150)

#Frame 2_3
fr2_3 = LabelFrame(root, bg="#8a37cc")
lb0_fr2_3 = Label(fr2_3, text='Todas As Contas', font='Arial 15',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5')
lb0_fr2_3.grid(row=0, column=0)
bt0_fr2_3 = Button(fr2_3, text='Voltar', font='Arial 15', bg='#8a37cc',fg='#f5f5f5', command= lambda: [fr2_3.grid_remove(), fr2.grid(row=0,column=0)]).grid(row=0, column=1, sticky=NE)


#Frame 3 - Felipe - FALTA BAIRRO E SENHA
#criando janela
fr3 = LabelFrame(root, text='Login / Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5',pady=30)
fr3_1 = LabelFrame(root, text='Cadastro',font=('Mongolian Baiti', '17'), bg='#8a37cc',fg='#f5f5f5')
#criando widgets
#lb0_fr3 = Label(fr3, text='Bem Vindo ao Dellux', font='Arial 20', background='#10929c', foreground='#f5f5f5').grid(row=0, column=0, sticky=NSEW)
#lb1_fr3 = Label(fr3, text='O que deseja fazer?', font='Arial 20', background='#10929c', foreground='#f5f5f5').grid(row=1, column=0, sticky=NSEW)
lb2_fr3 = Label(fr3, text='CPF:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=170)
lb3_fr3 = Label(fr3, text='Senha:', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5').grid(row=3, column=0, sticky=W,padx=149)
in0_fr3 = Entry(fr3, font='Arial 20', bg='#fff')
in0_fr3.bind('<KeyRelease>', cpf_cliente_login) #Usuário
in0_fr3.grid(row=2, column=0,sticky=W,padx=240)
in1_fr3 = Entry(fr3, textvariable=hello_1, font='Arial 20', bg='#fff',show="*") #Senha
in1_fr3.grid(row=3, column=0,sticky=W,padx=240,pady=10)
#widgets j2
lb4_fr3_1 = Label(fr3_1, text='Bem vindo a área de cadastro', font=('Mongolian Baiti', '22'), bg='#8a37cc', fg='#f5f5f5').grid(row=0, column=0,sticky=W, padx=193,pady=20)
lb5_fr3_1 = Label(fr3_1, text='Nome:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=1, column=0,sticky=W, padx=67)
lb6_fr3_1 = Label(fr3_1, text='Data de Nasc:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W)
lb7_fr3_1 = Label(fr3_1, text='CPF:', font=('Mongolian Baiti', '17'), bg='#8a37cc', fg='#f5f5f5').grid(row=2, column=0,sticky=W, padx=441)
lb8_fr3_1 = Label(fr3_1, text='Telefone:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W, padx=400)
lb9_fr3_1 = Label(fr3_1, text='Logradouro:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W,padx=10)
lb10_fr3_1 = Label(fr3_1, text='Cidade:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W,padx=56)
lb11_fr3_1 = Label(fr3_1, text='UF:',font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=4, column=0,sticky=W, padx=453)
lb12_fr3_1 = Label(fr3_1, text='N°:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=5, column=0,sticky=W, padx=457)
lb13_fr3_1 = Label(fr3_1, text='Email:', font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=6, column=0,sticky=W,padx=66)


lb14_fr3_1 = Label(fr3_1, text="Bairro:", font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=3, column=0,sticky=W,padx=62)
in14_fr3_1 = Entry(fr3_1,  font= ('Arial 16'),width=22, bg='#f5f5f5')
in14_fr3_1.grid(row=3, column=0, sticky=W,padx=132) #Bairro
lb15_fr3_1 = Label(fr3_1, text="Senha:", font=('Mongolian Baiti', '17'), bg='#8a37cc', foreground='#f5f5f5').grid(row=6, column=0,sticky=W, padx=425)
in15_fr3_1 = Entry(fr3_1, font= ('Arial 16'), bg='#f5f5f5')
in15_fr3_1.grid(row=6, column=0, sticky=W,padx=492) #Senha


in2_fr3_1 = Entry(fr3_1, font= ('Arial 16'),textvariable=var ,width=50, bg='#f5f5f5')
in2_fr3_1.grid(row=1, column=0, sticky=W,padx=132) #NOME OK
in3_fr3_1 = Entry(fr3_1, font= ('Arial 16'),width=22, bg='#f5f5f5')
in3_fr3_1.bind('<KeyRelease>', data_nasc1)
in3_fr3_1.grid(row=2, column=0, sticky=W,padx=132) #DATA NASC OK
in4_fr3_1 = Entry(fr3_1, font= ('Arial 16'), bg='#f5f5f5')
in4_fr3_1.bind('<KeyRelease>', cpf_cliente)
in4_fr3_1.grid(row=2, column=0, sticky=W,padx=492) #CPF OK
in5_fr3_1 = Entry(fr3_1,  font= ('Arial 16'), bg='#f5f5f5')
in5_fr3_1.bind('<KeyRelease>', telefone_cliente)
in5_fr3_1.grid(row=3, column=0, sticky=W,padx=492) #TELEFONE OK
in6_fr3_1 = Entry(fr3_1,  font= ('Arial 16'), textvariable=var7,width=22, bg='#f5f5f5')
in6_fr3_1.grid(row=4, column=0, sticky=W,padx=132) #LOGRADOURO
in7_fr3_1 = Entry(fr3_1, font= ('Arial 16'), textvariable=var5,width=22,bg='#f5f5f5')
in7_fr3_1.grid(row=5, column=0, sticky=W,padx=132) #CIDADE
in8_fr3_1 = Entry(fr3_1, font= ('Arial 16'),textvariable=var6, bg='#f5f5f5')
in8_fr3_1.bind('<KeyRelease>', dois_digitos_cliente)
in8_fr3_1.grid(row=4, column=0, sticky=W,padx=492) #UF OK
in9_fr3_1 = Entry(fr3_1, font= ('Arial 16'), bg='#f5f5f5')
in9_fr3_1.bind('<KeyRelease>', numeros_cliente)
in9_fr3_1.grid(row=5, column=0, sticky=W,padx=492) #Nº OK
in10_fr3_1 = Entry(fr3_1, font= ('Arial 16'),width=22, bg='#f5f5f5')
in10_fr3_1.grid(row=6, column=0, sticky=W,padx=132) #EMAIL

#botões #Atualizado o texto e os botoes
bt0_fr3 = Button(fr3, text='Login', font = ('Mongolian Baiti', '20', 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[login_cliente()]).grid(row=6, column=0, sticky=W,padx=150,pady=10)
lb16_fr3 = Label(fr3, text='', font=('Mongolian Baiti', '23'), bg='#8a37cc', fg='#f5f5f5')
lb16_fr3.grid(row=5, column=0, sticky=W,padx=200)
bt1_fr3 = Button(fr3, text='Cadastrar', font = ('Mongolian Baiti', "20", 'bold' ) , bg='#eb8334', fg='#f5f5f5',width=13, command= lambda:[in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), fr3.grid_remove(), fr3_1.grid(row=0, column=0)] ).grid(row=6, column=0, sticky=W,padx=400)
bt2_fr3 = Button(fr3, text='Voltar', font = ('Mongolian Baiti', "20", 'bold') , bg='#eb8334', fg='#f5f5f5',width=13 , command= lambda:[in0_fr3.delete(0, 'end'), in1_fr3.delete(0, 'end'), fr3.grid_remove(), fr0.grid(row=0, column=0)]).grid(row=7, column=0, sticky=W,padx=400)
bt9_fr3 = Button(fr3, text="Editar Usuário", font=("Mongolian Baiti", "20", "bold"),width=13, bg="#eb8334", fg='#f5f5f5').grid(row=7, column=0,sticky=W,padx=150,pady=10) 

bt7_fr3 = Button(fr3, text='👁', font=('Mongolian Baiti', "15", "bold"),bg='#eb8334', fg='#fff',command=mostrar_1).grid(row=3, column=0, sticky=W,padx=550,pady=5)
bt3_fr3_1 = Button(fr3_1, text='Salvar', font = ('Mongolian Baiti', '19', 'bold' ), width= 18, bg='#eb8334', fg='#f5f5f5', command= lambda:[confirmar_usuario(), in15_fr3_1.delete(0, 'end'), in2_fr3_1.delete(0, 'end'),in3_fr3_1.delete(0, 'end'),in4_fr3_1.delete(0, 'end'),in5_fr3_1.delete(0, 'end'),in6_fr3_1.delete(0, 'end'),in7_fr3_1.delete(0, 'end'),in8_fr3_1.delete(0, 'end'),in9_fr3_1.delete(0, 'end'),in10_fr3_1.delete(0, 'end'),fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=7, column=0,sticky=W,padx=130,pady=15)
bt4_fr3_1 = Button(fr3_1, text='Voltar', font = ('Mongolian Baiti', '19', 'bold' ), width=18, bg='#eb8334', fg='#f5f5f5', command= lambda:[in15_fr3_1.delete(0, 'end'), in2_fr3_1.delete(0, 'end'),in3_fr3_1.delete(0, 'end'),in4_fr3_1.delete(0, 'end'),in5_fr3_1.delete(0, 'end'),in6_fr3_1.delete(0, 'end'),in7_fr3_1.delete(0, 'end'),in8_fr3_1.delete(0, 'end'),in9_fr3_1.delete(0, 'end'),in10_fr3_1.delete(0, 'end'),fr3_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=7, column=0, sticky=W,padx=460)

#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#8a37cc', text='Usuário', font='Arial 25',fg='#f5f5f5', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Usuário', font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5')
lb0_fr4.grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5')
lb0_1_fr4.grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#8a37cc',fg='#f5f5f5')
lb1_fr4.grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [lb7_fr4.grid_remove(), fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W,pady=5)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [lb7_fr4.grid_remove(), fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W,pady=5)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [lb7_fr4.grid_remove(), fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W,pady=5)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=12, command= lambda: [lb7_fr4.grid_remove(), fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=5, column=0, sticky=W,pady=5)
bt6_fr4 = Button(fr4, text='Sair', font='Arial 20',padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=14, command= lambda:[lb7_fr4.grid_remove(), fr4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=7, column=2, sticky=E) #Atualizado o texto
lb7_fr4 = Label(fr4, text='',font='Arial 20',padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5')
lb7_fr4.grid(row=1 ,column=2, rowspan=4)

#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, pady=5, bg= '#8a37cc', text='Depósito',fg='#f5f5f5', font=('Mongolian Baiti', "19" ), borderwidth=1, relief="sunken",width=150)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado:',bg='#8a37cc',fg='#f5f5f5', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0).grid(row=0, column=0 , sticky=W,padx=25)
in0_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#f5f5f5')
in0_fr4_1.bind("<KeyRelease>", deposito)
in0_fr4_1.grid(row=0, column=0,sticky=W,padx=280)
lb1_fr4_1 = Label(fr4_1, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_1 = Entry(fr4_1, font='Arial 20', textvariable=hello_3,bg='#f5f5f5',show="*") #Atualizado o entrar e o botão 
in1_fr4_1.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font=('Mongolian Baiti', '19', 'bold'),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=19, command= lambda: deposito_calculo())
bt2_fr4_1.grid(row=2, column=0, sticky=W,padx=282,pady=5)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', fg='#f5f5f5',font=('Mongolian Baiti', "17" ),padx=5, pady=0, bg= '#8a37cc',width=38)
lb3_fr4_1.grid(row=3, column=0, columnspan=3, sticky=W,padx=175)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(),in0_fr4_1.delete(0, 'end'), in1_fr4_1.delete(0, 'end'), fr4_1.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=450) #Atualizado o texto e troca de pocisão
bt4_1_fr4_1 = Button(fr4_1, text='Sair', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda:[mensagem(),in1_fr4_1.delete(0, 'end'), fr4_1.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=190,pady=5) #Atualizado o texto e troca de pocisão
bt5_fr4_1 = Button(fr4_1, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_3).grid(row=1, column=0, sticky=W,padx=588,pady=5) #Atualizado o entrar e o botão

#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Saque', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado:', font=('Mongolian Baiti', "17", "bold" ),padx=5, pady=0, bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=0 , sticky=W,padx=67)
in0_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#f5f5f5')
in0_fr4_2.bind('<KeyRelease>', saque)
in0_fr4_2.grid(row=0, column=0,sticky=W,padx=280)
lb1_fr4_2 = Label(fr4_2, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_2 = Entry(fr4_2, font='Arial 20',textvariable=hello_4, bg='#f5f5f5',show="*") #Atualizado o entrar e o botão
in1_fr4_2.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=19, command= lambda: saque_calculo()).grid(row=2, column=0, sticky=W,padx=282,pady=5)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font=('Mongolian Baiti', "17" ),padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5',width=31)
lb3_fr4_2.grid(row=3, column=0, columnspan=3, sticky=W,padx=220)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(),in0_fr4_2.delete(0, 'end'), in1_fr4_2.delete(0, 'end'), fr4_2.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=450) #Atualizado o texto e troca de pocisão
bt4_1_fr4_2 = Button(fr4_2, text='Sair', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg='#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(),in0_fr4_2.delete(0, 'end'), in1_fr4_2.delete(0, 'end'), fr4_2.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=190,pady=5) #Atualizado o texto e troca de pocisão
bt5_fr4_2 = Button(fr4_2, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_4).grid(row=1, column=0, sticky=W,padx=588,pady=5) #Atualizado o entrar e o botão

#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Transferência', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido:',padx=5, pady=0, font=('Mongolian Baiti', "17", "bold" ),bg='#8a37cc',fg='#f5f5f5').grid(row=0, column=0 , sticky=W,padx=21)
in0_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#f5f5f5')
in0_fr4_3.bind('<KeyRelease>', transferencia)
in0_fr4_3.grid(row=0, column=0, sticky=W,padx=280)
lb1_1_fr4_3 = Label(fr4_3, text='Conta Destino:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=117)
in1_1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#f5f5f5')
in1_1_fr4_3.grid(row=1, column=0, sticky=W,padx=280)
lb1_fr4_3 = Label(fr4_3, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=2, column=0, sticky=W,padx=203)
in1_fr4_3 = Entry(fr4_3, font='Arial 20',textvariable=hello_5, bg='#f5f5f5',show="*") #Atualizado o entrar e o botão
in1_fr4_3.grid(row=2, column=0, sticky=W,padx=280)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=19, command= lambda: transfere_calculo()).grid(row=3, column=0, sticky=W, padx=282,pady=5)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font=('Mongolian Baiti', "17" ),padx=5, pady=0,  bg= '#8a37cc',fg='#f5f5f5',width=31)
lb3_fr4_3.grid(row=4, column=0, columnspan=3, sticky=W,padx=220)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0,  bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(),in1_1_fr4_3.delete(0,'end'), in0_fr4_3.delete(0, 'end'), in1_fr4_3.delete(0, 'end'), fr4_3.grid_remove(), fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=5, column=0, sticky=W,padx=450) #Atualizado o texto e troca de pocisão
bt4_1_fr4_3 = Button(fr4_3, text='Sair', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda:[mensagem(),in1_1_fr4_3.delete(0,'end'), in0_fr4_3.delete(0, 'end'), in1_fr4_3.delete(0, 'end'), fr4_3.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=5, column=0, sticky=W,padx=190,pady=5) #Atualizado o texto e troca de pocisão
bt5_fr4_3 = Button(fr4_3, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_5).grid(row=2, column=0, sticky=W,padx=588,pady=5) #Atualizado o entrar e o botão

#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, pady=5, bg= '#8a37cc',fg='#f5f5f5', text='Extrato', font=('Mongolian Baiti', "22" ), borderwidth=1, relief="sunken", width=150)
lb0_fr4_4 = Label(fr4_4, text='Periodo:', font=('Mongolian Baiti', "17", "bold" ),bg='#8a37cc',fg='#f5f5f5',padx=5, pady=0).grid(row=0, column=0 , sticky=W,padx=185)
in0_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#f5f5f5')
in0_fr4_4.bind('<KeyRelease>', extrato)
in0_fr4_4.grid(row=0, column=0, sticky=W,padx=280)
in0_fr4_4.insert(0, 'MM/AAAA')
lb1_fr4_4 = Label(fr4_4, text='Senha:', font=('Mongolian Baiti', "17", "bold" ) ,padx=5, pady=0, bg= '#8a37cc',fg='#f5f5f5').grid(row=1, column=0, sticky=W,padx=203)
in1_fr4_4 = Entry(fr4_4, font='Arial 20',textvariable=hello_6, bg='#f5f5f5',show="*") #Atualizado o entrar e o botão
in1_fr4_4.grid(row=1, column=0,sticky=W,padx=280)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=19,command= lambda: [lb7_fr4.grid(row=1 ,column=2, rowspan=4),extrato_calculo()]).grid(row=2, column=0, sticky=W, padx=282,pady=5)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação',  font=('Mongolian Baiti', "17" ),padx=5, pady=0,  bg= '#8a37cc',fg='#f5f5f5',width=31)
lb3_fr4_4.grid(row=3, column=0, columnspan=3, sticky=W,padx=220) 
bt4_fr4_4 = Button(fr4_4, text='Voltar', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0,  bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(), in0_fr4_4.delete(0, 'end'), in1_fr4_4.delete(0, 'end'), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=W,padx=450) #Atualizado o texto e troca de pocisão
bt4_1_fr4_4 = Button(fr4_4, text='Sair', font=('Mongolian Baiti', '19', 'bold' ),padx=5, pady=0, bg= '#eb8334',fg='#f5f5f5',width=15, command= lambda: [mensagem(), in0_fr4_4.delete(0, 'end'), in1_fr4_4.delete(0, 'end'), fr4_4.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=4, column=0, sticky=W,padx=190,pady=5) #Atualizado o texto e troca de pocisão
bt5_fr4_4 = Button(fr4_4, text='👁', font=('Mongolian Baiti', "14", "bold"),bg='#eb8334', fg='#fff', command=mostrar_6).grid(row=1, column=0, sticky=W,padx=588,pady=5) #Atualizado o entrar e o botão

#Looping para tudo
root.mainloop()