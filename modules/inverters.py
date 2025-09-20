class Inverter:
    def __init__(self, pdc, nmmpts, pmp, vmp, imp, voc, isc, ef, icost):
        self.pdc = pdc              # DC Power Input (W)
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
    
    def power_required(self, site):
        power_required = site.annual_demand / self.ef * site.capacity_factor

        return power_required
    
    def number_inverters(self, power_required):
        self.ninv = power_required / self.pdc

        return self.ninv
    
    def max_strings_per_mppt(self, module):
        self.max_strings = self.imp / module.imp

        return self.max_strings

    def modules_per_string(self, module):
        self.mod_string = module.nmod / (self.ninv * self.nmmpts * self.max_strings)

        return self.mod_string