import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo.
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Define o tamanho da janela de plotagem
    plt.figure(figsize = (10, 6)) # A função figure() controla a largura, a altura, a resolução e a cor de fundo do gráfico.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)
    # Enfatiza o primeiro e o último ponto.
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 50) # [B] Pinta o primeiro ponto de verde e com um círculo de maior diâmetro.
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 50) # [B] Pinta o último ponto de vermelho e com um círculo de maior diâmetros.
    # Remove os eixos
    plt.axes().get_xaxis().set_visible(False) # [B] Comando complicado para deixar o eixo x oculto.
    plt.axes().get_yaxis().set_visible(False) # [B] Comando complicado para deixar o eixo y oculto.
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
