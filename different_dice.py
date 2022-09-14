from die import Die
import pygal

# Cria uma D6 e um D10

die_1 = Die()
die_2 = Die(10) # Passei o 10 como parâmetro para mudar a quantidade de lados.

# Faz alguns lançamentos e armazena os resultados em uma lista
results = [] # Lista vazia para receber os valores dos lançamentos.

for roll_num in range(5000):
    result =  die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling one D6 and D10 50 000 times." # Título do Gráfico
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] # Valores do eíxo x
hist.x_title = "Result" # Título do eixo x
hist.y_title = "Frequency of Result" # Título do eixo y
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual2.svg')
