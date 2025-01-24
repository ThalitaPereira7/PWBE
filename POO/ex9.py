class Paciente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []

    def nova_consulta(self):
        resposta = input("Você deseja fazer uma consulta? S/N: ")
        
        while resposta == 'S':
            qual_consulta = input("Digite a consulta que deseja realizar, se desejar sair digite 'N': ")
            if qual_consulta == 'N':
                print("Saindo do registro de consultas.")
                break
            self.historico.append(qual_consulta)
            print("Consulta adicionada com sucesso!")

    def exibir_consultas(self):
        if not self.historico:
            print(f"O paciente {self.nome} não possui consultas registradas.")
        else:
            print(f"Histórico de consultas de {self.nome}:")
            for consulta in self.historico:
                print(f"- {consulta}")


paciente = Paciente("Jose", 50)
paciente.nova_consulta()
paciente.exibir_consultas()
