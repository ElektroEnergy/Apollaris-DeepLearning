import numpy as np
    
def inclination(lat = None,lon = None,alt = None,x_atemp = None,stil = None,sazi = None): 
    # clc
# clear all
    
    #ESTIMATIVA DA IRRADIAÇÃO TOTAL SOBRE UMA SUPERFÍCIE INCLINADA
#A PARTIR DA IRRADIAÇÃO GLOBAL NA HORIZONTAL
#José Scolar,1
# Dinival Martins,2
# João Francisco Escobedo3
    
    #https://pvpmc.sandia.gov/modeling-steps/1-weather-design-inputs/array-orientation/fixed-tilt/
# References
#   Grover Hughes' class and related class materials on Engineering
#   Astronomy at Sandia National Laboratories, 1985.
    
    # See also PVL_MAKETIMESTRUCT PVL_MAKELOCATIONSTRUCT PVL_ALT2PRES
#          PVL_GETAOI PVL_SPA
    
    #HB direct irradiation
#HC diffuse irradiation
#HR reflected irradiation
#H média mensal de irradiação global
#Hd média mensal de irradiação difusa
# Rb razao entre a média mensal direta de irradiação em uma superficie inclinada e horizontal
# Rd razao entre a média mensal difusa de irradiação em uma superficie inclinada e horizontal
# z é o angulo azimutal
# beta e o angulo de inclinacao do modulo
# theta e a latitude
# phi e a declinacao
# ws e a hora angular do por do sol
# ws' e a hora angular do por do sol na superficie inclinada
# n e o dia medio de cada mes
    
    # beta deve ficar entre -20 <= lat <= +20, pode fazer passos de 1grau p
# achar o melhor beta. Beta náo pode ser inferior a 10 ou 15 graus para
# evitar sujeira que pode bloquear 20# de irradiacao
    
    # observar tambem a orientacao do telhado. telhado no brasil com face norte
# tem uma perda de irradiacao na ordem de 3 a 8#, ja inclinacao a oeste
# tem uma perda de irradiacao na ordem de 12 a 20#, face sul náo compensa,
# somente para cidades acima da linha do equador.
    
    #lat=-22.9; lon=-43.1; #Rio de Janeiro
#altitude=20;   #altitud RIO
# lat=-7.23; lon=-35.8; #Campina Grande
# altitude=551;   #altitud Campina Grande
# lat=-30.02; lon=-51.22; #Campina Grande
# alt=22;   #altitud Campina Grande
    
    Delta = 20
    Dai = np.abs(np.abs(np.round(lat)) - Delta)
    if (Dai < 10) or (np.abs(np.round(lat)) < 10):
        surftilt = 10
    else:
        surftilt = Dai
    
    Daf = np.abs(np.round(lat)) + Delta
    if Daf > 80:
        final = 80
    else:
        final = Daf
    
    dif = final - surftilt
    if (np.isnan(sazi) == 1) and (np.isnan(stil) == 1):
        surfAz = 0
        pro = 3
    else:
        if (np.isnan(sazi) == 0) and (np.isnan(stil) == 1):
            surfAz = sazi
            pro = 2
        else:
            if (np.isnan(sazi) == 0) and (np.isnan(stil) == 0):
                surfAz = sazi
                surftilt = stil
                pro = 1
    
    #Solar time per month
    Tm,Tx,sunrise_min,sunset_min,hora = sol_por_dia(lon,lat)
    #wind_speed = 3.98;
    ro = 0.2
    
    pressure = pvl_alt2pres(alt)
    temperature = x_atemp
    Rad2Deg = 180 / np.pi
    Deg2Rad = np.pi / 180
    Abber = 20 / 3600
    LatR = lat * Deg2Rad
    #    jan fev mar apr mai jun jul ago set out nov dez
    mon = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    # Hg = [5.96          6.10          5.31          4.69          3.70          3.44          3.47          4.32          4.59          5.33          5.60          5.83];
