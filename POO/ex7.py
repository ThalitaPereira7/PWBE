class Triangulo():
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        
    
    def validar(self):
        if (self.lado1 + self.lado2) < self.base:
            print("Invalido")
        else:
            print("Valido")

    def area(self):
        self.conta = self.base * (self.altura/2)

        print(f"A area do triangulo é : {self.conta}")




retangulo1 = Triangulo(10, 15, 12, 13)
retangulo1.validar()
retangulo1.area()