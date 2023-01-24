class Cliente:

    def __init__(self, nome: str, cpf: str, dataNasc: str, tel: str, uf: str, logradouro: str, numero: str, bairro: str, cidade: str, email: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc
        self.tel = tel
        self.uf = uf
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.email = email
        self.senha = senha

    def imprime_dados(self):
        print(f'Nome: {self.nome}\ncpf: {self.cpf}\n'
              f'Data de Nasc: {self.dataNasc}')