from learning.generator import demand_generator, irradiance_generator, temperature_generator, wind_speed_generator
from modules.decision import System
from modules.site import Site
from utils.io import Console
import pandas as pd

def seeds(size):
    seeds = []
    
    for i in range(size):
        seed = []
        seed.append(demand_generator())         # Demand
        seed.append(irradiance_generator())     # Irradiance
        seed.append(temperature_generator())    # Temperature
        seed.append(wind_speed_generator())     # Wind Speed    
        
        seeds.append(seed)
        
    return seeds

def factory(seeds, size):
    selections = []
    data = []
    
    for i in range(size):
        site = Site(seeds[i])
        system = System(site)
        
        selection = system.decision_making()
        if selection == 0:
            continue
        
        selections.append([selection['module'], selection['inverter'], selection['power_required'], selection['nmod'], selection['ninv'], selection['total_ipmd'], selection['total_ipinv'], selection['ipsys']])
        
        
        data.append(selection)

    df = pd.DataFrame(data)
    df.to_csv('learning/debug/dados.csv')
    Console.send_debug('Data from factory saved to learning/debug/dados.csv')
    return selections    

# Debug
# factory(seeds(100), 100)
    
