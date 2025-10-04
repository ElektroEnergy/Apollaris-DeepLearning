import numpy as np

# Random demand generator
def demand_generator():
    rng = np.random.default_rng()
    
    radical = rng.integers(0, 10)
    multiplier = rng.integers(3, 7)   
    demand = radical * (10 ** multiplier)
    
    return demand

# Random irradiance generator
def irradiance_generator():
    rng = np.random.default_rng()
    
    irradiance = rng.uniform(100, 1000)
    
    return irradiance

# Random temperature generator
def temperature_generator():
    rng = np.random.default_rng()
    
    temperature = rng.uniform(-10, 40)
    
    return temperature

# Random wind speed generator
def wind_speed_generator():
    rng = np.random.default_rng()
    
    wind_speed = rng.uniform(0, 25)
    
    return wind_speed