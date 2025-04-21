import random


def create_list():
    list_random: list = []
    lon: int = random.randrange(5, 16)

    for _ in range(lon):
        elem = random.randrange(1, 101)
        list_random.append(elem)
    return list_random

def verification(list_random:list):
    list_prime: list = []

    for n in list_random:
        dividers = []

        for i in range(1, n+1):
            if n % i == 0:
                dividers.append(i)
        if len(dividers) == 2:
            list_prime.append(i)
                
    if not list_prime:
        return "Niniguno"
    else:
        return list_prime


if __name__ == "__main__":
    cl = create_list()
    v = verification(cl)
    print("En la lista:", cl)
    print("Los numeros primos son:", v)