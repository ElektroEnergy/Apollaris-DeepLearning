import numpy as np
    
def module_temperature(wind_speed = None,x_atemp = None,sunN = None,E = None,max_atemp = None,min_atemp = None): 
    
    #Calculation of the polycrystalline PV module
#temperature using a simple method of energy balance
#M. Mattei, G. Notton*, C. Cristofari, M. Muselli, P. Poggi
    
    Tr = 25
    E1 = 1200
    
    nr = sunN(:,16) / 100
    beta = np.abs(sunN(:,8) / 100)
    upv = 17.1 + np.multiply(5.7,wind_speed)
    upv_max = 17.1 + np.multiply(np.multiply(5.7,wind_speed),2)
    upv_min = 17.1 + np.multiply(np.multiply(5.7,wind_speed),0.1)
    for i in np.arange(1,len(beta)+1).reshape(-1):
        x_temp[i,1] = (np.multiply(upv,x_atemp) + np.multiply(E,(0.81 - nr(i) - (np.multiply(np.multiply(beta(i),nr(i)),Tr))))) / (upv - np.multiply(np.multiply(beta(i),nr(i)),E))
        max_temp[i,1] = (np.multiply(upv_min,max_atemp) + np.multiply(E1,(0.81 - nr(i) - (np.multiply(np.multiply(beta(i),nr(i)),Tr))))) / (upv_min - np.multiply(np.multiply(beta(i),nr(i)),E1))
        min_temp[i,1] = (np.multiply(upv_max,min_atemp) + np.multiply(0.1 * E,(0.81 - nr(i) - (np.multiply(np.multiply(beta(i),nr(i)),Tr))))) / (upv_max - np.multiply(np.multiply(beta(i),nr(i)),0.1) * E)
        nef[i,1] = nr(i) - np.multiply(beta(i),(x_temp(i,1) - Tr))
        i = i + 1
    
    #         for i=1:length(beta)
#     x_temp(i,1)=(upv.*x_atemp+E.*(0.81-nr(i)-(beta(i).*nr(i).*Tr)))/(upv-beta(i).*nr(i).*E);
#     max_temp(i,1)=(upv_min.*max_atemp+2*E.*(0.81-nr(i)-(beta(i).*nr(i).*Tr)))/(upv_min-beta(i).*nr(i).*2*E); # para maxima temperatura E=2*Emedio, wind=0,1*wind_speed
#     min_temp(i,1)=(upv_max.*min_atemp+0.1*E.*(0.81-nr(i)-(beta(i).*nr(i).*Tr)))/(upv_max-beta(i).*nr(i).*0.1*E);     # para minima temperatura E=10#Emedio, wind=2*wind_speed
#     nef(i,1)=nr(i)-beta(i).*(x_temp(i,1)-Tr);
#     i=i+1;
#     end
#     for i=1:length(beta)
#     x_temp(i,1)=((sunN(i,24)-20).*E/800)+x_atemp;
#     max_temp(i,1)=((sunN(i,24)-20).*(2.*E/800))+x_atemp; # para maxima temperatura E=2*Emedio, wind=0,1*wind_speed
#     min_temp(i,1)=((sunN(i,24)-20).*(0.1.*E/800))+x_atemp; # para minima temperatura E=10#Emedio, wind=2*wind_speed
#     nef(i,1)=nr(i)-beta(i).*(x_temp(i,1)-Tr);
#     i=i+1;
#     end
    return x_temp,max_temp,min_temp,nef