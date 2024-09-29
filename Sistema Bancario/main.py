from clientes import PessoaFísica
from contas import ContaCorrente
from transacoes import Saque, Deposito
from historico import Historico

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
            print("\nOpção inválida. Por favor, escolha entre as seguintes opções: [1] Cadastrar Cliente, [2] Criar Conta Corrente, [3] Depositar, [4] Sacar, [5] Ver extrato, [6] Exibir Contas, [7] Sair\n")

main()