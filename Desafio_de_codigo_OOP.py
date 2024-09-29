#Depois adicionar sistema de notificação de transações, tranferências, tipos de contas, geração de relatórios por data, tipo de transação
# e possibilidade de exportar por pdf ou csv

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
        
    def adicionar_conta(self, conta): #cliente pode ter várias contas
        self.contas.append(conta)

class PessoaFísica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco) #super()__init__ chama o construtor da classe pai
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
            print("Impossível realizar saque. Valor inválido.")
        return False
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
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
        if valor > self.limite:
            print("\nO valor do saque excede o limite de sua Conta. Tente novamente.")
        elif self.numero_saque >= self.limite_saques:
            print("\nLimite de saques diários atingido.")
        else:
            super().sacar(valor) #super(). para chamar o método da classe ascendente
            self.numero_saque += 1
            self.data_hora_atual = datetime.now().strftime(mascara_ptbr)
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso.")
        return False
       
    def depositar(self, valor):
        if super().depositar(valor): #precisa de if
            self.data_hora_atual = datetime.now().strftime(mascara_ptbr)
            print(f"Deposito no valor de R$ {valor:.2f} efetuado com sucesso.")
            
    def __str__(self): #fornece uma representação em string de um objeto
        return f"""Titular: {self.cliente.nome},
                C/C: {self.numero},
                Agência: {self.agencia}"""
    
class Transacao(ABC): #classe abstrata; contém atributos e métodos comuns com outras classes derivadas
    
    @property #classe abstrata; garante com que cada transação tenha um valor associado 
    @abstractmethod #propriedade abstrata; subclasses obrigadas a usá-la
    def valor(self):
        pass
    
    @abstractmethod #não possui implementação na classe base, apenas nas derivadas (obrigadas); método abstrato
    def registrar(self, conta: Conta): #vai ser chamada através de polimorfismo
        pass

class Deposito(Transacao): #adicionar método para verificar transação
    #atributos (self, valor)
    #ganha o método registrar da classe transacao
    def __init__(self, valor):
        self.__valor = valor
        
    @property #implementa o valor como uma propriedade
    def valor(self):
        return self.__valor
        
    def registrar(self, conta: Conta): 
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
    
    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            print(f"Sacando R$ {self.valor:.2f} na conta.")
            conta.historico.adicionar_transacao(self)

class Historico: #init + adicionar transaçoes em self.transacoes + atributo transacoes retorna transacoes
    def __init__(self):
        self.__transacoes = []  #Lista vazia; armazena instância criadas da classe
    
    @property #getter    
    def transacoes(self):
        return self.__transacoes
        
    def adicionar_transacao(self, transacao): #precisa de um append para __transacoes; dict
        self.__transacoes.append({'Tipo de Transação': transacao.__class__.__name__, #retorna a o nome da classe a qual o objeto transacao pertence com string
                    'Valor da Transação': transacao.valor,
                    'Data da Transação': datetime.now().strftime(mascara_ptbr)})

def criar_cliente(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("Já existe usuários cadastrado com este CPF.")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/UF): ")
    
    cliente = PessoaFísica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
    
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente_cpf = None
    
    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_cpf = cliente
            break    
    if not cliente_cpf:
        print("Cliente não cadastrado. Não é possível criar uma conta.")
        return None
    
    conta = ContaCorrente.nova_conta(cliente=cliente_cpf, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n Conta criada com sucesso!")
    
    return cliente_cpf
    
def listar_contas(contas):
    for conta in contas:
        print("= * 100")
        print(str(conta))
    
def recuperar_conta_cliente(cliente): # verificar qual conta do cliente
    if not cliente.contas:
        print("Cliente não possui conta.")
        return
    return cliente.contas[0]

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não cadastrado.")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print(">>>>>>>>>> EXTRATO <<<<<<<<<<")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações nesta Conta."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\nR$[{transacao['valor']:.2f}]\nDia e Hora: {transacao['data']}."
    print(extrato)
    print(f"\nSaldo: R${conta.saldo:.2f}")
    print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
    
def depositar(clientes):
    cpf = (input("Digite seu CPF: "))
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não cadastrado.")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = (input("Digite seu CPF: "))
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não cadastrado.")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)
    
def menu():
    menu = f"""
            Olá, Bem-vindo à sua conta. Por gentileza, escolha uma opção:


            [1] Cadastrar Cliente
            [2] Criar Conta Corrente
            [3] Depositar
            [4] Sacar
            [5] Ver extrato
            [6] Exibir Contas
            [7] Sair

            """
    return int(input(menu))
            
def main():          
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1:
            criar_cliente(clientes)
        elif opcao == 2:
            numero_conta = len(contas) + 1
            titular_conta = criar_conta(numero_conta, clientes, contas) # Cria uma instância?
            print(f"Conta {numero_conta} criada com sucesso para {titular_conta.nome}.")
        elif opcao == 3:
           depositar(clientes)
        elif opcao == 4:
            sacar(clientes)
        elif opcao == 5:
            exibir_extrato(clientes)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 7:
            print("\nObrigado por utilizar os nossos serviços. Volte sempre!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha entre as seguintes opções: [1] Depositar, [2] Sacar, [3] Ver extrato, [4] Sair\n")

main()