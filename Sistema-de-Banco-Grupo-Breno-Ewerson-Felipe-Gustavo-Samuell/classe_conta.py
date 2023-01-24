from classe_historico import Historico
class Conta:

    def __init__(self, objeto, num: str, saldo=0.0):
        self.titular = objeto.nome
        self.num = num
        self.saldo = saldo
        self.historico = Historico()

    def extrato(self):
        print(f'='*30,f'\nTitular: {self.titular}\nNum. Conta: {self.num}\nSaldo: {self.saldo}')
        self.historico.transacoes_bancarias()

    def deposito(self, valor, data):
        self.saldo += valor
        self.historico.transacoes.append(f'depósito: R$ {valor} - {data}')
        return self.saldo
    def saque(self, valor, data):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de R$ {valor} - {data}')
            return self.saldo
        else:
            print('Saldo Insuficiente!')

    def transfere(self, valor, destino, data):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f'transferencia de R$ {valor} para a conta {destino.num} - {data}')
            return self.saldo
        else:
            print('Saldo Insuficiente!')

    def transfere_para(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.recebe_transferencia(valor,self)
            self.historico.transacoes.append(f'transferencia de {valor} para a conta {destino.num}')
            return self.saldo
        else:
            print('Saldo insuficiente para a transferencia!')

    def recebe_transferencia(self, valor, origem, data):
        #self.saldo += valor
        self.historico.transacoes.append(f'transferencia de R$ {valor} da conta {origem.num} - {data}')
