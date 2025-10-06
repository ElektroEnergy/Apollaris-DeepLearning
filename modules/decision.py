from modules.site import Site
from modules.inverters import Inverter
from modules.modules import Module

from utils.io import Console
import json

class System():
    def __init__(self, site):
        self.site = site
        with open('data/inverters.json', 'r') as f:
            data = json.load(f)

        self.inverters = data["inverters"]
        
        with open('data/modules.json', 'r') as f:
            data = json.load(f)

        self.modules = data["modules"]

    # Decide the best configuration for the system
    def decision_making(self):
        combinations = []

        for module in self.modules:
            PVModule = Module(module['voc'], module['isc'], module['vmp'], module['imp'], module['pmp'], module['vmax_sys'], module['tcoef_voc'], module['tcoef_vmp'], module['tcoef_isc'], module['weight'], module['depth'], module['width'], module['length'], module['area'], module['icost'], module['ef'], module['ncel'], module['tol'], module['dur'], module['material'], module['tmax'], module['tmin'], module['tnm'], module['tier'], module['max_fuse'], self.site)
            
            # Make the corrections based on the site conditions
            PVModule.correct_voc_vmp_by_temp(self.site)
            PVModule.correct_imp_isc_pmp_by_irr(self.site)
            # PVModule.correct_imp_isc_pmp_by_shading(self.site)
                
            for inverter in self.inverters:
                PVInverter = Inverter(inverter['pdc'], inverter['nmmpts'], inverter['vmpmax'], inverter['vmpmin'], inverter['imp'], inverter['isc'], inverter['ef'], inverter['icost'])

                # Calculate the estimated power required
                power_required = PVInverter.power_required(self.site)

                # Check if the inverter power is compatible with the power required using the rule of 85% to 130% of the power required
                # if PVInverter.pdc < (power_required * 0.85) or PVInverter.pdc > (power_required * 1.30):
                #    continue # Pass to the next interation

                # Calculate the number of inverters needed
                PVInverter.number_inverters(power_required)

                # Calculate the number of modules needed
                PVModule.number_modules(power_required)

                # Calculate the strings
                max_strings = PVInverter.max_strings_per_mppt(PVModule)
                modules_per_string = PVInverter.modules_per_string(PVModule)

                # Electric restriction of modules per string
                if not modules_per_string:
                    continue

                # Calculate the performance index of the module
                module_perfomance_index = PVModule.module_perfomance_index()
                total_module_perfomance_index = module_perfomance_index * PVModule.nmod

                # Calculate the performance index of the inverter
                inverter_perfomance_index = PVInverter.inverter_perfomance_index()
                total_inverter_perfomance_index = inverter_perfomance_index * PVInverter.ninv

                # Calculate the total index of the system
                system_perfomance_index = total_module_perfomance_index + total_inverter_perfomance_index
                
                # Save the combination
                combination = {
                    'module': module['id'],
                    'inverter': inverter['id'],
                    'power_required': power_required,
                    'nmod': PVModule.nmod,
                    'ninv': PVInverter.ninv,
                    'modules_per_string': modules_per_string,
                    'max_strings': max_strings,
                    'total_ipmd': total_module_perfomance_index,
                    'total_ipinv': total_inverter_perfomance_index,
                    'ipsys': system_perfomance_index
                }
                combinations.append(combination)

        # Return the best combination
        if not len(combinations):
            Console.send_warn(f'Unable to select a configuration for demand: {self.site.annual_demand}W, maybe you dont have enough data?')
            return {
                    'module': -1,
                    'inverter': -1,
                    'power_required': -1,
                    'nmod': -1,
                    'ninv': -1,
                    'modules_per_string': -1,
                    'max_strings': -1,
                    'total_ipmd': -1,
                    'total_ipinv': -1,
                    'ipsys': -1
                }
        else:
            return max(combinations, key=lambda x: x['ipsys'])
        
# Message from author Nicolas Fernandes
# I dedicate this code for Ana Sophia Dutra, I love you honey 💗