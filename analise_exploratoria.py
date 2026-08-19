"""
Análise Exploratória de Churn - Projeto Chatuba x ObraMax
Objetivo: identificar padrões de clientes que cancelam (churn)
          em uma rede fictícia de materiais de construção.
"""

import pandas as pd

# 1. Carregar os dados
# Baixe um dataset de churn no Kaggle (ex: "Telco Customer Churn") 
# e coloque o arquivo .csv na mesma pasta do script.
df = pd.read_csv("churn_data.csv")

# 2. Primeira olhada nos dados
print("Primeiras linhas:")
print(df.head())

print("\nInformações gerais (tipos de dados, valores nulos):")
print(df.info())

print("\nEstatísticas básicas das colunas numéricas:")
print(df.describe())

# 3. Quantos clientes cancelaram (churn) vs quantos ficaram?
# Ajuste "Churn" para o nome real da coluna no seu dataset
print("\nDistribuição de churn:")
print(df["Target_Churn"].value_counts())
print(df["Target_Churn"].value_counts(normalize=True) * 100)  # em percentual

# 4. Valores nulos por coluna (dados faltando)
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# 5. Próximo passo (não implementado ainda):
# - Cruzar churn com tempo de contrato, forma de pagamento, etc.
# - Gerar gráficos com matplotlib/seaborn
