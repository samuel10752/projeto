from tkinter import *

root  = Tk()

# Tudo acima daqui é padrão tkinter

hello = StringVar() # Essa linha basicamente vai ler a senha do usuario e transformar ela em uma string

#Aqui eu vou trocar a ordem em q deveria ser mostrada para facilitar a apresentação, portanto comece a ler o codigo pulando as funções



def mostrar(*args):
    senha = Entry(root,textvariable = hello).grid(row=1, column=0)
    # Como tudo indica que n há uma maneira de esconder ou n a senha, essa função substitui a entrada de dados do usuario por uma netrada identida porem sem o show = "*"
    feecho = Button(root, text="Esconder",width=10, command=esconde).grid(row=2, column= 0)
    #  E wuanod isso acontece tambem substituimos o botão de mostrar por um de esconder  q chama a função a baixo

def esconde(*args):
    senha = Entry(root,textvariable = hello, show="*").grid(row=1, column=0)
    #  Assim como em cima novamente puxamos um novo entry em cima porem dessa vez com o show="*" igual ao primeiro
    mostra = Button(root, text="Mostrar",width=10, command=mostrar).grid(row=2, column= 0)
    #  E novamente o botão muda chamando a função de cima, o q coloca os dois em um loop

def salva():
    print(hello.get())
    # E para fechar o loop existe a função de salvar q basicamente registra os dados, n importa em qual das funções esteja

senha = Entry(root,textvariable = hello, show="*").grid(row=1, column=0) # Esse entry pega a senha do usuario, pórem a mostra com ***** no lugar

mostra = Button(root, text="Mostrar",width=10, command=mostrar).grid(row=2, column= 0)# Esse botão mostra o que o usuario digitou, basicamente vc chama a função imprimi q vai mostrar o que ele digitou

salvar = Button(root, text="salvarr",width=10, command=salva).grid(row=2, column= 1)


# Observações:
# Não é a maneira mais facil, creio q da pra simplificar usando ifs e elses, orem n vejo uma linha de codigo q poderia solucionar esse problema no momento
# A nova caixa de entry e os botões que substituem deverão ter o mesmo tamanho e posição, pois eles ainda continuam visiveis mesmo sobrepostos
# Eu n me garanto com o lambda ent se conseguirem colocar mias de um botão pra rodar nessa função. parabens
# Caso não boa sorte pra vc inclementando tudo
# P.S - ele precisa de delete pra poder trocar o frame tambem
# #Ewersonnãomemate



root.mainloop()