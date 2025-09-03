import numpy as np
    
def distancia_de_sombreamento(lat = None,sunN = None,sunrise = None): 
    ###########################################################################
    
    # Based on Optimal displacement of photovoltaic array’s rows using a novel
#shading model Nuria Novas Castellano, José Antonio Gázquez Parra, Juan
#Valls-Guirado, Francisco Manzano-Agugliaro
    
    # http://www.lusosol.com/fileiras.htm
    
    # Created by Gustavo Dill - april 2020
###########################################################################
# clc
# clear all
# sunrise=10; lat=22.9; b=1.665;
    lat = lat
    b = sunN(:,14) / 1000
    
    T = sunrise
    rad = np.pi / 180
    w = (12 - T) * 15
    beta = np.abs(lat)
    
    H = 360 - w
    dec = 23.45
    h = asind(np.sin(lat * rad) * np.sin(dec * rad) + np.cos(lat * rad) * np.cos(dec * rad) * np.cos(H * rad))
    d = b * np.sin(beta * rad) / np.tan(dec * rad)
    dmax = b * np.sin(beta * rad) / np.tan(h * rad)
    # #phi=0.006918-0.399912*cos(tau)+0.070257*sin(tau)-0.006758cos(2*tau)+0.000907sin(2*tau)-0.002697*cos(3*tau)+0.00148*sin(3*tau)
# alpha=asind(cos(phi*rad)*cos(lat*rad)*cos(w*rad)+sin(phi*rad)*sin(lat*rad))
# D=b*(cos(beta*rad)+sin(beta*rad)*cot(alpha*rad))
# d=D-b*cos(beta*rad)
    return d,dmax