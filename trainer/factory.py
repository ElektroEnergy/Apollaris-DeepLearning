from generator import demand_generator, irradiance_generator, temperature_generator, wind_speed_generator
from modules.decision import System
from modules.site import Site

def seeds(size):
    seeds = []
    
    for i in range(size):
        seed = []
        seed.append(demand_generator())         # Demand
        seed.append(irradiance_generator())     # Irradiance
        seed.append(temperature_generator())    # Temperature
        seed.append(0)                          # Shadding Factor
        seed.append(wind_speed_generator())     # Wind Speed    
        
        seeds.append(seed)
        
    return seeds

def factory(seeds, size):
    selections = []
    
    for i in range(size):
        site = Site(seeds[i])
        system = System(site)
        
        selection = system.decision_making()
        
        selections.append([selection['module'], selection['inverter'], selection['power_required'], selection['nmod'], selection['ninv'], selection['total_ipmd'], selection['total_ipinv'], selection['ipsys']])
    
    return selections    
    