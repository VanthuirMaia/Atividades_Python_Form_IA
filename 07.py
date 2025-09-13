# 7. Leia um número e informe se ele é positivo, negativo ou zero.

num = int(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")