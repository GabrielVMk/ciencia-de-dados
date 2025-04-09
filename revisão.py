import matplotlib.pyplot as plt #gera o grafico
import pandas as pd #organisar e ter dados kestatisticos

#organisa os dados de melhor forma
df = pd.DataFrame({
    "time": ["Gremio", "Inter", "Juventus"],
    "pontos": [30, 1, 10]

})

plt.bar(df['time'], df['pontos'], color=['blue', 'red', 'orange'])

plt.title('Pontos por times gáuchos do campeonato')
plt.xlabel('times')
plt.ylabel('pontos')

plt.show()
plt.savefig('chart.png')
