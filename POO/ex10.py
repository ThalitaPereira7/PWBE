class Livro:
    def __init__(self, titulo, autor, num_paginas):
       
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.disponivel = True

    def emprestar(self):
      
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
      
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está disponível na biblioteca.")

    def verificar_disponibilidade(self):
       
        if self.disponivel:
            print(f"O livro '{self.titulo}' está disponível para empréstimo.")
        else:
            print(f"O livro '{self.titulo}' não está disponível no momento.")


livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)


livro.verificar_disponibilidade()
livro.emprestar()
livro.emprestar()
livro.devolver()
livro.verificar_disponibilidade()

        