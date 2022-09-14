from die import Die
import pygal
# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
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
hist.title = "Results of rolling two D6 1000 times." # Título do Gráfico
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] # Valores do eíxo x
hist.x_title = "Result" # Título do eixo x
hist.y_title = "Frequency of Result" # Título do eixo y
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
