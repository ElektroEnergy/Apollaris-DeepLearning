class Site:
    def __init__(self):
        self.capacity_factor = 0.8   # Capacity Factor (%)
        
        # Montly Data
        self.tmed_amb = []          # Average Ambient Temperature for the Months (°C)
        self.irr = []               # Irradiance for the Months (W/m²)
        self.wind_speed = []        # Wind Speed for the Months (m/s)