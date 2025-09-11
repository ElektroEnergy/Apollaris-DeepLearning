class Inverter:
    def __init__(self, nmmpts, pmp, vmp, imp, voc, isc, ef, icost):
        self.nmmpts = nmmpts        # Number of MPPTs
        self.pmp = pmp              # Maximum Power per MPPT (Pmp)
        self.vmp = vmp              # Maximum Voltage per MPPT (Vmp)
        self.imp = imp              # Maximum Current per MPPT (Imp)
        self.voc = voc              # Open Circuit Voltage per MPPT (Voc)
        self.isc = isc              # Short-Circuit Current per MPPT(Isc)
        self.ef = ef                # Efficiency (Ef)
        self.icost = icost          # Investment Cost ($/W)
        self.ni = None              # Number of inverters required

    def inverter_perfomance_index(self):
        self.ipvi = (1 / (self.ef * (self.imp + self.isc) * (self.voc - self.vmp) * self.icost))
        
        return self.ipvi
    
    def number_inverters(self, site):
        self.ni = site.annual_demand / self.pmp
        
        return self.ni