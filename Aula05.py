import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#conjunto de dados exs
dados = [10, 20 , 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]

#calculando o quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

#calcular decis
decis = np.percentile(dados, [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f'Decis: {decis}')

#calculando percentis
percentis = np.percentile(dados, [10, 25, 50, 75, 90])
print(f'Percentis: {percentis}')

#visualização do BoxPlot
plt.boxplot(dados, vert=False)
plt.title('BoxPlot das Notas')
plt.xlabel('Notas')
plt.show
plt.savefig('chart5.png')
