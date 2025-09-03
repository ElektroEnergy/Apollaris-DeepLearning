import numpy as np
    
def irradiation(lat = None,lon = None,alt = None,x_atemp = None,FS = None,proj = None,stil = None,sazi = None): 
    # Data obtained from http://www.cresesb.cepel.br/index.php?section=sundata&#sundata
#http://labren.ccst.inpe.br/atlas_2017-en.html#mod
    
    incl,ori = inclination(lat,lon,alt,x_atemp,stil,sazi)
    # if proj==1
# irrad = xlsread('brazil_solar_tilted_10km.xlsx');
# elseif proj==2
# irrad = xlsread('brazil_solar_direct_10km.xlsx');
# elseif proj==3
# irrad = xlsread('brazil_solar_diffuse_10km.xlsx');
# elseif proj==4
    irrad = xlsread('brazil_solar_global_10km.xlsx')
    # end
    nl,nc = irrad.shape
    pos_lat = []
    for i in np.arange(1,nl+1).reshape(-1):
        if ((irrad(i,2) <= lat + 0.1) and (irrad(i,2) >= lat - 0.1)):
            pos_lat = np.array([i,pos_lat])
        i = i + 1
    
    pos = []
    l = len(pos_lat)
    for i in np.arange(1,l+1).reshape(-1):
        if irrad(pos_lat(i),1) == lon:
            pos = np.array([i,pos])
        else:
            if ((irrad(pos_lat(i),1) < lon + 0.1) and (irrad(pos_lat(i),1) > lon - 0.1)):
                pos = np.array([i,pos])
        i = i + 1
    
    #disp('LONGITUDE AND LATITUDE FOUNDED AND THEIR IRRADIATIONS BY MONTH')
    founded_solutions = irrad(pos_lat(pos),np.arange(1,14+1))
    s = len(pos)
    for k in np.arange(1,s+1).reshape(-1):
        h[k] = sum(irrad(pos_lat(pos(k)),np.arange(3,14+1)))
    
    hh,p = np.amin(h)
    sol = irrad(pos_lat(pos(p)),np.arange(1,14+1))
    #disp('Hours of sun per day January to December')
    Ns = irrad(pos_lat(pos(p)),np.arange(3,14+1))
    if proj == 2:
        y = np.multiply((irrad1(pos_lat(pos(p)),np.arange(4,15+1)) / 1000),FS)
    else:
        y = np.multiply(irrad(pos_lat(pos(p)),np.arange(3,14+1)),FS)
    
    return sol,y,incl,ori