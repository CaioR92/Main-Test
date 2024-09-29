from historico import Historico
import utils

class Conta:
    def __init__(self, cliente, numero): #para acessar os atributos privadas usa-se _NomedaClasse__nomeatributo
        self.__saldo = 0 #atributos privados precisam de getters (@property) para serem acessados
        self.__numero = numero #gerador de número aleatório
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()
    
    @property #transforma um método em um getter; retorna o atributo, um valor ou um objeto
    def saldo(self): #não recebe argumento e retorna float
        return self.__saldo
    
    @property #define métodos que funcionam como atributos de classe
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
    def nova_conta(cls, cliente, numero): #pega a classeConta + numero e nome e retorna objConta
        return cls(cliente, numero)
        
    def sacar(self, __saldo, valor: float) -> bool:
        excede_saldo = valor > __saldo
        __saldo = self.__saldo
        
        if excede_saldo:
            print("Impossível sacar este valor. Saldo indisponível.")
            return False
        elif valor > 0:
            self.__saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso.") #Não pode ser self.valor pois o valor é um argumento, ñ um atributo
            return True
        else:
            print("Impossível realizar saque. Valor inválido.")
        return False
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            self.data_hora_atual = utils.gerar_data_atual()
            print(f"Deposíto no valor de R$ {valor:.2f} efetuado com sucesso.")
        else:
            print("Impossível realizar depósito. Valor inválido.")
            return False
        return True
        
class ContaCorrente(Conta): #herança; com haverá diferentes tipos de conta, os controles devem ser feito nas classes descendentes
    def __init__(self, cliente, numero, limite=500, limite_saques=3): #limites devem ser inicializados no construtor
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saque = 0
        self.data_hora_atual = None
        
#É necessário chamar os métodos da classe base para realizar outros tipos de verificações
#Adicionar contador de saques que é verificado a cada operação
#Faltou verificar limite
    def sacar(self, valor):
        from transacoes import Saque
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["Tipo de Transação"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("\nO valor do saque excede o limite de sua Conta. Tente novamente.")
        elif excedeu_saques:
            print("\nLimite de saques diários atingido.")
        else:
            super().sacar(valor) #super(). para chamar o método da classe ascendente
            self.numero_saque += 1
            self.data_hora_atual = utils.gerar_data_atual()
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso.")
        return False
            
    def __str__(self): #fornece uma representação em string de um objeto
        return f"""Titular: {self.cliente.nome},
                C/C: {self.numero},
                Agência: {self.agencia}"""