# faZ a importação da biblioteca matplotlib e adicionar um alias (apelido)
# usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    # Definição dos grupos e valores
    grupos = ['A', 'B', 'C']
    valores = [23, 38, 12]

    # Configura um gráfico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(grupos, valores, color=['red', 'blue', 'grey'])

    # Define o título do gráfico
    plt.title('Gráfico de Barras Simples')

    # Define o título do eixo X
    plt.xlabel('Grupos')

    #defini o titulo do eixo y
    plt.ylabel('Valores')

    #cria o gráfico
    plt.show()

    #salva dentro do arquivo de imagen
    plt.savefig('chart.png')
