

class Menu:
    def __init__(self):
        agenda = Agenda()

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
                cod = len(agenda.listaContatos) + 1
                nome = input('Entre com o Nome: ')
                telefone = input('Entre com o Telefone: ')
                email = input('Entre com o E-mail: ')

                agenda.salva_contato(cod, nome, telefone, email)

            elif entrada_menu == '2':
                agenda.lista_contatos()

            elif entrada_menu == '3':
                cod = int(input('Informe o código do contato: '))
                nome_novo = input('Entre com o novo Nome: ')
                agenda.altera_nome(cod, nome_novo)

            elif entrada_menu == '4':
                cod = int(input('Informe o código do contato: '))
                telefone_novo = input('Entre com o novo Telefone: ')
                agenda.altera_telefone(cod, telefone_novo)

            elif entrada_menu == '5':
                cod = int(input('Informe o código do contato: '))
                email_novo = input('Entre com o novo E-mail: ')
                agenda.altera_email(cod, email_novo)

            elif entrada_menu == '6':
                cod = int(input('Informe o código do contato: '))
                agenda.exclui_contato(cod)

            elif entrada_menu == '0':
                break

            else:
                print('Entrada incorreta!')