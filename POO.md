self = características
defs = ações
__init__ = necessário para criação
_ = encapsulamento; apenas o método pode acessar
@property = 
@classmethod =
@staticmethod

class Usuario:
# variáveis de classe = para todos os objetos
    def __init__(self, nome, cpf, data_nascimento, endereco): # variáveis de instância = particular de cada objeto
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
    
    def criar_conta(self):
        
    def saque(self, conta: Conta):
        
    def extrato(self, conta: Conta):
        
    def deposito(self, conta: Conta):
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Conta:


#objeto #classe        
u1 = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
u1.criar_conta() #objeto + método



contexto objeto =/= contexto classe


----- Estrutura de dados ------

Pilha vs. Fila
FIla = FIFO (First in, first out) [A, B, C] + D = [A, B, C, D]
Pilha = LIFO (ast in, first out) [A, B, C] + D = [D, A, B, C]

Métodos de classe estão ligados à classe, não ao objeto. Possuem acesso ao ESTADO DA CLASSE. Criar métodos de fábrica. Retorna uma nova instância.

Métodos estáticos: Método vinculado à classe, e não ao objeto da classe. Não pode acessar o modificar o estado da classe. Criar funções utilitárias. 

Classes abstratas: ao colocar @abstractmethod em algum método você é obrigado a implementar os métodos na outra classe que a estiver chamando.

# meu_script.py

def funcao():
    print("Essa função foi chamada.")

if __name__ == "__main__":
    print("Este script está sendo executado diretamente.")
    funcao()
else: #chamando em outro arquivo como import meu_script
    print("Este script foi importado como um módulo.")
