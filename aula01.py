# faZ a importação da biblioteca matplotlib e adicionar um alias (apelido)
# usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    # Definição dos grupos e valores
    filmes = ['Filme A', ' Filme B', 'Filme C', 'Filme D', 'Filme E']
    notas = [7.8, 8.2, 6.9, 8.5, 7.3 ]

    # Configura um gráfico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(filmes, notas, color=['darkred', 'darkgreen', 'darkblue', 'darkorange', 'darkviolet'])

    # Define o título do gráfico
    plt.title('Grupo 6- Avaliação de filmes')

    # Define o título do eixo X
    plt.xlabel('Filme')

    #defini o titulo do eixo y
    plt.ylabel('Notas')

    #cria o gráfico
    plt.show()

    #salva dentro do arquivo de imagen
    plt.savefig('chart.png')
