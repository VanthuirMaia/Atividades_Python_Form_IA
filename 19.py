# 19. Crie uma função que receba uma lista de números e retorne a soma.

def soma_lista(lista):
    return sum(lista)

numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para parar): ")
    
    if entrada.lower() == "sair":
        break
    
    if entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit()):
        numeros.append(int(entrada))
    else:
        print("Valor inválido! Digite apenas números ou 'sair'.")

resultado = soma_lista(numeros)
print(f"A soma dos números digitados é: {resultado}")
