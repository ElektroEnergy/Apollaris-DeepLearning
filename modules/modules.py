from irradiance import estimate_cell_temperature

class Module:
    def __init__(self, site):
        self.voc = 0.0              # Open Circuit Voltage (Voc)
        self.isc = 0.0              # Short-Circuit Current (Isc)
        self.vmp = 0.0              # Maximum Voltage at 25°C (Vmp)
        self.imp = 0.0              # Maximum Current at 25°C (Imp)
        self.pmp = 0.0              # Maximum Power at 25°C (Pmp)
        self.vmax_sys = 0.0         # Maximum System Voltage
        self.tcoef_voc = 0.0        # Open Circuit Voltage Temperature Coefficient (V/°C)
        self.tcoef_vmp = 0.0        # Output Temperature Coefficient (V/°C)
        self.tcoef_isc = 0.0        # Short Circuit Current Temperature Coefficient (%/°C)
        self.weight = 0.0           # Weight (kg)
        self.depth = 0.0            # Depth (mm)
        self.width = 0.0            # Width (mm)
        self.length = 0.0           # Length (mm)
        self.area = 0.0             # Area (m²)
        self.icost = 0.0            # Index used to optimize and select the PV
        self.ef = 0.0               # Efficiency (%)
        self.ncel = 0               # Number of cells per PV
        self.tol = 0.0              # Tolerance of the capacity (%)
        self.dur = 0                # Durability (years)
        self.material = 0           # Material of the cell (1: mono, 2: poly, 3: thin-film, 4: amorphous)
        self.tmax = 0.0             # Minimum operational temperature
        self.tmin = 0.0             # Maximum operational temperature
        self.tnm = 0.0              # Nominal Operating Cell Temperature
        self.tier = ""              # Certifications (IEC-61730, IEC-61215, etc.)
        self.max_fuse = 0.0         # Max. series fuse rating
        
        # Corrected values
        self.voc_corr = None         # Corrected Open Circuit Voltage (Voc)
        self.vmp_corr = None         # Corrected Maximum Voltage (Vmp)
        self.imp_corr = None         # Corrected Maximum Current (Imp)
        self.isc_corr = None         # Corrected Short-Circuit Current (Isc)
        
        # Corrected Nominal Operating Cell Temperature for the Months
        self.tnm_corr = estimate_cell_temperature(site.tmed_amb, self.tnm, 0.95, self.ef, site.irr, site.wind_speed)
    
    def correct_voc_vmp_by_temp(self):
        # Constants
        t_stc = 25
    
        for m in range(12):
            self.voc_corr[m] = self.voc * (1 + self.tcoef_voc * (self.tnm_corr[m] - t_stc))
            self.vmp_corr[m] = self.vmp * (1 + self.tcoef_vmp * (self.tnm_corr[m] - t_stc))
        
        return self.voc_corr, self.vmp_corr
    
    def number_modules(self, inverter, site):
        self.nm[inverter] = inverter.power_required_annual(site) / self.pmp
        
        return self.nm
    

    def module_perfomance_index(self):
        self.ipvn = (self.pmp * self.ef) / (self.area * self.icost)
        
        return self.ipvn