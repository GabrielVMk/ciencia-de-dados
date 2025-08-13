import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = [120, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
quartis = np.percentile(dados [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

plt.boxplot(dados, vert=False)
plt.title('Meses')
plt.xlabel('Vendas')
plt.show
plt.savefig('chartrecuperacao.png')