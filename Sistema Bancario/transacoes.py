from abc import ABC, abstractmethod

class Transacao(ABC): #classe abstrata; contém atributos e métodos comuns com outras classes derivadas
    
    @property #classe abstrata; garante com que cada transação tenha um valor associado 
    @abstractmethod #propriedade abstrata; subclasses obrigadas a usá-la
    def valor(self):
        pass
    
    @abstractmethod #não possui implementação na classe base, apenas nas derivadas (obrigadas); método abstrato
    def registrar(self, conta):
        from contas import Conta #vai ser chamada através de polimorfismo
        pass

class Deposito(Transacao): #adicionar método para verificar transação
    #atributos (self, valor)
    #ganha o método registrar da classe transacao
    def __init__(self, valor):
        self.__valor = valor
        
    @property #implementa o valor como uma propriedade
    def valor(self):
        return self.__valor
        
    def registrar(self, conta):
        from contas import Conta 
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            print(f"Depositando R$ {self.valor:.2f} na conta.")
            conta.historico.adicionar_transacao(self) #para registrar a transação no histórico
    
class Saque(Transacao): #adicionar método para verificar transação
    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        from contas import Conta
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            print(f"Sacando R$ {self.valor:.2f} na conta.")
            conta.historico.adicionar_transacao(self)
