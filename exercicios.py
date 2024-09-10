#caso numero 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor final de SOMA é: {SOMA}")

#caso numero 2
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# caso numero 3

import json

# Exemplo de dados de faturamento em JSON
dados_faturamento = '''
{
    "faturamento": [100, 200, 0, 300, 400, 0, 500, 600, 0, 700, 0, 800, 900, 1000]
}
'''

# Parse do JSON
faturamento_diario = json.loads(dados_faturamento)['faturamento']

# Filtra os dias com faturamento > 0
faturamento_valido = [f for f in faturamento_diario if f > 0]

# Calcula o menor, maior faturamento e a média
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Conta o número de dias com faturamento superior à média
dias_acima_da_media = len([f for f in faturamento_valido if f > media_mensal])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# caso numero 4

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}% do faturamento total")


# caso numero 5

def inverter_string(s):
    string_invertida = ""
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Digite uma string: ")
print("String invertida:", inverter_string(string))
