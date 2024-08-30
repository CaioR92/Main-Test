# Desafio de projeto 1: Criando um sistema bancário (sacar, depositar e visualizar extrato)
# Valor inteiro e positivo para deposito
# Histórico dos depósitos no extrato
# 3 saques diários com o limite de 500 reais cada
# Mensagem informando se não houver dinheiro
# Histórico de saques no extrato
# Exibir saldo atual da conta no fim do extrato
# Valores em R$ xxx.xx

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
    # global extrato
    
    valor = float(input("Qual valor deseja depositar? "))
    if valor <= 0:
        print("Não é possível depositar este valor. Tente novamente.")
    else:
        saldo += valor
        historico_deposito.append(valor)
        # extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Você acaba de depositar R$  {valor:.2f} reais.")
    # Adicionar linha para inputs que não sejam números


def saque():
    global saldo
    global numero_saque
    # global extrato
    
    valor = float(input("Qual valor deseja sacar?"))
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
        # extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saldo efetuado com sucesso. Você acaba de sacar R$ {valor:.2f} reais.")
    # Adicionar linha para inputs que não sejam números


# escrever def exibir_extrato

# VERIFICAR MENU E INPUT

nome = input("Qual seu nome?")

while(True):
    menu = f"""
    Olá, {nome}. Bem-vindo à sua conta. Por getileza, escolha uma opção:\n

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
        extrato = f"""----- Extrato de sua conta bancária -----
          
          Histórico de Depósito = {historico_deposito}
          
          Histórico de Saque = {historico_saque}
          
          Saldo atual = {saldo:.2f}
          
          Obrigado por usar os nossos serviço. Volte sempre!
          
          """
        print(extrato)
    
    elif opcao == 4:
        print("Obrigado por usar os nossos serviço. Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha entre as seguintes opções: [1] Depositar, [2] Sacar, [3] Ver extrato, [4] Sair\n")
    # Adicionar linha para inputs que não sejam números
