###########################################################################
#                    SOLAR PANEL DESIGN CODE                              #
# THE METHODOLOGY CONSIDER THE AVALIABLE SPACE IN THE LOCATION AND THE    #
# DESIDERED DEMAND FOR CONSUMERS FOR STAND-ALONE OPERATION AND ON GRID    #
#                                                                         #
# PREPARED BY: GUSTAVO KAEFER DILL - JUNE 2017                            #
# CONVERTED BY: NICOLAS FERNANDES - AUGUST 2025                           #
#                                                                         #
# Variables: tilt angle, efficency, type, type of inverter, battery capac.#
#            battery voltage                                              #
###########################################################################

# Import each function
from inverter_parameters_matheus import inverter_parameters
from pv_parameters_matheus import pv_parameters
from brapv import brapv
from consumption import consumption
from irradiation import irradiation
from month_hour import month_hour
from sol_por_dia import sol_por_dia
from module_temperature import module_temperature
from distancia_de_sombreamento import distancia_de_sombreamento
from power24 import power24
from pv2 import pv2
from inverter2t import inverter2t
from optm2ttopsis import optm2ttopsis
from optm2ta import optm2ta
from optm2tc import optm2tc
from optm2t import optm2t
from pv4 import pv4
from inverter4t import inverter4t
from optm4ttopsis import optm4ttopsis
from optm4ta import optm4ta
from optm4tc import optm4tc
from optm4t import optm4t
from cor_P import cor_P
from pv_inv_string2 import pv_inv_string2
from checking import checking
from protection_system import protection_system
from pv_inv_string4 import pv_inv_string4

import numpy as np
import matplotlib.pyplot as plt
import os


# Manual input of the location and system information

inputs = ['Enter the longitude:','Enter the latitude:','Enter the annual average of wind speed for day times in (m/s)','Enter the annual average temperature for day times in (�C)','Enter the annual maximum temperature for day times in (�C)','Enter the annual minimum temperature for day times in (�C)','Enter the altitud in (m)','Enter the annual minimum humidity in (%)','Enter the area without shadding for the PV installation (m�)','Enter the number of phases avaliable in the nearest system. Type [1], [2] or [3]','Enter the distribution/transmission system voltage phase-pneutro.','Enter the frequency of the grid in (Hz)','Enter [2]-ON-grid optimum design or [4]-ON-grid optimum design choosing the PV model','Enter the load demand [1]-per month; [2]-annual average; [3]-Light criteria','Enter the shadding factor [0 to 1]','Enter the PV inclination angle (roof angle) [in graus] or [Nan] for optimal angle design','Enter the PV azimuth angle [in graus], North is 0 graus or [Nan] for optimal angle design']
lon = int(input(inputs[0]))             # Longitude
lat = int(input(inputs[1]))             # Latitude
wind_speed = int(input(inputs[2]))      # Wind Speed
x_atemp = int(input(inputs[3]))         # Average Temperature
max_atemp = int(input(inputs[4]))       # Maximum Temperature
min_atemp = int(input(inputs[5]))       # Minimum Temperature
alt = int(input(inputs[6]))             # Altitude
hum = int(input(inputs[7]))             # Humidity
area = int(input(inputs[8]))            # Area
nf = int(input(inputs[9]))              # Number of Phases
vfn = int(input(inputs[10]))            # Voltage Phase-Neutral
freq = int(input(inputs[11]))           # Frequency
pro = int(input(inputs[12]))            # Project Type
sel = int(input(inputs[13]))            # Selection Criteria
FS = int(input(inputs[14]))             # Shading Factor
stil = int(input(inputs[15]))           # Tilt Angle
sazi = int(input(inputs[16]))           # Azimuth Angle
proj = 4

# Data sheets
froS,froN = inverter_parameters(pro)
sunS,sunN,brandpv = pv_parameters(pro)

Fc = 0.8

# When especifing the PV model
if pro == 4:
    pv_mo = brapv(sunS,brandpv)

# Demand and Consumption
demand = consumption(sel,area)

# Result from the latitude and longitude
sol,y,incl,ori = irradiation(lat,lon,alt,x_atemp,FS,proj,stil,sazi)
h = month_hour(y)
Tm,T,sunrise_min,sunset_min = sol_por_dia(lon,lat)
#E=mean((y.*1000)./Tm);
E = 1000

x_temp,max_temp,min_temp,nef = module_temperature(wind_speed,x_atemp,sunN,E,max_atemp,min_atemp)
dist,dmax = distancia_de_sombreamento(lat,sunN,sunrise_min)
extra = np.array([x_temp,max_temp,min_temp,dist,dmax])
sunN1 = np.array([sunN,x_temp,max_temp,min_temp,dist,dmax])

# Compute the demand of the system
P_tilt,M_tilt = power24(demand,h,froN,Fc)
if pro == 2:
    # 4 - PV DESIGN
    Ntt,pt,p = pv2(area,M_tilt,sunN1,froN)
    # # 7 - INVERTER AND MPPT DESIGN
    Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,tt,NS = inverter2t(M_tilt,min_atemp,max_atemp,p,pt,Ntt,vfn,nf,alt,hum,freq)
    # # DECISION MAKING CRITERIA
    Nto,Nito,pto,pito,Npito,Nfto,Npt1o,tto,NFTo,NSto,pato,disto,dmaxo = optm2ttopsis(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS,pro)
    Nta,Nita,pta,pita,Npita,Nfta,Npt1a,tta,NFTa,NSta,pata,Mta,lta,xta,dista,dmaxa = optm2ta(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    Ntc,Nitc,ptc,pitc,Npitc,Nftc,Npt1c,ttc,NFTc,NStc,patc,distc,dmaxc = optm2tc(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,dist,dmax = optm2t(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)

if pro == 4:
    # 4 - PV DESIGN
    Ntt,pt,p = pv4(area,M_tilt,sunN1,froN,pv_mo)
    # 7 - INVERTER AND MPPT DESIGN
    Nit,Cit,pit,Nt,Ct,Npit,Nft,Npt1,tt,NS = inverter4t(M_tilt,min_atemp,max_atemp,p,pt,Ntt,vfn,nf,alt,hum,freq)
    # # DECISION MAKING CRITERIA
    Nto,Nito,pto,pito,Npito,Nfto,Npt1o,tto,NFTo,NSto,Niito,piito,disto,dmaxo = optm4ttopsis(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS,pro)
    Nta,Nita,pta,pita,Npita,Nfta,Npt1a,tta,NFTa,NSta,Cta,Niita,piita,dista,dmaxa = optm4ta(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    Ntc,Nitc,ptc,pitc,Npitc,Nftc,Npt1c,ttc,NFTc,NStc,Niitc,piitc,distc,dmaxc = optm4tc(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,Niit,piit,dist,dmax = optm4t(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)

P_tilt = cor_P(pit,P_tilt)
