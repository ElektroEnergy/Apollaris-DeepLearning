class Inverter:
    def __init__(self):
        self.pmp = 0.0              # Maximum Power (Pmp)
        self.vmp = 0.0              # Maximum Voltage (Vmp)
        self.imp = 0.0              # Maximum Current (Imp)
        self.voc = 0.0              # Open Circuit Voltage (Voc)
        self.isc = 0.0              # Short-Circuit Current (Isc)
        self.ef = 0.0               # Efficiency (Ef)
        self.icost = 0.0            # Investment Cost ($/W)

    def inverter_perfomance_index(self):
        self.ipvi = self.ef / self.icost
        
        return self.ipvi
    
    def power_required_annual(self, site):
        # Constants
        istc = 1000
        
        self.power_required_annual = (site.annual_demand * istc) / (self.ef * site.capacity_factor)
        
        return self.power_required_annual
    
    def number_inverters(self):
        self.ni = power_required_annual / self.pmp
        
        return self.ni