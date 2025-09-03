import os
import numpy as np
    
def sol_por_dia(lon = None,lat = None): 
    ###########################################################################
    
    # https://www.inf.ufrgs.br/~cabral/Nascer_Por_Sol.html
    
    # Created by: Gustavo Dill - April 2020                                   #
    
    # T = tempo de duraçao do dia
# phi = latitude do local
# theta = declinaçao da terra
# n = dia sequencial do ano
# A seguir, tomar o T, dividí-lo por 2. Agora subtrai-se do meio-dia o    #
# valor de T, seguido da soma de T ao meio-dia. Os 2 horários obtidos são #
# respectivamente o nascer e pôr do sol para a cidade em questão.         #
# Para fazer a correção do fuso horário, usa-se uma regra de três. Uma    #
# hora corresponde a 15°. Sabendo-se a longitude do local, calcula-se a   #
# diferença entre esta e a longitude do meridiano do fuso. Entra-se na    #
# regra de 3 para saber quantos minutos de relógio, corresponde a         #
# diferença em graus obtida.                                              #
# Aplica-se a referida correção aos horários inicialmente encontrados. Se #
# a cidade estiver à esquerda do meridiano do fuso, há um atraso, ou seja,#
# deve-se somar os minutos calculados, se for à direita subtrai-se.       #
###########################################################################
    
    mon = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    # lat=-22.9; lon=-43.1;
    phi = lat
    rad = np.pi / 180
    fuso = - 45
    dif = np.abs(lon - fuso)
    xmin = (np.multiply(dif,60)) / 15
    #n=130 # equivalente a 29 de abril
    a = 1
    b = 0
    i = 1
    for j in np.arange(1,len(mon)+1).reshape(-1):
        nb = mon(j)
        n = nb + b
        for i in np.arange(i,n+1).reshape(-1):
            theta = np.multiply(23.45,np.sin(np.multiply(np.multiply((360 / 365),(284 + i)),rad)))
            T[a,j] = np.multiply((2 / 15),acosd(np.multiply(- np.tan(np.multiply(phi,rad)),np.tan(np.multiply(theta,rad)))))
            # correcao da longitude
            T[a,j] = T(a,j) + xmin / 60
            a = a + 1
            i = i + 1
        Tm[j] = mean(T(np.arange(1,mon(j)+1),j))
        sunrise[j] = 12 - (Tm(j) / 2)
        sunset[j] = 12 + (Tm(j) / 2)
        a = 1
        b = i
    
    #Td=(2/15).*acosd(0.4357119.*tan(23.45.*sin((72/73).*(284+n).*rad).*rad))
#delta=Tm./floor(Tm)
    th = np.amin(Tm) / 2
    sunrise_min = 12 - th
    sunset_min = 12 + th
    delta = 0
    for j in np.arange(1,12+1).reshape(-1):
        for i in np.arange(1,np.ceil(Tm(j))+1).reshape(-1):
            hora[i,j] = sunrise(j) + delta
            delta = (Tm(j) / int(np.floor(Tm(j))) * i)
        i = 1
        delta = 0
    
    hora[hora == 0] = nan
    return Tm,T,sunrise_min,sunset_min,hora