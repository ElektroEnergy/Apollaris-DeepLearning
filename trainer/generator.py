import numpy as np

# Random demand generator
def demand_generator(low=1200, high=150000):
    # Generate one number, rounded to the nearest 100
    demand = np.random.randint(low // 100, high // 100 + 1) * 100

    return demand

# Random irradiance generator
def irradiance_generator():
    rng = np.random.default_rng()
    
    irradiance = rng.uniform(600, 1500)
    
    return irradiance

# Random temperature generator
def temperature_generator():
    rng = np.random.default_rng()
    
    temperature = rng.uniform(20, 45)
    
    return temperature

# Random wind speed generator
def wind_speed_generator():
    rng = np.random.default_rng()
    
    wind_speed = rng.uniform(1, 25)
    
    return wind_speed