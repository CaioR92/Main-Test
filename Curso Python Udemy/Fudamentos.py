# Fundamentos básicos
movie_name = "Top Gun"
movie_name2 = "top Gun"
print(movie_name == movie_name2) # Case sensitve; False

# Saber o tipo
print(type(variável))

# 1- Multiplicação de Strings
line = "="
print(line*50)

# 2- Procurar uma palavra dentro de um texto
print("top" in movie_name2)

# 3- Buscar string a partir da primeira posição
print(movie_name[0:])

#4- Buscar até a última posição
print(movie_name[:7])

#5- Buscar do número x até a última
print(movie_name[x:])

#6- A cada intervalo x
print(movie_name[::x])

#7- Inverter a string
print(movie_name[::-1])

#8- Outro métodos e operações
print(movie_name.upper()) # Tudo maiúsculo
print(movie_name.lower())# Tudo minúsculo
print(movie_name.capitalize()) # Primeira letra da primeira palavra
print(movie_name.title()) # Primeira letra maiúscula de cada palavra
print(movie_name.center(x, '-')) # Retorna string centralizada com caractere de preenchimento
print(movie_name.find("x")) # Retorna o index da primeira ocorrência do caractere
print(movie_name.count("x")) # Retorna quantas vezes x aparece
print(movie_name.replace("x", "y")) # Altera x por y
print(movie_name.split(',')) # Divide a string a cada vírgula

# Listas

lista_filmes = ["Matrix", 1999, 8.7, True]
lista_filmes2 = ["Matrix", "Inception", "Casa Vazia",
                 "Pulp Fiction"]

#1- Buscar os x primeiro itens da lista
print(lista_filmes2[:2])

#2- Buscar o último
print(lista_filmes2[-1])

#3- Buscar itens até uma determinada posição
print(lista_filmes2[:3])

#4- Buscar filmes de uma posião em diante
print(lista_filmes2[x:y])

#5- Tamanho da Lista
print(len(lista_filmes2))

#6- Mostra o index de um item da lista pelo nome
print(lista_filmes2.index("Pulp Fiction"))

#7- Adicionar item na lista
lista_filmes.append("xxxxxx")

#8- Ordenar lista
lista_filmes2.sort()

#9- Copiar lista para outra
lista_filmes2 = lista_filmes.copy()

#10- Remover item
lista_filmes2.remove("xxx")

#11- Remove todos os itens da lista
lista_filmes2.clear()

# Tupla
tupla_filmes = ("Matrix", "Inception", "Casa Vazia",
                 "Pulp Fiction")

# Set
set_filmes = {"Matrix", "Inception", "Casa Vazia",
                 "Pulp Fiction"}

set_filmes.update(outroset) # Adiciona itens de outro set

# Dicionário
dic_filmes = {"Title": "Pulp Fiction",
              "ano": "1994",
              "genero": ["Ação, Thriller"],
              "rating": 9.5}

print(len(dic_filmes))
print(type(dic_filmes))

#1- Recuperar um elemento do dicionário
print(dic_filmes["ano"])
print(dic_filmes.get("x"))

#2- Buscar chaves
print(dic_filmes.keys())

#3- Buscar valores
print(dic_filmes.values())

#4- Buscar itens com chave e valor
print(dic_filmes.items())

#5- Adicionar itens
dic_filmes["Title"] = "xxx"

#6- Atualizar itens
dic_filmes.update({"ano": "xx"})

#7- Remover item
dic_filmes.pop("rating")


filmes_dic = {
    "Pulp Fiction":{
        "ano": 1994,
        "rating": 9.5,
        "gênero": ["drama", "thriller"]
    },
    "Tudo sobre minha mãe":{
        "ano:" 1999
        "rating": 9.5,
        "gênero": ["drama"]
        }"
}

#import pprint (melhora a visualização de dicionários)
# pp = pprint.PrettyPrinter(depth=4)
pp.pprint(dic_filmes)

#1- Buscar uma info em um dic aninhado
print(filmes_dic["Pulp Fiction"]["gênero"])

#2- Adicionar nova chave: valor
filmes_dic["Pulp Fiction"]["diretor"] = "Tarantino"

#3- Deletar item
del filmes_dic["Tudo sobre minha mãe"]

# break; quando a condição for atendida, o loop será encerrado
# continue; quando a condição for atendida, o lopp vai para a próxima iteração
# for i in range(lista)

# List comprehension
lista_filmes2e = [movie for movie in lista_filmes2 if "e" in movie.lower()]

# Encontrando o filme pelo nome
while True:
    searchmovie = input("Digite o nome do filme: ")
    if searchmovie.lower() == "sair":
        print("Adeus")
        break
    
procurarfilme = [movie for movie in lista_filmes2 if searchmovie.lower() in movie.lower()]
if procurarfilme:
    print(f"Filme {searchmovie} encontrado")
    for filme in procurarfilme:
        print(filme)
else:
    print("Filme não encontrado.")
    
# Função recursiva
# Fatorial de um número:
# 1 -> 1 * 1 = 1
# 2 -> 2 * 1 = 2 * (fatorial(1)) = 2
# 3 -> 3 * 2 * 1 = 3 * (fatorial(2)) = 6
# Ou seja, uma função que volta a ela mesma

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

# Args e Kwargs
# *Args = quando não temos certeza quantos argumentos queremos na função
# os argumentos são chamados como tupla

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(sum_total)

# **Kwargs = quando precisamos passar chaves para argumentos. São passados como dicionários.

def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

presentation(name="Python", category="Backend", level="Iniciante")

# Função Lambda - função anônima; pode ser utilizada como parâmetro em outras funções

power = lambda num: num ** 2
is_even = lambda x: x % 2 == 0

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

check_movie = lambda movie_name: movie_name in movies_list

recommended_movie = lambda movie_name: f"recomendo assistir {movie_name}"