# Ht = [5.40          5.92          5.77          5.44          4.79          4.58          4.36          5.24          4.99          5.43          5.31          5.22];
# Hb = [6.86          4.66          4.74          5.59          4.67          4.43          3.92          4.75          4.44          5.73          4.42          6.08];
# Hd = [2.39          2.23          1.97          1.64          1.41          1.14          1.13          1.28          1.78          2.02          2.39          2.46];
    
    # calculating day mean per month
    sumM = 0
    for i in np.arange(1,12+1).reshape(-1):
        n[i] = int(np.floor(mon(1,i) / 2)) + sumM
        sumM = sum(mon(np.arange(1,i+1)))
        # declination angle
        dec[i] = np.multiply(23.45,np.sin(np.multiply((360.0 * (284 + n(i)) / 365),Deg2Rad)))
        DecR[i] = np.multiply(dec(i),Deg2Rad)
        for j in np.arange(np.arange(1,len(hora(,,1))+1)):
            #Angle time per month
            HrAngle[j,i] = (15.0 * hora(j,i)) - 180
            HrAngleR[j,i] = np.multiply(Deg2Rad,HrAngle(j,i))
            HrAngle[j,i] = HrAngle(j,i) - (np.multiply(np.multiply(360,np.sign(HrAngle(j,i))),(np.abs(HrAngle(j,i)) > 180)))
            #Azimuth angle
            SunAz[j,i] = np.multiply(Rad2Deg,atan2(- 1 * np.sin(HrAngleR(j,i)),np.multiply(np.cos(LatR),np.tan(DecR(i))) - np.multiply(np.sin(LatR),np.cos(HrAngleR(j,i)))))
            SunAz[j,i] = SunAz(j,i) + (SunAz(j,i) < 0) * 360
            #Elevation angle
            SunEl[j,i] = asind(np.multiply(np.multiply(np.cos(LatR),np.cos(DecR(i))),np.cos(HrAngleR(j,i))) + np.multiply(np.sin(LatR),np.sin(DecR(i))))
            # Calculate the refraction of the sun until the actual center of the sun is
