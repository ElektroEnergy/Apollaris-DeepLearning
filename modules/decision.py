from site import Site
import json

class System():
    def __init__(self):
        self.site = Site()
        self.inverters = json.load(open('data/inverters.json'))
        self.modules = json.load(open('data/modules.json'))

    def decision_making(self):
        for module in self.modules:
            Module = Module(module['pmp'], module['vmp'], module['imp'], module['voc'], module['isc'], module['tcoef_voc'], module['tcoef_vmp'], module['area'], module['icost'], module['ef'], module['ncel'], module['tol'], module['dur'], module['material'], module['tmax'], module['tmin'], module['tnm'], module['tier'], module['max_fuse'], self.site)
            
            # Make the corrections based on the site conditions
            Module.correct_voc_vmp_by_temp(self.site)
            Module.correct_imp_isc_pmp_by_irr(self.site)
            Module.correct_imp_isc_pmp_by_shading(self.site)
                
            for inverter in self.inverters:
                Inverter = Inverter(inverter['pdc'], inverter['nmmpts'], inverter['pmp'], inverter['vmp'], inverter['imp'], inverter['voc'], inverter['isc'], inverter['ef'], inverter['icost'])

                # Calculate the estimated power required
                power_required = Inverter.power_required(self.site)

                # Check if the inverter power is compatible with the power required using the rule of 85% to 130% of the power required
                if Inverter.pdc < (power_required * 0.85) or Inverter.pdc > (power_required * 1.30):
                    continue # Pass to the next interation

                # Calculate the number of inverters needed
                Inverter.number_inverters(power_required)

                # Calculate the number of modules needed
                Module.number_modules(power_required)

                # Calculate the strings
                max_strings = Inverter.max_strings_per_mppt(Module)
                modules_per_string = Inverter.modules_per_string(Module)

                # Calculate the performance index of the module
                module_perfomance_index = Module.module_perfomance_index()
                total_module_perfomance_index = module_perfomance_index * Module.nmod

                # Calculate the performance index of the inverter
                inverter_perfomance_index = Inverter.inverter_perfomance_index(Module)
                total_inverter_perfomance_index = inverter_perfomance_index * Inverter.ninv

                # Calculate the total index of the system
                system_perfomance_index = total_module_perfomance_index * total_inverter_perfomance_index
                