import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtém as temperaturas máximas do arquivo
filename = 'sitka_weather_2018_full.csv'
with open(filename)  as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        if row[8] != "":
            high =int(row[8])
            highs.append(high)
        else:
            highs.append(50) # Uma linha está em branco gerando conflito na plotagem.

# Faz a plotagem dos dados
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red')

# Formata o gráfico
plt.title("Daily high temperatures, July 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()
