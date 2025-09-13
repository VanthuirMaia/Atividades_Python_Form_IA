# 18. Crie uma função que receba dois números e retorne a multiplicação.

def multiplicar(num1, num2):
    return num1 * num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = multiplicar(num1, num2)
print(f"O resultado da multiplicação é: {resultado}")