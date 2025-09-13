# 23. Crie uma função que receba uma lista e retorne a lista sem elementos repetidos.

def remover_repetidos(lista):
    return list(set(lista))

# Exemplo de uso
entrada = ["A", "B", "A", "C", "B", "D"]
lista_sem_repetidos = remover_repetidos(entrada)

print("Lista sem repetidos:", sorted(lista_sem_repetidos))
