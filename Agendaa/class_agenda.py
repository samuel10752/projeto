


class Agenda:
    def __init__(self):
        self.listaContatos = []

    def salva_contato(self, cod, nome, telefone, email):

        self.listaContatos.append(Contato(cod, nome, telefone, email))
        print('Contato adicionado com sucesso')

    def lista_contatos(self):
        for i in range(len(self.listaContatos)):
            print('cod:', self.listaContatos[i].cod, '- nome:', self.listaContatos[i].nome, '- telefone:', self.listaContatos[i].telefone, '- email:', self.listaContatos[i].email)

    def altera_nome(self, cod, nome_novo):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                self.listaContatos[i].nome = nome_novo
            else:
                print('Codigo de Contato não existe!')

    def altera_telefone(self, cod, telefone_novo):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                self.listaContatos[i].telefone = telefone_novo
            else:
                print('Codigo de Contato não existe!')

    def altera_email(self, cod, email_novo):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                self.listaContatos[i].email = email_novo
            else:
                print('Codigo de Contato não existe!')

    def exclui_contato(self, cod):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                del self.listaContatos[i]
            else:
                print('Codigo de Contato não existe!')