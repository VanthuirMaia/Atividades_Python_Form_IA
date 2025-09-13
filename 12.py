# 12. Leia uma frase e conte quantas vogais ela possui.

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = sum(1 for vogal in frase if vogal in vogais) # Conta as vogais na frase
print(f"A frase possui {contador} vogais.")