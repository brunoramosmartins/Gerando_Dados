from die import Die
import pygal
# Cria um D6
die = Die()
# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value) # começa a contar os valores a partir do 1.
    frequencies.append(frequency)

dic = {}

for i in results:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print (results)
print (frequencies)
print (dic) # Percebi que os valores não ficam na ordem. (os índices)

hist = pygal.Bar() # Gráfico de barras.
hist.title = "Results of rolling one D6 1000 times." # Título do Gráfico
hist.x_labels = ['1', '2', '3', '4', '5', '6'] # Valores do eíxo x
hist.x_title = "Result" # Título do eixo x
hist.y_title = "Frequency of Result" # Título do eixo y
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
