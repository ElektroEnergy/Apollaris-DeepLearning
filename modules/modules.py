from irradiance import estimate_cell_temperature

class Module:
    def __init__(self, voc, isc, vmp, imp, pmp, vmax_sys, tcoef_voc, tcoef_vmp, tcoef_isc, weight, depth, width, length, area, icost, ef, ncel, tol, dur, material, tmax, tmin, tnm, tier, max_fuse, site):
        self.voc = voc                  # Open Circuit Voltage (Voc)
        self.isc = isc                  # Short-Circuit Current (Isc)
        self.vmp = vmp                  # Maximum Voltage at 25°C (Vmp)
        self.imp = imp                  # Maximum Current at 25°C (Imp)
        self.pmp = pmp                  # Maximum Power at 25°C (Pmp)
        self.vmax_sys = vmax_sys        # Maximum System Voltage
        self.tcoef_voc = tcoef_voc      # Open Circuit Voltage Temperature Coefficient (V/°C)
        self.tcoef_vmp = tcoef_vmp      # Output Temperature Coefficient (V/°C)
        self.tcoef_isc = tcoef_isc      # Short Circuit Current Temperature Coefficient (%/°C)
        self.weight = weight            # Weight (kg)
        self.depth = depth              # Depth (mm)
        self.width = width              # Width (mm)
        self.length = length            # Length (mm)
        self.area = area                # Area (m²)
        self.icost = icost              # Index used to optimize and select the PV
        self.ef = ef                    # Efficiency (%)
        self.ncel = ncel                # Number of cells per PV
        self.tol = tol                  # Tolerance of the capacity (%)
        self.dur = dur                  # Durability (years)
        self.material = material        # Material of the cell (1: mono, 2: poly, 3: thin-film, 4: amorphous)
        self.tmax = tmax                # Minimum operational temperature
        self.tmin = tmin                # Maximum operational temperature
        self.tnm = tnm                  # Nominal Operating Cell Temperature
        self.tier = tier                # Certifications (IEC-61730, IEC-61215, etc.)
        self.max_fuse = max_fuse        # Max. series fuse rating (A)
        
        # Corrected values
        self.voc_corr = None            # Corrected Open Circuit Voltage (Voc)
        self.vmp_corr = None            # Corrected Maximum Voltage (Vmp)
        self.imp_corr = None            # Corrected Maximum Current (Imp)
        self.isc_corr = None            # Corrected Short-Circuit Current (Isc)
        self.pmp_corr = None            # Corrected Maximum Power (Pmp)
        
        # Corrected Nominal Operating Cell Temperature for the Months
        self.tnm_corr = estimate_cell_temperature(site.tmed_amb, self.tnm, 0.95, self.ef, site.irrmed, site.wind_speed)
    
    def correct_voc_vmp_by_temp(self):
        # Constants
        t_stc = 25
    
        self.voc_corr = self.voc * (1 + self.tcoef_voc * (self.tnm_corr - t_stc))
        self.vmp_corr = self.vmp * (1 + self.tcoef_vmp * (self.tnm_corr - t_stc))
        
        return self.voc_corr, self.vmp_corr
    
    def correct_imp_isc_pmp_by_irr(self, site):
        # Constants 
        g_stc = 1000

        self.imp_corr = self.imp * (site.irrmed / g_stc)
        self.isc_corr = self.isc * (site.irrmed / g_stc)
        self.pmp_corr = self.pmp * (site.irrmed / g_stc)

    def correct_imp_isc_pmp_by_shading(self, site):
        # Constants 
        k = 1.5     # Non-linear factor

        self.imp_corr = self.imp_corr * (1 - site.shading_factor)**k
        self.isc_corr = self.isc_corr * (1 - site.shading_factor)**k
        self.pmp_corr = self.pmp_corr * (1 - site.shading_factor)**k
    
    # Liable of correction to implement Voc and Isc
    def modules_in_string_and_mppt(self, inverter):
        # Calculate number of modules in a string (series)
        n_string = int(inverter.vmp / self.vmp_corr)
        # Calculate number of parallel strings per MPPT
        n_mppt = int(inverter.imp / self.imp_corr)
        
        return n_string, n_mppt

    def module_perfomance_index(self):
        self.ipvn = (self.pmp * self.ef) / (self.area * self.icost)
        
        return self.ipvn