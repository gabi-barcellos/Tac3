import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
from estatisticas_pandas_script import valor_maximo, valor_minimo, media_valores, soma_total, Xpais_decrescente, normalizar


max_input = int(input("Digite o numero da coluna para retornar o valor máximo: 1- Total_cases, 2-Total_deaths, 3-Total_recovered, 4-Population: "))
min_input = int(input("Digite o numero da coluna para retornar o valor minimo: 1- Total_cases, 2-Total_deaths, 3-Total_recovered, 4-Population: "))
media_input = int(input("Digite o numero da coluna para retornar o valor medio: 1- Total_cases, 2-Total_deaths, 3-Total_recovered, 4-Population: "))
total_input = int(input("Digite o numero da coluna para retornar o valor total: 1- Total_cases, 2-Total_deaths, 3-Total_recovered, 4-Population: "))
coluna_xpais = int(input('Digite a quantidade de países com maior número de casos que você deseja visualizar: '))



arquivo = pd.read_excel(r"C:/Users/gabri/Downloads/covid_cases_23_01_2021_clean.xlsx")
df = pd.DataFrame(arquivo)



val_maximo = valor_maximo(df, max_input)
val_minimo = valor_minimo(df, min_input)
val_media = media_valores(df, media_input)
val_total = soma_total(df, total_input)
paisdecres = Xpais_decrescente(df, coluna_xpais)
norma_lizar = normalizar(df)

print('Esse é o valor máximo: {}'.format(val_maximo))
print('Esse é o valor minimo: {}'.format(val_minimo))
print('Esse é o valor médio: {}'.format(val_media))
print('Esse é o valor total: {}'.format(val_total))
print('Os paises do top: {}'.format(paisdecres))
print('Dados normalizados: {}'.format(norma_lizar))
