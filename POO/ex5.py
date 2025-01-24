class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def calcular_salario(self):
       
        descontos = 100
        beneficios = 200
        
        calcular = (self.salario - descontos) + beneficios
        
        print(f'O salário final de {self.nome} é: R${calcular:.2f}')
        
        
        

funcionario1 = Funcionario("Jose", "adm", 2000)
funcionario1.calcular_salario()
    