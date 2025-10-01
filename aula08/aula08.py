import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pl

# faz a leitura o arquivo CSV a partir de uma url ou arquivo.
dados = pd.read_csv('./aula08/desmatamento_prodes.csv')

# exibindo os dados
print(dados)

print('-+-' * 50)

#exibindo a matris de correlação de pearson
#Fornecendo uma pré-analise dos dados para encontras.
#Correlações fortes possitivas/negativas ou sem correlação
print(dados.corr().round(2)) 