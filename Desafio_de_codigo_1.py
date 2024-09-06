# Desafio de projeto 1: Criando um sistema bancário (sacar, depositar e visualizar extrato)
# Valor inteiro e positivo para deposito
# Histórico dos depósitos no extrato
# 3 saques diários com o limite de 500 reais cada
# Mensagem informando se não houver dinheiro
# Histórico de saques no extrato
# Exibir saldo atual da conta no fim do extrato
# Valores em R$ xxx.xx

# Desafio de projeto 2: Data e hora
# Limite de 10 transações por dia
# Ao tentar uma transação além do limite, deve ser informado que o número de transações daquele dia foi atingido
# Informação de data e hora em todas as transações no extrato

# Desafio de projeto 3: Funções
# Função saque deve receber argumentos apenas por nome (keyword): saldo, valor, extrato, limite, numero_saques. retorno: saldo e extrato
# Função depósito positional: saldo, valor, extrato. retorno: saldo e extrato
# Extrato posicional e kewyqord: p = saldo, k= extrato
# Criar funções: criar_usuario e criar_conta
# criar_usuario: lista; usuário = nome, data de nascimento, cpf e endereço; endereço = logradouro, nro - bairo - cidade/sigla estados. Armazenar apenas os números do cpf
# criar_conta: listas; conta = agência, nro da conta, usuário; numero_conta += 1, NUMEROAGENCIA = 0001; usuário + 1 conta, conta apenas 1 usuário e não existe conta sem usuário
# Para vincular um usuário a uma conta, filtre a lista de user buscando o cpf

# Transformar os argumentos globais em locais

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario()
    
    nome = input("Por gentileza, digite seu nome completo: ")
    data_nascimento = input("Por gentileza, informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Por gentileza, informe seu endereço competo (logradouro, número - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    
def criar_conta(contas):
    

from datetime import datetime

# formatação data e hora
mascara_ptbr = "%d/%m/%Y %H:%M"
data_hora_atual = datetime.now().strftime(mascara_ptbr)

saldo = 0
limite = 500
extrato = ""
# Alterrar limite de transações e inserir data e hora
AGENCIA = "0001"
numero_transacao = 0
LIMITE_TRANSACAO = 10
historico_saque = []
historico_deposito = []
usuarios = []
contas = []

# def deposito():
    global saldo
    global numero_transacao
    global historico_deposito
    
    try:
        valor = float(input("\nQual valor deseja depositar? R$ "))
        if valor <= 0:
            print("\nNão é possível depositar este valor. Tente novamente.\n")
        elif numero_transacao >= LIMITE_TRANSACAO:
            print("\nLimite de transações diárias atingido.")
        else:
            saldo += valor
            numero_transacao += 1
            data_hora_atual = datetime.now().strftime(mascara_ptbr)
            historico_deposito.append((valor, data_hora_atual))
            print(f"\nVocê acaba de depositar: R$ {valor:.2f} reais.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um valor numérico.\n")

def deposito_2(saldo, numero_transacao, historico_deposito, LIMITE_TRANSACAO, mascara_ptbr):
    
    try:
        valor = float(input("\nQual valor deseja depositar? R$ "))
        if valor <= 0:
            print("\nNão é possível depositar este valor. Tente novamente.\n")
        elif numero_transacao >= LIMITE_TRANSACAO:
            print("\nLimite de transações diárias atingido.")
        else:
            saldo += valor
            numero_transacao += 1
            data_hora_atual = datetime.now().strftime(mascara_ptbr)
            historico_deposito.append((valor, data_hora_atual))
            print(f"\nVocê acaba de depositar: R$ {valor:.2f} reais.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um valor numérico.\n")

    return saldo, numero_transacao, historico_deposito, extrato

# def saque():
    global saldo
    global numero_transacao
    
    try:
        valor = float(input("Qual valor deseja sacar? R$ "))
        if valor <= 0:
            print("\nNão é possível sacar este valor. Tente novamente.\n")
        elif valor > saldo:
            print("\nNão é possível sacar este valor. Saldo indisponível.\n")
        elif (valor > limite):
            print("\nLimite de saque atingido. Não é possível efetuar esta transação.\n")
        elif (numero_transacao >= LIMITE_TRANSACAO):
            print("\nLimite de transações diárias atingido.")
        else:
            saldo -= valor
            numero_transacao += 1
            data_hora_atual = datetime.now().strftime(mascara_ptbr)
            historico_saque.append((valor, data_hora_atual))
            print(f"\nSaque efetuado com sucesso. Você acaba de sacar: R$ {valor:.2f} reais.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um valor numérico.\n")
        
def saque_2(*, saldo, numero_transacao, LIMITE_TRANSACAO, limite, mascara_ptbr, historico_saque):
    
    try:
        valor = float(input("Qual valor deseja sacar? R$ "))
        if valor <= 0:
            print("\nNão é possível sacar este valor. Tente novamente.\n")
        elif valor > saldo:
            print("\nNão é possível sacar este valor. Saldo indisponível.\n")
        elif (valor > limite):
            print("\nLimite de saque atingido. Não é possível efetuar esta transação.\n")
        elif (numero_transacao >= LIMITE_TRANSACAO):
            print("\nLimite de transações diárias atingido.")
        else:
            saldo -= valor
            numero_transacao += 1
            data_hora_atual = datetime.now().strftime(mascara_ptbr)
            historico_saque.append((valor, data_hora_atual))
            print(f"\nSaque efetuado com sucesso. Você acaba de sacar: R$ {valor:.2f} reais.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um valor numérico.\n")
    return saldo, numero_transacao, historico_saque

def exibir_extrato():
    print("\n----- Extrato de sua conta bancária -----\n")
    if not historico_deposito:
        print("\nNão houve depósitos nesta conta.")
    else:
        print("\nHistórico de Depósito:\n")
        for deposito, data_hora in historico_deposito:
            print(f"Data e hora da transação: {data_hora} Tipo da trasação: Depósito Montante: R$ {deposito:.2f}\n")
    if not historico_saque:
        print("\nNão houve saques nesta conta.")
    else:
        print("\nHistórico de Saque:\n")
        for saque, data_hora in historico_saque:
            print(f"Data e hora da transação: {data_hora} Tipo da trasação: Saque Montante: R$ {saque:.2f}\n")
    print(f"\nSaldo atual: = R$ {saldo:.2f}\n\nObrigado por utilizar os nossos serviço. Volte sempre!")
    
def exibir_extrato_2(saldo, /, *, historico_deposito, histórico_saque):
    

nome = input("Qual seu nome? ")

while(True):
    menu = f"""
    Olá, {nome}. Bem-vindo à sua conta. Por gentileza, escolha uma opção:

    [1] Depositar
    [2] Sacar
    [3] Ver extrato
    [4] Sair

    """
    
    opcao = int(input(menu))
    if opcao == 1:
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 4:
        print("\nObrigado por utilizar os nossos serviços. Volte sempre!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha entre as seguintes opções: [1] Depositar, [2] Sacar, [3] Ver extrato, [4] Sair\n")