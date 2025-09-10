class Inverter:
    def __init__(self, pmp, vmp, imp, voc, isc, ef, icost):
        self.pmp = pmp              # Maximum Power (Pmp)
        self.vmp = vmp              # Maximum Voltage (Vmp)
        self.imp = imp              # Maximum Current (Imp)
        self.voc = voc              # Open Circuit Voltage (Voc)
        self.isc = isc              # Short-Circuit Current (Isc)
        self.ef = ef                # Efficiency (Ef)
        self.icost = icost          # Investment Cost ($/W)

    def inverter_perfomance_index(self):
        self.ipvi = self.ef / self.icost
        
        return self.ipvi
    
    def number_inverters(self, site):
        self.ni = site.annual_demand / self.pmp
        
        return self.ni