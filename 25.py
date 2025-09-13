# 25. Implemente um programa que leia 10 notas e calcule a média da turma.

def calcular_media(notas):
    return sum(notas) / len(notas)

# Exemplo de uso
notas = []
for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = calcular_media(notas)
print("Média da turma:", media)
