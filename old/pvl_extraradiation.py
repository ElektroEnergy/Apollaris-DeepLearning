import numpy as np
    
def pvl_extraradiation(doy = None): 
    # PVL_EXTRARADIATION Determine extraterrestrial radiation from day of year
    
    # Syntax
#   Ea = pvl_extraradiation(doy)
    
    # Description
#   Determine the amount of extraterrestrial solar radiation.
    
    #   Output Ea is the extraterrestrial radiation present in watts per square meter
#   on a surface which is normal to the sun. Ea is of the same size as the
#   input doy.
    
    #   Input doy is an array specifying the day of year. Valid values are >=1 and <367.
    
    
    # Source
#   http://solardat.uoregon.edu/SolarRadiationBasics.html, Eqs. SR1 and SR2
#   SR1 	   	Partridge, G. W. and Platt, C. M. R. 1976. Radiative Processes in Meteorology and Climatology.
#   SR2 	   	Duffie, J. A. and Beckman, W. A. 1991. Solar Engineering of Thermal Processes, 2nd edn. J. Wiley and Sons, New York.
    
    # See also PVL_DAYOFYEAR PVL_DISC
    
    p = inputParser
    p.addRequired('doy',lambda x = None: np.all(np.logical_and(isnumeric(x),x) >= np.logical_and(1,x) < 367))
    p.parse(doy)
    B = 2 * np.pi * doy / 365
    Rfact2 = 1.00011 + np.multiply(0.034221,np.cos(B)) + np.multiply(0.00128,np.sin(B)) + np.multiply(0.000719,np.cos(2 * B)) + np.multiply(7.7e-05,np.sin(2 * B))
    Ea = 1367 * Rfact2
    return Ea
    
    return Ea