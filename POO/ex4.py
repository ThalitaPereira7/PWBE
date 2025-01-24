class Aluno():
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = [] 
    
    def adicionar_notas(self):
        
        quantidade = int(input("Quantas notas você deseja adicionar: "))
        
       
        for i in range(quantidade):
            nota = float(input(f"Digite a nota {i+1}: "))
            self.notas.append(nota)
    
    def media(self):
       
        media = sum(self.notas) / len(self.notas)
        print(f"A média das notas é: {media:.2f}")
        
        if media < 5:
            print("Reprovado")
        else:
            print("Aprovado")
    


aluno = Aluno("Thalita", 777)
aluno.adicionar_notas()
aluno.media()

