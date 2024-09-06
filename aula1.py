for numero in range(0, 51, 5):
    print(numero, end=" ")
    
    # While precisa de break
    # Continue pula na condição
    
    while opcao != 0:
        opcao = int(input("[1] Sacar \n [2] Extrato \n [3] Sair \n"))
        
#r ou l ou .strip() remove espaço
#.center(10, " ") centraliza o string com o número de caracteres total
# (" ".join(variável)) coloca o caractere definido item a item

# print(f"Olá, me chamo {nome} e tenho {idade} anos. )
# print("Olá, me chamo {} e tenho {} anos.".format(nome, idade))
# print("Olá, me chamo {nome} e tenho {idade} anos.".format(nome=nome, idade=idade))
# print("Olá, me chamo {nome} e tenho {idade} anos.".format(**pessoa)) dicionário pessoa

# nome[start:stop:step] fatiamento de string
# print(˜˜˜
# blab
# 
# bblablabl
# 
# ablababa
# ˜˜˜) mantem a forma

# quando você dá um valor ao argumento (="valor") ele é utilizado quando não dá um valor na hora que a chama

def retorna_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor
print(retorna_antecessor(numero="4"))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso!    (marca)/(modelo)/(ano)/(placa)")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # se o usuário colocar valores em posições erradas, o programa não saberá e o print não seguirá a ordem
salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="ABC-1234") # quando nomeia, não importa a posição do argumento na função, o print seguirá a ordem
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": "1999", "placa":"ABC-1234"}) # funciona com o 2o

 # *args, *kwargs
 
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Quinta, 29 de Agosto de 2024", "Será que eu entendi", "o que eu fiz nesse código?", "não sei,", "veremos!", autor="Caio Silva", ano=2024)

# Parâmetros especiais (nomeados ou posicionais)
# / o que está antes é apenas posicional (não precisa nomear a chave)
# o que estiver após o / é opcional ser nomeado ou posicional
# * o que está após é apenas nomeado (precisa indicar)

def criar_carro(modelo, ano, placa, / marca, motor, combustivel):
    print(modelo,ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # funciona
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # não funciona


