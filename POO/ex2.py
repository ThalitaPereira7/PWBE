class ContaBancaria():
    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo


    def deposito(self):
        self.deposito = float(input("Digite o valor do deposito:"))

        self.conta = self.saldo + self.deposito

        print(f"Seu saldo depois do deposito: {self.conta}")

    def saque (self):
        self.saque = float(input("Digite o valor que você gostaria de sacar da sua conta: "))

        self.conta2 = self.saldo - self.saque

        print(f"Seu saldo após o saque: {self.conta2}")



pessoa = ContaBancaria(777, "Thalita", 500)
pessoa.deposito()
pessoa.saque()
