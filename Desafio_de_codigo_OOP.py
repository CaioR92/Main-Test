from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao): #polimorfismo
        
        
    def adicionar_conta(self, conta): # liente pode ter várias contas
        self.contas.append(conta)

class PessoaFísica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, cliente, numero): #para acessar os atributos privadas usa-se _NomedaClasse__nomeatributo
        self.__saldo = 0 #atributos privados precisam de getters (@property) para serem acessados
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()
    
    @property #transforma um método em um getter; retorna o atributo, um valor ou um objeto
    def exibir_saldo(self): #não recebe argumento e retorna float
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico
    
    @classmethod #não recebe a instância (self), mas sim a classe como argumento. Acessar ou modifica atributos ou métodos da classe
    def criar_conta(cls, cliente, numero): #pega a classeConta + numero e nome e retorna objConta
        return cls(cliente, numero)
        
    @property #define métodos que funcionam como atributos de classe, ou seja, self.sacar chama o método sacar como um atributo
    def sacar(self, valor: float) -> bool:
        excede_saldo = valor > saldo
        saldo = self.__saldo
        
        if excede_saldo:
            print("Impossível sacar este valor. Saldo indisponível.")
            return False
        elif valor > 0:
            self.__saldo -= valor
            print(f"Saque no valor de R$ {self.valor} efetuado com sucesso.")
            return True
        else:
            print("Impossível realizar saque. Valor incorreto.")
        return False
    
    @property
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            print(f"Deposíto no valor de R$ {self.valor} efetuado com sucesso.")
        else:
            print("Impossível realizar depósito. Valor incorreto.")
            return False
        return True
        
class ContaCorrente(Conta): #herança 
    def __init__(self, numero, saldo, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente, saldo)
        self.limite = limite
        self.limite_saques = limite_saques

class Transacao(ABC): #abstrata; contém atributos e métodos comuns com outras classes derivadas
    
    @abstractmethod #não possui implementação na classe base, apenas nas derivadas (obrigadas)
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        
    def registrar(self, conta: Conta): 
        conta.depositar(self.valor)    
    # atributos (self, valor)
    # ganha o método registrar da classe transacao
    
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        
    def registrar(self, conta: Conta):
        conta.sacar(self.valor)
    
    #implementa o método registrar
    # atributos (self. valor)
    # ganha o método registrar da classe transacao

class Historico: #init + adicionar transaçoes em self.transacoes + atributo transacoes retorna transacoes
    def __init__(self):
        self.__transacoes = []  #Lista vazia; armazena instância criadas da classe
        
    def transacoes(trasacao: Transacao):
        return self.transacoes
        
    def adicionar_transacao(self): #dict
        