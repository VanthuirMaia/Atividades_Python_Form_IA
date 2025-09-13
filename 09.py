# 9. Peça um número e exiba sua tabuada de 1 a 10

num = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada de {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    