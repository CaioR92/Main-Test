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

from datetime import datetime

mascara_ptbr = "%d/%m/%Y %H:%M"
data_hora_atual = datetime.now().strftime(mascara_ptbr)
    
def listar_contas(contas):
    for conta in contas:
        print(f"""Titular: {conta["usuario"]["nome"]}
              "C/C: {conta["nro_conta"]}
              "Agência: {conta["agencia"]}"
              """)
    
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nEste CPF já foi utilizado para cadastro de usuário.")
        return
    
    nome = input("Por gentileza, digite seu nome completo: ")
    data_nascimento = input("Por gentileza, informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Por gentileza, informe seu endereço competo (logradouro, número - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário cadastrado com sucesso!\n")

def filtrar_usuario(cpf, usuarios):
   usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(usuarios, AGENCIA, nro_conta, contas):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        nro_conta_str = str(nro_conta).zfill(5)
        print("\nConta criada com sucesso!\n")
        contas.append({"usuario": usuario, "nro_conta": nro_conta_str, "agencia": AGENCIA})
        nro_conta += 1
        return nro_conta
    else:
        print("\nUsuário não encontrado. Por favor, cadastre um usuário para poder criar uma conta.\n")
        return nro_conta

def deposito_2(saldo, valor, numero_transacao, historico_deposito, LIMITE_TRANSACAO, mascara_ptbr, /):
    
    try:
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

    return saldo, numero_transacao, historico_deposito

def saque_2(*, saldo, valor, numero_transacao, LIMITE_TRANSACAO, limite, mascara_ptbr, historico_saque):
    
    try:
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

def exibir_extrato_2(saldo, /, *, historico_deposito, historico_saque):
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
    
def main():

    mascara_ptbr = "%d/%m/%Y %H:%M"
    data_hora_atual = datetime.now().strftime(mascara_ptbr)

    AGENCIA = "0001"
    LIMITE_TRANSACAO = 10

    saldo = 0
    limite = 500
    extrato = ""
    numero_transacao = 0
    historico_saque = []
    historico_deposito = []
    usuarios = []
    contas = []
    nro_conta = 1

    while(True):

        menu = f"""
        Olá, Bem-vindo à sua conta. Por gentileza, escolha uma opção:

        [1] Depositar
        [2] Sacar
        [3] Ver extrato
        [4] Cadastrar usuário
        [5] Criar Conta Corrente
        [6] Listar Contas
        [7] Sair

        """
        
        opcao = int(input(menu))
        if opcao == 1:
            valor = float(input("\nQual valor deseja depositar? R$ "))
            saldo, numero_transacao, historico_deposito = deposito_2(saldo, valor, numero_transacao, historico_deposito, LIMITE_TRANSACAO, mascara_ptbr)
        elif opcao == 2:
            valor = float(input("\nQual valor deseja sacar? R$ "))
            saldo, numero_transacao, historico_saque = saque_2(
            saldo=saldo,
            valor=valor,
            numero_transacao=numero_transacao,
            LIMITE_TRANSACAO=LIMITE_TRANSACAO,
            limite=limite,
            mascara_ptbr=mascara_ptbr, 
            historico_saque=historico_saque,
            )
        elif opcao == 3:
            exibir_extrato_2(saldo, historico_deposito=historico_deposito, historico_saque=historico_saque)
        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            nro_conta = criar_conta(usuarios, AGENCIA, nro_conta, contas)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 7:
            print("\nObrigado por utilizar os nossos serviços. Volte sempre!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha entre as seguintes opções: [1] Depositar, [2] Sacar, [3] Ver extrato, [4] Sair\n")

main()