# Desafio de projeto 1: Criando um sistema bancário (sacar, depositar e visualizar extrato)
# Valor inteiro e positivo para deposito
# Histórico dos depósitos no extrato
# 3 saques diários com o limite de 500 reais cada
# Mensagem informando se não houver dinheiro
# Histórico de saques no extrato
# Exibir saldo atual da conta no fim do extrato

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
historico_saque = []
historico_deposito = []

def deposito():
    global saldo
    global historico_deposito
    
    valor = int(input("Qual valor deseja depositar? "))
    if valor <= 0:
        print("Não é possível depositar este valor. Tente novamente.")
    else:
        print(f"Você acaba de depositar R$  {valor} reais.")
        saldo += valor
        historico_deposito.append(valor)

def saque():
    global saldo
    global numero_saque
    
    valor = int(input("Qual valor deseja sacar?"))
    if valor <= 0:
        print("Não é possível sacar este valor. Tene novamente.")
    elif valor > saldo:
        print("Não é possível sacar este valor. Saldo indisponível.")
    elif (valor > limite) or (numero_saque >= LIMITE_SAQUE):
        print("Limite de saque atingido.")
    else:
        saldo -= valor
        numero_saque += 1
        historico_saque.append(valor)
        print(f"Saldo efetuado com sucesso. Você acaba de sacar R$ {valor} reais.")

# VERIFICAR MENU E INPUT

nome = input("Qual seu nome?")

while(True):
    menu = print(f"""
    Olá, {nome}. Bem-vindo à sua conta. Por getileza, escolha uma opção:\n

    [1] Depositar\n
    [2] Sacar\n
    [3] Ver extrato\n
    [4] Sair\n

    """)
    
    opcao = int(input(menu))
    if opcao == 1:
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        extrato = print(f"""----- Extrato de sua conta bancária -----
          
          Histórico de Depósito = {historico_deposito}
          
          Histórico de Saque = {historico_saque}
          
          Saldo atual = {saldo}
          
          Obrigado por usar os nossos serviço. Volte sempre!
          
          """)
    
    elif opcao == 4:
        print("Obrigado por usar os nossos serviço. Volte sempre!")
    else:
        print("Opção inválida. Por favor, escolha entre as seguintes opções: [1] Depositar, [2] Sacar, [3] Ver extrato, [4] Sair\n")
