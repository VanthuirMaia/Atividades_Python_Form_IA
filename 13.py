# 13. Solicite 5 números e exiba a média deles.

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))

media = (num1 + num2 + num3 + num4 + num5) / 5
print(f"A média dos números é: {media:.2f}")