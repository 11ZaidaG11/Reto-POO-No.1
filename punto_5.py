user: str = input("Ingrese las palabras separadas por comas: ")
user = user.split(",")
all_num: list = []
for word in user:
    num: list = []
    for c in word:
        num.append(ord(c))
    num.sort()
    all_num.append(num)
print(all_num)

equal: list = []
for i in range(len(all_num)-1):
    if all_num[i] == all_num[i+1]:
        equal.append(all_num[i])
print(equal)