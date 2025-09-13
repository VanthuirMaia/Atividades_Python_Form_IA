# 15. Leia uma lista de 10 números e exiba apenas os pares

numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
pares = [num for num in numeros if num % 2 == 0]
print("Números pares na lista:", pares)
