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