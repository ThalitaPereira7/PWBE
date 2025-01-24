class Retangulo():

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        self.conta = self.largura * self.altura

        print(f"A area do retangulo é : {self.conta}")

    def perimetro(self):
        self.conta2 = (self.altura * 2) + (self.largura * 2)

        print(f"O perimetro do retangulo é : {self.conta2}")



retangulo1 = Retangulo(10, 15)
retangulo1.area()
retangulo1.perimetro()
