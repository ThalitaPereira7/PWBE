class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def quant_estoque (self):
        
        calculo = self.preco * self.estoque
        
        print(f"De acordo com o estoque o valor do total é : {calculo}")
        
        if self.estoque <= 0:
            print("Produto Indisponivel")
        else:
            print("Produto Disponivel")

produto1 = Produto("Lapis", 10, 5)
produto1.quant_estoque()
            
        
        