class Site:
    def __init__(self):
        self.capacity_factor = 0.8   # Capacity Factor (%)

        # Demand Data
        self.annual_demand = 0.0    # Annual Energy Demand (kWh)
        
        # Ambient Data
        self.tmed_amb = []          # Average Ambient Temperature for the Year (°C)
        self.irrmed = []            # Average Irradiance for the Year (W/m²)
        self.wind_speed = []        # Average Wind Speed for the Year (m/s)