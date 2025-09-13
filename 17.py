# 17. Solicite 10 números e exiba o maior e o menor

numeros = []
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
maior = max(numeros)
menor = min(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")