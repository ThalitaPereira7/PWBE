class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        formula = 3.14 * self.raio ** 2
        print(formula)
    
circulo1 = Circulo(5)
circulo1.area()