# 1 degree below the horizon.
            TanEl[j,i] = np.tan(Deg2Rad * SunEl(j,i))
            Refract[j,i] = np.zeros((len(SunEl(j,i)),1)) + (np.multiply(and_(SunEl(j,i) > 5,SunEl(j,i) <= 85),(58.1 / TanEl(j,i) - 0.07 / (TanEl(j,i) ** 3) + 8.6e-05 / (TanEl(j,i) ** 5)))) + (np.multiply(and_(SunEl(j,i) > - 0.575,SunEl(j,i) <= 5),(np.multiply(SunEl(j,i),(- 518.2 + np.multiply(SunEl(j,i),(103.4 + np.multiply(SunEl(j,i),(- 12.79 + np.multiply(SunEl(j,i),0.711))))))) + 1735))) + (np.multiply(and_(SunEl(j,i) > - 1,SunEl(j,i) <= - 0.575),((- 20.774 / TanEl(j,i)))))
            Refract[j,i] = np.multiply(np.multiply(Refract(j,i),(283 / (273 + temperature))),pressure) / 101325 / 3600
            # Generate apparent sun elevation including refraction
            sunElR[j,i] = SunEl(j,i) + Refract(j,i)
            sunZen[j,i] = (90 - sunElR(j,i))
        i = i + 1
    
    sunZen[sunZen > 88.8] = nan
    # Air mass calculation
    AMaR = np.multiply((1.0 / (np.cos(np.pi/180*sunZen) + np.multiply(0.50572,((6.07995 + (90 - sunZen)) ** - 1.6364)))),pressure) / 101325
    
    AMa = np.multiply(AMaR,pressure) / 101325
    AMa[AMa > 10] = 0
    #Extraterrestrial irradiation
    I0 = pvl_extraradiation(n)
    #GHI Estimation
    ClearSkyGHI,ClearSkyDNI,ClearSkyDHI = pvl_clearsky_ineichen1(n,hora,lat,lon,alt,sunZen,AMa)
    # ClearSkyGHI = 1098.* cosd(sunZen) .* exp(-0.059 ./ cosd(sunZen))  # Haurwitz
    ClearSkyGHI[ClearSkyGHI < 0] = 0
    ClearSkyDHI[ClearSkyDHI < 0] = 0
    ClearSkyDNI[ClearSkyDNI < 0] = 0
    #Irradiation calculation for tilt angle
    if pro == 1:
        # Incident diffuse irradiation using Perez model and incidence angle
        for i in np.arange(1,12+1).reshape(-1):
            for j in np.arange(np.arange(1,len(hora(,,1))+1)):
                DHI = ClearSkyDHI(j,i)
                DNI = ClearSkyDNI(j,i)
                I01 = I0(i)
                sunzen = sunZen(j,i)
                sunAz = SunAz(j,i)
                AM = AMa(j,i)
                SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor = pvl_perez(surftilt,surfAz,DHI,DNI,I01,sunzen,sunAz,AM,'allsitescomposite1990')
                if DNI != 0:
                    a[j,i] = np.multiply(np.cos(np.pi/180*sunzen),np.cos(np.pi/180*surftilt)) + np.multiply(np.multiply(np.sin(np.pi/180*surftilt),np.sin(np.pi/180*sunzen)),np.cos(np.pi/180*sunAz - surfAz))
                else:
                    a[j,i] = 90
                Id[j,i] = SkyDiffuse
                Di[j,i] = SkyDiffuse_Iso
                Dc[j,i] = SkyDiffuse_Cir
                Dh[j,i] = SkyDiffuse_Hor
        #Incident angle AOI
        a[a > 1] = 1
        a[a < - 1] = - 1
        AOI = acosd(a)
        #Incident beam irradiation
        Ib = np.multiply(ClearSkyDNI,np.cos(np.pi/180*AOI))
        #Incident ground-reflected Irradiation
        Ir = np.multiply(np.multiply(ro,(np.multiply(ClearSkyDNI,np.cos(np.pi/180*sunZen)) + ClearSkyDHI)),((1 - np.cos(np.pi/180*surftilt)) / 2))
        #Total incident irradiation for clearsky
        I = Ib + Id + Ir
        teste = nansum(I)
        Avg = mean(teste)
        incl = surftilt
        ori = surfAz
    
    if pro == 2:
        for k in np.arange(1,dif+1).reshape(-1):
            # Incident diffuse irradiation using Perez model and incidence angle
            for i in np.arange(1,12+1).reshape(-1):
                for j in np.arange(np.arange(1,len(hora(,,1))+1)):
                    DHI = ClearSkyDHI(j,i)
                    DNI = ClearSkyDNI(j,i)
                    I01 = I0(i)
                    sunzen = sunZen(j,i)
                    sunAz = SunAz(j,i)
                    AM = AMa(j,i)
                    SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor = pvl_perez(surftilt,surfAz,DHI,DNI,I01,sunzen,sunAz,AM,'allsitescomposite1990')
                    if DNI != 0:
                        a[j,i] = np.multiply(np.cos(np.pi/180*sunzen),np.cos(np.pi/180*surftilt)) + np.multiply(np.multiply(np.sin(np.pi/180*surftilt),np.sin(np.pi/180*sunzen)),np.cos(np.pi/180*sunAz - surfAz))
                    else:
                        a[j,i] = 90
                    Id[j,i] = SkyDiffuse
                    Di[j,i] = SkyDiffuse_Iso
                    Dc[j,i] = SkyDiffuse_Cir
                    Dh[j,i] = SkyDiffuse_Hor
            #Incident angle AOI
            a[a > 1] = 1
            a[a < - 1] = - 1
            AOI = acosd(a)
            #Incident beam irradiation
            Ib = np.multiply(ClearSkyDNI,np.cos(np.pi/180*AOI))
            #Incident ground-reflected Irradiation
            Ir = np.multiply(np.multiply(ro,(np.multiply(ClearSkyDNI,np.cos(np.pi/180*sunZen)) + ClearSkyDHI)),((1 - np.cos(np.pi/180*surftilt)) / 2))
            #Total incident irradiation for clearsky
            I = Ib + Id + Ir
            teste = nansum(I)
            Avg[k] = mean(teste)
            postilt[k] = surftilt
            i = 1
            j = 1
            l = 1
            surftilt = surftilt + 1
        M,I = np.amax(Avg)
        incl = postilt(I)
        ori = surfAz
    
    if pro == 3:
        for k in np.arange(1,dif+1).reshape(-1):
            for l in np.arange(1,(360 / 10)+1).reshape(-1):
                # Incident diffuse irradiation using Perez model and incidence angle
                for i in np.arange(1,12+1).reshape(-1):
                    for j in np.arange(np.arange(1,len(hora(,,1))+1)):
                        DHI = ClearSkyDHI(j,i)
                        DNI = ClearSkyDNI(j,i)
                        I01 = I0(i)
                        sunzen = sunZen(j,i)
                        sunAz = SunAz(j,i)
                        AM = AMa(j,i)
                        SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor = pvl_perez(surftilt,surfAz,DHI,DNI,I01,sunzen,sunAz,AM,'allsitescomposite1990')
                        if DNI != 0:
                            a[j,i] = np.multiply(np.cos(np.pi/180*sunzen),np.cos(np.pi/180*surftilt)) + np.multiply(np.multiply(np.sin(np.pi/180*surftilt),np.sin(np.pi/180*sunzen)),np.cos(np.pi/180*sunAz - surfAz))
                        else:
                            a[j,i] = 90
                        Id[j,i] = SkyDiffuse
                        Di[j,i] = SkyDiffuse_Iso
                        Dc[j,i] = SkyDiffuse_Cir
                        Dh[j,i] = SkyDiffuse_Hor
                #Incident angle AOI
                a[a > 1] = 1
                a[a < - 1] = - 1
                AOI = acosd(a)
                #Incident beam irradiation
                Ib = np.multiply(ClearSkyDNI,np.cos(np.pi/180*AOI))
                #Incident ground-reflected Irradiation
                Ir = np.multiply(np.multiply(ro,(np.multiply(ClearSkyDNI,np.cos(np.pi/180*sunZen)) + ClearSkyDHI)),((1 - np.cos(np.pi/180*surftilt)) / 2))
                #Total incident irradiation for clearsky
                I = Ib + Id + Ir
                teste = nansum(I)
                Avg[k,l] = mean(teste)
                posAz[k,l] = surfAz
                postilt[k,l] = surftilt
                i = 1
                j = 1
                surfAz = surfAz + 10
            surfAz = 0
            i = 1
            j = 1
            l = 1
            surftilt = surftilt + 1
        M,I = np.amax(Avg)
        I_row,I_col = ind2sub(Avg.shape,I)
        incl = postilt(I_row)
        ori = posAz(I_col)
    
    ################ ATE AQUI ESTÁ CORRETO ####################################
    
    # Parei aqui. considerar os efeitos das perdas e nebulosidade sobre os
