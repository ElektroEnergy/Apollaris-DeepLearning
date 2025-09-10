def compute_irradiace(site):
    return 'WIP'

def estimate_cell_temperature(tmed_amb, tnm, trmtabs, ef, irr, wind_speed):
    # Constants
    irr_noct = 800
    t_ambnoct = 20
    
    tnm_corr = tmed_amb + (irr / irr_noct) * (9.5 / (5.7 + (3.8 * wind_speed))) * (tnm - t_ambnoct) * (1 - (ef / trmtabs))
    return tnm_corr