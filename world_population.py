import json
from country_codes import get_country_code
import pygal.maps.world
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS
# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # Constrói um dicionário com dados das populações
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population
    # Agrupa os países em três níveis populacionais
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop, in cc_populations.items():
        if pop < 10**7:
            cc_pops_1[cc] = pop
        elif pop < 10**9:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop
    # Vê quantos países estão em cada nível
    print(len(cc_pops_1))
    print(len(cc_pops_2))
    print(len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style = LCS)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
