class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = 0 

    def acelerar(self, incremento):
        
        self.velocidade_atual += incremento
        print(f'O carro acelerou para {self.velocidade_atual} km/h.')

    def frear(self, decremento):
        
        if self.velocidade_atual - decremento >= 0:
            self.velocidade_atual -= decremento
            print(f'O carro reduziu a velocidade para {self.velocidade_atual} km/h.')
        else:
            self.velocidade_atual = 0
            print('O carro parou! A velocidade não pode ser negativa.')

    def exibir_velocidade(self):
      
        print(f'A velocidade atual do carro é {self.velocidade_atual} km/h.')


carro1 = Carro("Fusca", "1978")
carro1.exibir_velocidade()
carro1.acelerar(50)
carro1.frear(20)
carro1.acelerar(30)
carro1.frear(100)
carro1.exibir_velocidade()
