class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)
        
    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} - {biblioteca.ativo}")
            
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

