import pandas as pd



def converte_colunas (coluna):
      if (coluna == 1):
        return 'Total_cases'
      if (coluna == 2):
        return 'Total_deaths'
      if (coluna == 3):
          return 'Total_recovered'
      elif (coluna == 4):
          return 'Population'


def valor_maximo (df, coluna):
    nomecoluna = converte_colunas(coluna)
    return df[nomecoluna].max()

def valor_minimo (df, coluna):
    nomecoluna = converte_colunas(coluna)
    return df[nomecoluna].min()


def media_valores (df, coluna):
    nomecoluna = converte_colunas(coluna)
    return df[nomecoluna].mean()


def soma_total (df, coluna):
    nomecoluna = converte_colunas(coluna)
    return df[nomecoluna].sum()

def Xpais_decrescente (df, coluna_xpais):
    df.sort_values(['Total_cases'], ascending=False)
    return df.nlargest(coluna_xpais, 'Total_cases')

def normalizar (df):
    for index in df:
        novacoluna = df['Total_cases']*100000 / df['Population']
        df['Total_cases_per_100mil'] = novacoluna
    return df