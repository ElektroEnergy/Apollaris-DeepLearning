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
            
            # Calculate the performance index of the module
            module_perfomance_index = Module.module_perfomance_index()
            total_module_perfomance_index = module_perfomance_index * Module.nmod
                
            for inverter in self.inverters:
                Inverter = Inverter(inverter['pmp'], inverter['vmp'], inverter['imp'], inverter['voc'], inverter['isc'], inverter['ef'], inverter['icost'])
                
                # Calculate the performance index of the inverter
                inverter_perfomance_index = Inverter.inverter_perfomance_index(Module)
                total_inverter_perfomance_index = inverter_perfomance_index * Inverter.ninv
                
                # Calculate the total index of the system
                system_perfomance_index = total_module_perfomance_index * total_inverter_perfomance_index
                