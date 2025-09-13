# 24. Crie uma função que inverta uma string.

def inverter_string(s):
    return s[::-1]

# Exemplo de uso
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
