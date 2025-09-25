from site import Site
from inverters import Inverter
from modules import Module
import json

class System():
    def __init__(self):
        self.site = Site()
        self.inverters = json.load(open('data/inverters.json'))
        self.modules = json.load(open('data/modules.json'))

    # Decide the best configuration for the system
    def decision_making(self):
        for module in self.modules:
            PVModule = Module(module['pmp'], module['vmp'], module['imp'], module['voc'], module['isc'], module['tcoef_voc'], module['tcoef_vmp'], module['area'], module['icost'], module['ef'], module['ncel'], module['tol'], module['dur'], module['material'], module['tmax'], module['tmin'], module['tnm'], module['tier'], module['max_fuse'], self.site)
            
            # Make the corrections based on the site conditions
            PVModule.correct_voc_vmp_by_temp(self.site)
            PVModule.correct_imp_isc_pmp_by_irr(self.site)
            PVModule.correct_imp_isc_pmp_by_shading(self.site)
                
            for inverter in self.inverters:
                PVInverter = Inverter(inverter['pdc'], inverter['nmmpts'], inverter['pmp'], inverter['vmp'], inverter['imp'], inverter['voc'], inverter['isc'], inverter['ef'], inverter['icost'])

                # Calculate the estimated power required
                power_required = PVInverter.power_required(self.site)

                # Check if the inverter power is compatible with the power required using the rule of 85% to 130% of the power required
                if PVInverter.pdc < (power_required * 0.85) or PVInverter.pdc > (power_required * 1.30):
                    continue # Pass to the next interation

                # Calculate the number of inverters needed
                PVInverter.number_inverters(power_required)

                # Calculate the number of modules needed
                PVModule.number_modules(power_required)

                # Calculate the strings
                max_strings = PVInverter.max_strings_per_mppt(Module)
                modules_per_string = PVInverter.modules_per_string(Module)

                # Calculate the performance index of the module
                module_perfomance_index = PVModule.module_perfomance_index()
                total_module_perfomance_index = module_perfomance_index * PVModule.nmod

                # Calculate the performance index of the inverter
                inverter_perfomance_index = PVInverter.inverter_perfomance_index(Module)
                total_inverter_perfomance_index = inverter_perfomance_index * PVInverter.ninv

                # Calculate the total index of the system
                system_perfomance_index = total_module_perfomance_index * total_inverter_perfomance_index
                