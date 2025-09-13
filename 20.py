# 20. Crie uma função que receba uma string e retorne se ela é um palíndromo.

def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = input("Digite uma string: ")
if eh_palindromo(string):
    print(f'"{string}" é um palíndromo.')
else:
    print(f'"{string}" não é um palíndromo.')
