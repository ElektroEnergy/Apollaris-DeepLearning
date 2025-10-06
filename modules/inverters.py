import math

class Inverter:
    def __init__(self, pdc, nmmpts, vmpmax, vmpmin, imp, isc, ef, icost):
        self.pdc = pdc              # DC Power Input (W)
        self.nmmpts = nmmpts        # Number of MPPTs

        self.vmpmax = vmpmax           # Maximum Voltage per MPPT (VmpMax)
        self.vmpmin = vmpmin           # Minimum Voltage per MPPT (VmpMin)
        self.imp = imp              # Maximum Current per MPPT (Imp)

        self.isc = isc              # Maximum Short-Circuit Current per MPPT (Isc)
    
        self.ef = ef                # Efficiency (Ef)
        self.icost = icost          # Investment Cost ($/W)
        self.ni = None              # Number of inverters required

    def inverter_perfomance_index(self):
        self.ipvi = (1 / ((self.ef / 100) * (self.imp * self.nmmpts) * (self.vmpmax - self.vmpmin) * self.icost))
        
        return self.ipvi
    
    def power_required(self, site):
        power_required = math.ceil(site.annual_demand / (self.ef / 100) * site.capacity_factor)

        return power_required
    
    def number_inverters(self, power_required):
        self.ninv = math.ceil(power_required / self.pdc)

        return self.ninv
    
    def max_strings_per_mppt(self, module):
        self.max_strings = math.ceil(self.imp / module.imp)

        return self.max_strings

    def modules_per_string(self, module):
        # DEBUG MODULE
        # print(module.nmod, self.ninv, self.nmmpts, self.max_strings)
        self.mod_string = math.ceil(module.nmod / (self.ninv * self.nmmpts * self.max_strings))

        if self.vmpmin <= (module.nmod * module.voc) <= self.vmpmax:
            return None 

        return self.mod_string