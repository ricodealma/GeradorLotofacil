import pandas as pd
import random

git add lotofacil.py
git commit -m "Adiciona código de geração de combinações da Lotofácil"
git push origin main

# Carrega os resultados da Lotofácil do arquivo Excel
resultados_lotofacil = pd.read_excel('caminho/para/o/arquivo_excel.xlsx')

# Obtém a lista de números sorteados em todos os resultados
numeros_sorteados = []
for resultado in resultados_lotofacil['Números Sorteados']:
    numeros_sorteados += resultado.split()

# Conta a frequência de cada número sorteado
frequencia_numeros = dict()
for numero in numeros_sorteados:
    if numero in frequencia_numeros:
        frequencia_numeros[numero] += 1
    else:
        frequencia_numeros[numero] = 1

# Ordena os números por frequência em ordem decrescente
numeros_ordenados = sorted(frequencia_numeros, key=frequencia_numeros.get, reverse=True)

# Gera uma nova combinação de números com base na frequência
nova_combinacao = []
while len(nova_combinacao) < 15:
    numero = numeros_ordenados.pop(0)
    nova_combinacao.append(numero)

# Completa a nova combinação com números aleatórios até ter 15 números
while len(nova_combinacao) < 15:
    numero = str(random.randint(1, 25))
    if numero not in nova_combinacao:
        nova_combinacao.append(numero)

# Exibe a nova combinação gerada
print("Combinação de maior probabilidade de sorteio:")
print(" ".join(nova_combinacao))
