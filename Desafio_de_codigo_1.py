# Desafio de projeto 1: Criando um sistema bancário (sacar, depositar e visualizar extrato)
# Valor inteiro e positivo para deposito
# Histórico dos depósitos no extrato
# 3 saques diários com o limite de 500 reais cada
# Mensagem informando se não houver dinheiro
# Histórico de saques no extrato
# Exibir saldo atual da conta no fim do extrato

menu = print("""
Olá, f'{nome}. Bem-vindo à sua conta. Por getileza, escolha uma opção

[1] Depositar
[2] Sacar
[3] Ver extrato
[4] Sair

"""
)

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

def deposito():
    print("Qual valor deseja depositar?")
    depositar = int(input()
        if int(input) ≤ 0:
            print("Não é possível depositar este valor.")
        else
            print(f"Você acaba de depositar {input} reais.")
    novo_saldo = depositar + saldo
    

while (True):
    opcao = input(menu)