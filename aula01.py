# faZ a importação da biblioteca matplotlib e adicionar um alias (apelido)
# usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']
    populacao = [12300, 6700, 2800, 1500, 1940]
    
    plt.bar(cidades, populacao, color=['red', 'blue', 'grey'])
    plt.title('grafico de barra simples')
    plt.xlabel('cidades')
    plt.show()
    plt.savefig('chart.png')
