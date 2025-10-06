class Site:
    def __init__(self, seeds):
        self.capacity_factor = 0.8   # Capacity Factor (%)

        # Demand Data
        self.annual_demand = seeds[0]    # Annual Energy Demand (kWh)

        self.shading_factor = 1
        
        # Ambient Data
        self.tmed_amb = seeds[2]          # Average Ambient Temperature for the Year (°C)
        self.irrmed = seeds[1]            # Average Irradiance for the Year (W/m²)
        self.wind_speed = seeds[3]        # Average Wind Speed for the Year (m/s)