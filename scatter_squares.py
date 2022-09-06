import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap =plt.cm.Blues, edgecolor = 'none', s = 40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.show()

# Podemos salvar os gráficos automaticamente em um arquivo.
# Para isso, basta substituir plt.show por uma chamada plt.savefig(): plt.savefig('squares_plot.png', bbox_inches = 'tight')
# O primeiro argumento é o nome de um arquivo para imagem do gráfico, que será salvo no mesmo diretório do arquivo .py