# valores determinados para I. I pode ser calculado para cada dia do ano
# ao inves de um dia medio de cada mes. Parei na pagina 31 effective poa
# para obter inclinacao e orientacao variar surftilt e surfAz e calcular a
# irr total, escolhendo a de maior valor.
    
    # [Front_Irradiance,Rear_Irradiance] = pvl_Purdue_bifacial_irradiance(SurfTilt, SurfAz, EtoH, Albedo, DHI, DNI, HExtra, SunZen, SunAz, AM, varargin)
# [I_Alb] = pvl_Purdue_albedo_model(SurfTilt, SurfAz, EtoH, Albedo,DHI, DNI, HExtra, SunZen, SunAz, AM, varargin)
# [Pwat] = pvl_calcPwat(T,RH)
    
    # out = pvl_detect_shadows(Time, GHI, interval, site_info, dbg)
    
    # [clearSamples, csGHI, alpha] = pvl_detect_clear_times(GHI, Time, UTCoffset, Location, win_length, sample_interval)
    
    # kbh=Hb./Hg
# kd=Hd./Hg
# #Irradiation calculation for tilt angle
# Dai = abs(abs(lat)-abs(beta))
# Daf = abs(lat)+abs(beta)
# if Dai<10
# inicio=10
# else
# inicio=Dai
# end
# if Daf>80
# final=80
# else
# final=Daf
# end
# dif=floor(final-inicio)
# beta=inicio;
# for j=1:12
# for i=1:dif
# #Diffuse irradiation from Perez methodology
# #Rb(i,j)=Ht(j)/Hb(j)   #ver melhor maneira de calcular Rb
# #Rb(i,j)=(  cos((theta+beta)*rad).*cos(dec(j)*rad).*sin(HrAngleR(i))+(pi/180).*wsb(i,j).*sin((theta+beta)*rad).*sin(phi(j)*rad)  ) / (  cos(theta*rad).*cos(phi(j)*rad).*cos(ws(j).*rad)+(pi/180).*ws(j).*sin(theta*rad)*sin(phi(j)*rad)  )
# #Rb(i,j)=(  cos((theta+beta)*rad).*cos(phi(j)*rad).*sin(wsb(i,j).*rad)+(pi/180).*wsb(i,j).*sin((theta+beta)*rad).*sin(phi(j)*rad)  ) / (  cos(theta*rad).*cos(phi(j)*rad).*cos(ws(j).*rad)+ws(j).*sin(theta*rad)*sin(phi(j)*rad)  )
# Rb(i,j)=cos(beta*rad)/cos(z(j)*rad)
# #total irradiation for beta inclination
# HT(i,j)=(Hg(j)-Hd(j)).*Rb(i,j) + Hd(j)*0.5*(1+cos(beta*rad)) + Hg(j).*ro*0.5*(1-cos(beta*rad))  # Liu, Jordan, 1963
# HTH(i,j)=Hg(j).*((1-kd(j)).*Rb(i,j) + ro.*0.5.*(1-cos(beta*rad)) + kd(j).*0.5.*(1+cos(beta)))   # klein, 1977
# HTP(i,j)=Hg(j).*(kbh(j).*Rb(i,j) + Hg(j).*ro.*0.5.*(1-cos(beta*rad)) + Hg(j).*(1-kbh(j)).*0.5.*(1+cos(beta)))   # Hay, 1979
# BETA(i,j)=beta
# beta=beta+1
# end
# beta=inicio
# end
    
    # for i=1:dif
# opt(i)=sum(HT(i,:))
# opt1(i)=sum(HTH(i,:))
# opt2(i)=sum(HTP(i,:))
# end
# [l,c]=max(opt)
# beta=BETA(c)
# [l1,c1]=max(opt1)
# beta1=BETA(c1)
# [l2,c2]=max(opt2)
# beta2=BETA(c2)
    
    
    
    
    
    
    
    
    
    return incl,ori