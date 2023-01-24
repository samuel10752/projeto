#!/usr/bin/env python
# -*- coding: latin-1 -*-
# Desenvolvimento Aberto
# Senha.py
 
# importa modulos
 
from tkinter import *
import  Tk
 
# Cria formulario
formulario = Tk()
formulario.title = "Desenvolvimento Aberto"
formulario.geometry("300x150")
 
# Cria janela para menssagem
janela = Tk()
janela.wm_withdraw()
 
# Cria evento do botão
def clique():
    if (verificaSenha(senha.get())):
        tkMessageBox.showinfo(title="Menssagem",message="Senha correta",parent=janela)
    else:
        tkMessageBox.showinfo(title="Menssagem",message="Senha incorreta",parent=janela)
 
# Verifica Senha
def verificaSenha(psenha):
    correto = True
    #Senha ficticia deve vir de alguma fonte
    rsenha = "daaberto"
    if (len(psenha) != len(rsenha)):
        correto = False
    else:
        if (psenha != rsenha):
            correto = False
    return correto
 
# Cria Componentes
rotulo = Label(formulario, text="Digite uma senha de 8 caracteres:")
 
senha = Entry(formulario, show="*")
 
botao = Button(formulario, text="Ok", command=clique)
 
# Posiciona componentes no formulario
rotulo.grid(row=0,sticky=W, padx = 20, pady=20)
senha.grid(row=1,sticky=W, padx =20)
botao.grid(row=2,sticky=W, padx=20, pady=10)
 
# loop do tcl
mainloop()