from class_db_agenda import DBAgenda

class Menu:
    def __init__(self):
        agenda = DBAgenda()

        while True:
            entrada_menu = input('Digite!\n'
                                 '1 - Salvar novo contato\n'
                                 '2 - Listar contatos\n'
                                 '3 - Alterar Nome\n'
                                 '4 - Alterar Telefone\n'
                                 '5 - Alterar E-mail\n'
                                 '6 - Excluir\n'
                                 '0 - Sair\n')

            if entrada_menu == '1':
                cod = None  
                nome = input('Entre com o Nome: ')
                telefone = input('Entre com o Telefone: ')
                email = input('Entre com o E-mail: ')

                agenda.salva_contato(cod, nome, telefone, email)

            elif entrada_menu == '2':
                agenda.lista_contatos()

            elif entrada_menu == '3':
                cod = int(input('Informe o código do contato: '))
                valor = input('Entre com o novo Nome: ')
                atributo = 'nome'
                agenda.alterar_contato(atributo, valor, cod)

            elif entrada_menu == '4':
                cod = int(input('Informe o código do contato: '))
                valor = input('Entre com o novo Telefone: ')
                atributo = 'telefone'
                agenda.alterar_contato(atributo,valor, cod)

            elif entrada_menu == '5':
                cod = int(input('Informe o código do contato: '))
                valor= input('Entre com o novo E-mail: ')
                atributo = 'email'
                agenda.alterar_contato(atributo,valor,cod)

            elif entrada_menu == '6':
                cod = int(input('Informe o código do contato: '))
                agenda.excluir_contato(cod)

            elif entrada_menu == '0':
                break

            else:
                print('Entrada incorreta!')