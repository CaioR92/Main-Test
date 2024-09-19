from abc import ABC, abstractmethod
from datetime import datetime

mascara_ptbr = "%d/%m/%Y %H:%M"
data_hora_atual = datetime.now().strftime(mascara_ptbr)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao): #polimorfismo permite que se use um método ou interface comum em várias classes de maneiras distintas
        transacao.registrar(conta) #Passa qualquer tipo de transação genérica
        #(ou seja, qualquer tipo de transação que implemente a interface Transacao)
        #e o comportamento será diferente dependendo de qual subclasse de Transacao
        #está sendo utilizada (pode ser Deposito ou Saque).
        
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
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso.") #Não pode ser self.valor pois o valor é um argumento, ñ um atributo
            return True
        else:
            print("Impossível realizar saque. Valor incorreto.")
        return False
    
    @property
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            print(f"Deposíto no valor de R$ {valor:.2f} efetuado com sucesso.")
        else:
            print("Impossível realizar depósito. Valor incorreto.")
            return False
        return True
        
class ContaCorrente(Conta): #herança; com haverá diferentes tipos de conta, os controles devem ser feito nas classes descendentes
    def __init__(self, cliente, numero, saldo, limite=500, limite_saques=3): #limites devem ser inicializados no construtor
        super().__init__(cliente, numero, saldo)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saque = 0
        self.data_hora_atual = None
    
#É necessário chamar os métodos da classe base para realizar outros tipos de verificações
#Adicionar contador de saques que é verificado a cada operação
    def sacar(self, valor):
        if self.numero_saque >= self.limite_saques:
            print("\nLimite de saques diários atingido.")
        else:
            if super().sacar(valor): #super(). para chamar o método da classe ascendente
                self.numero_saque += 1
                self.data_hora_atual = datetime.now().strftime(mascara_ptbr)
                print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso.")

class Transacao(ABC): #abstrata; contém atributos e métodos comuns com outras classes derivadas
    
    @abstractmethod #não possui implementação na classe base, apenas nas derivadas (obrigadas)
    def registrar(self, conta: Conta): #vai ser chamada através de polimorfismo
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        
    def registrar(self, conta: Conta): 
        conta.depositar(self.valor)
        print(f"Depositando R$ {self.valor:.2f} na conta.")
    # atributos (self, valor)
    # ganha o método registrar da classe transacao
    
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        
    def registrar(self, conta: Conta):
        conta.sacar(self.valor)
        print(f"Sacando R$ {self.valor:.2f} na conta.")
    #implementa o método registrar
    # atributos (self. valor)
    # ganha o método registrar da classe transacao

class Historico: #init + adicionar transaçoes em self.transacoes + atributo transacoes retorna transacoes
    def __init__(self):
        self.__transacoes = []  #Lista vazia; armazena instância criadas da classe
        
    def transacoes(self, trasacao: Transacao):
        return self.transacoes
        
    def adicionar_transacao(self): #dict
        print(f"""{'Tipo de Transação': transacao,
                    'Valor da Transação': valor,
                    'Data da Transação': data_hora}""")

