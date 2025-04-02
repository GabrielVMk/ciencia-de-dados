import matplotlib.pyplot as plt

import pandas as pd
def exibirGrafico():
    # criando o DataFrame
    df = pd.DataFrame({
        "Meses" : ['Jan', 'Fev', 'Mar', 'abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        "Temperaturas" : [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })
    
    #redimensionamdo o grafico
    plt.figure(figsize=[10.0, 5.0])

    #criando o grafico
    plt.plot(df['Meses'], df['Temperaturas'], color="cyan")

    #definindo os titulos
    plt.title("Temperatura média ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("Temperaturas")

    #exixbindo o garfico
    plt.show()
    plt.savefig('chart2.png')

    print(f'Temperaturas: \n{df['Temperaturas'].describe()}')