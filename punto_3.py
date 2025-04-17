import random

prime = False
list_prime: list = []
list_random: list = []
l: int = random.randrange(5, 16)

for i in range(l):
    elem = random.randrange(1, 101)
    list_random.append(elem)

for n in list_random:
    suma = 0
    list_b = []
    list_c = []

    for i in range(2, n+1):
        list_b.append(i)
        for e in list_b:
            if n // e == 0:
                list_c.append(e)
        if len(list_c) == 2:
            list_prime.append(i)
            
if not list_prime:
    print("No hay numeros primos en la lista")


print(l)
print(list_random)
print(list_b)
print(list_c)
print(list_prime)