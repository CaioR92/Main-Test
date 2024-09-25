import math_operations

print(math_operations.sum(5, 6))

from math_operations import divide, sum
print(divide(5, 6))

# No terminal: chamar python; help('modules') -> para acessar módulos nativos
# Módulos: OS, Regex, HTTPServer, Math, Statistic, Hashlib, Colletcions, Random, Tkinter

# Contagem:
# from collections import counter

# namedtuple:
game = namedtuple('game', ['name', 'price', 'rating'])
g1 = game()

# ordenar dicionários:
students = {"Pedro": 28, "Ana": 32, "Tiago": 22, "Jurema": 40}
a = sorted(students.items(), key = itemgetter(0)) #vai ordenar pela chave
print(a)

# Adicionando fila em ambas extremidades
deq = deque([20, 30, 40, 50, 60, 70])
deq.appendleft(10)
deq.popleft()

# random:
# selecione valor aleatório
list1 = [7, 6, 5, 4, 3, 2, 8]
print(random.choice(list1))

# Gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)

# Valor aleatório de uma string
name = "Python"
r2 = random.choice(name)

# Selecionar mais de um valor aleatório
# random.sample(sequencia, tamanho)

# Programa de sorteio:
done = False
while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o número")
    print("2. Sair")
    
    choice = input(">")
    if choice == "1":
        print("==========Advinhe um número de 1 a 10.===========")
        number = int(input("Digite um número de 1 a 10"))
        result = random.randint(1, 10)
        if number == result:
            print("Você acertou!")
        else:
            print(f"Tente novamente. O número sorteado foi: {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida")
        
# Módulo Tkinter (construtor de aplicações desktop)
