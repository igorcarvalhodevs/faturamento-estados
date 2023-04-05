# Valores de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Somando todos os valores de faturamento para obter o valor total mensal
total_mensal = sum(faturamento.values())

# Calculando o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentuais[estado] = (valor / total_mensal) * 100

# Exibindo o percentual de representação de cada estado
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')