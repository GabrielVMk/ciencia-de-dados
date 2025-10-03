import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# faz a leitura o arquivo CSV a partir de uma url ou arquivo.
dados = pd.read_csv('./aula08/desmatamento_prodes.csv')

# exibindo os dados
print(dados)

print('-+-' * 50)

#exibindo a matris de correlação de pearson
#Fornecendo uma pré-analise dos dados para encontras.
#Correlações fortes possitivas/negativas ou sem correlação
print(dados.corr().round(2)) 

#Fazendo analise em pares 
sns.pairplot(dados)
plt.show()
plt.savefig('./aula08/pairplot.png')

# Fazando analise individual para correlação positiva
# x = avriavel dependente (Mato Grosso)
# y = variavel explicativa (Rondonia)
sns.lmplot(data= dados, x = 'mato_grosso', y= 'rondonia')
plt.show()

#Litura: conforme aumenta o desmatamento do Mato Grosso,
# aumenta o desmatamento em Rondônia, onde a correlaçâo de ambos é de 0.93            
plt.savefig('./aula08/lmplot-positivo.png')

# Fazando analise individual para correlação forte negativa
# x = avriavel dependente (Referencia)
# y = variavel explicativa (Tocantins)
sns.jointplot(data= dados, x= 'referencia', y= 'tocantins', kind='reg')
plt.show()

#Leitura: conforme passa os anos , a área total de desmatamento de Tocantins
#diminui com sua correlação de -0.74
plt.savefig('./aula08/jointplot-negativo.png')