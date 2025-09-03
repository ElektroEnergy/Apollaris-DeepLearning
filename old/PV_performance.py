###########################################################################
#                    SOLAR PANEL DESIGN CODE                              #
# THE METHODOLOGY CONSIDER THE AVALIABLE SPACE IN THE LOCATION AND THE    #
# DESIDERED DEMAND FOR CONSUMERS FOR STAND-ALONE OPERATION AND ON GRID    #
#                                                                         #
# PREPARED BY: GUSTAVO KAEFER DILL - JUNE 2017                            #
#                                                                         #
# Variables: tilt angle, efficency, type, type of inverter, battery capac.#
#            battery voltage                                              #
###########################################################################
import numpy as np
import matplotlib.pyplot as plt
import os
clear('all')
# 1 - LOCATION AND SYSTEM INFORMATION
# Enter the geographical coordinates where the panels will be installed
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%IF YOU DO NOT KNOW THAT, GO TO GOOGLE\MAPS, SET THE LOCATION AND OVER THE LOCATION SET WHAT IS HERE                 %')
print('Write just one digit after the comma, use only "." for numbers not ","                                               %')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
lon = input_('Enter the longitude \n')
lat = input_('Enter the latitude \n')
wind_speed = input_('Enter the annual average of wind speed in (m/s) \n')
x_temp = input_('Enter the annual average temperature in (ºC) \n')
b_temp = input_('Enter the annual maximum temperature in (ºC) \n')
n_temp = input_('Enter the annual minimum temperature in (ºC) \n')
len_ = input_('Enter the Lenght of the area for PV installation (m) \n')
wid = input_('Enter the Width of the area for PV installation (m) \n')
vff = input_('Enter the system voltage phase-phase. If the distribution system has one phase, inform the voltage phase-neutro (127V) \n')
vfn = vff / np.sqrt(3)
# Solar PV boundary area
area = len_ * wid
# 2 - ELECTRICITY CONSUPTION
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%%%%%%%%%%%%%%%%%%%%%%%%  ENTER THE ELECTRICITY CONSUPTION   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ')
print('[1] ENTER THE CONSUPTION FROM JANUARY TO DECEMBER         [2] ENTER A MEDIUM VALUE OR MAXIMUM VALUE OF A MONTH')
print('[3] TO COMPUTE THE DEMAND USING LIGHT CRITEREA')
sel = input_('Type [1], [2] or [3] \n')
demand = consumption(sel,area)
# 3 - DESIGN
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%%%%%%%%%%%%%%%%%%%%%%%%      CHOOSE THE PROJECT DESIGN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#disp('[1]-OFF-GRID OPTIMUM                       [3]-OFF-GRID CHOOSING THE PV MODEL')
print('[2]-GRID-TIE OPTIMUM                       [4]-GRID-TIE CHOOSING THE PV MODEL')
pro = input_('Type the option [2] OR [4] \n')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%%%%%%%%%%%%%%%%%%%%%%%%      CHOOSE THE PROJECT DESIGN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('[1]-ANNUAL MEDIUM DEMAND                       [2]-MINIMUM DEMAND EVERY MONTH')
proj = input_('Type the option [1] OR [2] \n')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
if pro == 4:
    pv_mo = brapv(pro)

# Result from the latitude and longitude
sol,y,y1,y2 = irradiation(lat,lon)
h,h1,h2 = month_hour(y,y1,y2)
#wind_speed_rio = 3.89m/s;
#wind_speed_salvador= 5.44m/s;
E = 1000
a_temp = 0.943 * x_temp + 0.0195 * E - 1.528 * wind_speed + 0.3529
m_temp = 0.943 * x_temp + 0.0195 * E - 1.528 * wind_speed + 0.3529
# Data_sheet
fro = inverter_parameters_1(pro)
bat = battery_parameters(pro)
sun = pv_parameters_1(pro)
lcc = lc_parameters(pro)
Fc = 0.8

if pro == 2:
    # Compute the demand of the system
    P_tilt,P_dir,P_dif,M_tilt,M_dir,M_dif = power2(demand,h,h1,h2,fro,proj,Fc)
    # 4 - PV DESIGN
    Ntt,Ndd,Nddf,pt,pd,pdf,p,p1,p2 = pv2(a_temp,m_temp,area,M_tilt,M_dir,M_dif,sun,fro)
    # # 7 - INVERTER AND MPPT DESIGN
    Nit,Cit,pit,Nt,Ct,ptt,Npit,Nft,Npt1,Npt2,tt = inverter2t(M_tilt,a_temp,m_temp,b_temp,n_temp,p,pt,Ntt,vff)
    Nid,Cid,pid,Nd,Cd,pdd,Npid,Nfd,Npd1,Npd2,td = inverter2d(M_dir,a_temp,m_temp,b_temp,n_temp,p1,pd,Ndd,vff)
    Nidf,Cidf,pidf,Ndf,Cdf,pddf,Npidf,Nfdf,Npdf1,Npdf2,tdf = inverter2df(M_dif,a_temp,m_temp,b_temp,n_temp,p2,pdf,Nddf,vff)
    # # OPTIMIZATION AND SELECTION CRITERIA
    Nt,Nit,pt,pit,Npit,Nft,Npt1,Npt2,tt,NFT = optm2t(ptt,Nt,Ct,pit,Nit,Cit,fro,sun,Npit,Nft,Npt1,Npt2,tt)
    Nd,Nid,pd,pid,Npid,Nfd,Npd1,Npd2,td,NFD = optm2d(pdd,Nd,Cd,pid,Nid,Cid,fro,sun,Npid,Nfd,Npd1,Npd2,td)
    Ndf,Nidf,pdf,pidf,Npidf,Nfdf,Npdf1,Npdf2,tdf,NFDF = optm2df(pddf,Ndf,Cdf,pidf,Nidf,Cidf,fro,sun,Npidf,Nfdf,Npdf1,Npdf2,tdf)
    P_tilt,P_dir,P_dif = cor_P(pit,pid,pidf,P_tilt,P_dir,P_dif)
    # 9 - CABLES DESIGN

if pro == 4:
    # Compute the demand of the system
    P_tilt,P_dir,P_dif,M_tilt,M_dir,M_dif = power2(demand,h,h1,h2,fro,proj,Fc)
    # 4 - PV DESIGN
    Ntt,Ndd,Nddf,pt,pd,pdf,p,p1,p2 = pv4(a_temp,m_temp,area,M_tilt,M_dir,M_dif,sun,fro,pv_mo)
    # 7 - INVERTER AND MPPT DESIGN
    Nit,Cit,pit,Nt,Ct,Npit,Nft,Npt1,Npt2,tt = inverter4t(M_tilt,a_temp,m_temp,b_temp,n_temp,p,pt,Ntt,vff)
    Nid,Cid,pid,Nd,Cd,Npid,Nfd,Npd1,Npd2,td = inverter4d(M_dir,a_temp,m_temp,b_temp,n_temp,p1,pd,Ndd,vff)
    Nidf,Cidf,pidf,Ndf,Cdf,Npidf,Nfdf,Npdf1,Npdf2,tdf = inverter4df(M_dif,a_temp,m_temp,b_temp,n_temp,p2,pdf,Nddf,vff)
    piit = pit
    piid = pid
    piidf = pidf
    Niit = Nit
    Niid = Nid
    Niidf = Nidf
    # OPTIMIZATION AND SELECTION CRITERIA
    Nt,Nit,pt,pit,Npit,Nft,Npt1,Npt2,tt,NFT = optm4t(pt,Nt,Ct,pit,Nit,Cit,fro,sun,Npit,Nft,Npt1,Npt2,tt)
    Nd,Nid,pd,pid,Npid,Nfd,Npd1,Npd2,td,NFD = optm4d(pd,Nd,Cd,pid,Nid,Cid,fro,sun,Npid,Nfd,Npd1,Npd2,td)
    Ndf,Nidf,pdf,pidf,Npidf,Nfdf,Npdf1,Npdf2,tdf,NFDF = optm4df(pdf,Ndf,Cdf,pidf,Nidf,Cidf,fro,sun,Npidf,Nfdf,Npdf1,Npdf2,tdf)
    NFT
    NFD
    NFDF
    P_tilt,P_dir,P_dif = cor_P(pit,pid,pidf,P_tilt,P_dir,P_dif)
    # 8 - CABLES DESIGN

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
# Figure 1 - Day Insollation
f1 = plt.figure(1)
format('bank')
d_t = sum(y / 12)
d_d = sum(y1 / 12)
d_df = sum(y2 / 12)
h_t = np.array([y,d_t])
h_d = np.array([y1,d_d])
h_df = np.array([y2,d_df])
yy = np.array([[h_t],[h_d],[h_df]])
rnames1 = np.array(['Tilt [h]','Direct [h]','Diffuse [h]'])
cnames1 = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Annual'])
t1 = uitable(f1,'Data',yy,'ColumnName',cnames1,'RowName',rnames1,'units','normalized','ColumnWidth',np.array([69]))
#'Position',[400 93 121 243],...
subplot(2,1,1,'position')
x = np.array([np.arange(1,12+1,1)])
plt.plot(x,y,'--or')
grid
plt.xlabel('Months')
plt.ylabel('Hours [h]')
plt.title('HOURS OF SUN PER DAY')
hold('on')
plt.plot(x,y1,'-+b')
plt.plot(x,y2,':*m')
plt.legend('Tilted','Direct','Difuse')
subplot(2,1,2)
pos1 = get(subplot(2,1,2),'position')
os.delete(subplot(2,1,2))
set(t1,'position',pos1)
# Figure 2 - Solar power
f2 = plt.figure(2)
format('bank')
Pger_t = (np.multiply(np.multiply(pt(1,6) * Nt,h(1,:)),Fc)) / 1000
Pger_d = (np.multiply(np.multiply(pd(1,6) * Nd,h1(1,:)),Fc)) / 1000
Pger_df = (np.multiply(np.multiply(pdf(1,6) * Ndf,h2(1,:)),Fc)) / 1000
Mger_t = sum(Pger_t / 12)
Mger_d = sum(Pger_d / 12)
Mger_df = sum(Pger_df / 12)
ger_t = np.array([Pger_t,Mger_t])
ger_d = np.array([Pger_d,Mger_d])
ger_df = np.array([Pger_df,Mger_df])
P = np.array([[ger_t],[ger_d],[ger_df]])
rnames2 = np.array(['Tilt[kWh]','Direct [kWh]','Diffuse [kWh]'])
cnames2 = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Annual'])
t2 = uitable(f2,'Data',P,'ColumnName',cnames2,'RowName',rnames2,'units','normalized','ColumnWidth',np.array([69]))
#'Position',[400 93 121 243],...
subplot(2,1,1,'position')
x = np.array([np.arange(1,12+1,1)])
plt.plot(x,Pger_t,'--or')
grid
plt.xlabel('Months')
plt.ylabel('Energy [kWh]')
plt.title('ENERGY PRODUCED BY MONTH')
hold('on')
plt.plot(x,Pger_d,':*m')
plt.plot(x,Pger_df,'-.+g')
plt.legend('Tilt','Direct','Difuse')
subplot(2,1,2)
#plot(t2)
plt.xlabel('Installation')
plt.ylabel('Solar Power [kW]')
plt.title('Maximum Power Produced')
pos2 = get(subplot(2,1,2),'position')
os.delete(subplot(2,1,2))
set(t2,'position',pos2)
# Solar Painel + Inverter Parameters
f3 = plt.figure(3)
format('bank')
St,Sd,Sdf = pv_string_1(pt,pd,pdf)
Sit,Sid,Sidf = inv_string_1(pit,pid,pidf)
pvv = np.array([[pt(1,np.arange(2,22+1))],[pd(1,np.arange(2,22+1))],[pdf(1,np.arange(2,22+1))]])
svv = np.array([[St],[Sd],[Sdf]])
inv = np.array([[pit(1,np.arange(2,25+1))],[pid(1,np.arange(2,25+1))],[pidf(1,np.arange(2,25+1))]])
sinv = np.array([[Sit],[Sid],[Sidf]])
nt = np.array([Nt,Nit,Npit,Npt1,Npt2,tt])
nd = np.array([Nd,Nid,Npid,Npd1,Npd2,td])
ndf = np.array([Ndf,Nidf,Npidf,Npdf1,Npdf2,tdf])
ntt = np.array([num2cell(nt),NFT])
ndd = np.array([num2cell(nd),NFD])
nddf = np.array([num2cell(ndf),NFDF])
nin = np.array([np.transpose(nt),np.transpose(nd),np.transpose(ndf)])
pvvv = np.array([svv,num2cell(pvv)])
invv = np.array([sinv,num2cell(inv)])
cnames3 = np.array(['Number of Solar Painel','Number of Inverters','Number of Solar Painel by inverter','Max. Number of String by Inverter at MPPT1','Max. Number of String by Inverter at MPPT2','Number of Power Transformer'])
rnames3 = np.array(['For tilted design','For direct design','For diffuse design'])
t3 = uitable(f3,'Data',nin,'ColumnName',rnames3,'RowName',cnames3,'Position',np.array([20,400,1200,150]),'ColumnWidth',np.array([80]))
txt_title3 = uicontrol('Style','text','Position',np.array([600,635,200,20]),'String','RESULTS')
f4 = plt.figure(4)
format('bank')
cnames4 = np.array(['Type','ocv','scc','vmax','imax','pmax','Vmax','ocvt','otvmp','tcisc','weig','deph','widt','leng','ibest','area','ef','ncell','tol+','dur','tcell','tier'])
rnames4 = np.array(['For tilted instalation','For direct instalation','For diffuse instalation'])
t4 = uitable(f4,'Data',pvvv,'ColumnName',cnames4,'RowName',rnames4,'Position',np.array([20,400,1200,150]),'ColumnWidth',np.array([40]))
txt_title4 = uicontrol('Style','text','Position',np.array([600,430,200,20]),'String','SOLAR PAINEL PARAMETERS')
f5 = plt.figure(5)
format('bank')
cnames5 = np.array(['Type','minvr','maxvr','miv','nout','mout','mdcp','meff','mint','maxt','weig','heig','widt','leng','ibest','PN','maxc1','maxc2','vouti','mip1','mip2','aci','minv','mod','tier'])
rnames5 = np.array(['For tilted instalation','For direct instalation','For diffuse instalation'])
t5 = uitable(f5,'Data',invv,'ColumnName',cnames5,'RowName',rnames5,'Position',np.array([20,400,1200,150]),'ColumnWidth',np.array([40]))
txt_title5 = uicontrol('Style','text','Position',np.array([600,225,200,20]),'String','INVERTER PARAMETERS WITH MPPT')
if pro == 4:
    Siit,Siid,Siidf,piit,piid,piidf = inv_string4(piit,piid,piidf,fro)
    # Figure 4 - Other possible inverters
    f6 = plt.figure(6)
    format('bank')
    inv_t = np.array([num2cell(np.transpose(Niit)),Siit,num2cell(piit(:,np.arange(2,24+1)))])
    cnames6 = np.array(['No.Inverters','Type','minvr','maxvr','miv','nout','mout','mdcp','meff','mint','maxt','weig','heig','widt','leng','ibest','PN','maxc1','maxc2','vouti','mip1','mip2','aci','minv','mod'])
    t6 = uitable(f6,'Data',inv_t,'ColumnName',cnames6,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title6 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH TILTED INSTALLATION')
    # Figure 5 - Other possible inverters
    f7 = plt.figure(7)
    format('bank')
    inv_d = np.array([num2cell(np.transpose(Niid)),Siid,num2cell(piid(:,np.arange(2,24+1)))])
    cnames7 = np.array(['No.Inverters','Type','minvr','maxvr','miv','nout','mout','mdcp','meff','mint','maxt','weig','heig','widt','leng','ibest','PN','maxc1','maxc2','vouti','mip1','mip2','aci','minv','mod'])
    t7 = uitable(f7,'Data',inv_d,'ColumnName',cnames7,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title8 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH DIRECT INSTALLATION')
    # Figure 4 - Other possible inverters
    f8 = plt.figure(8)
    format('bank')
    inv_df = np.array([num2cell(np.transpose(Niidf)),Siidf,num2cell(piidf(:,np.arange(2,24+1)))])
    cnames8 = np.array(['No.Inverters','Type','minvr','maxvr','miv','nout','mout','mdcp','meff','mint','maxt','weig','heig','widt','leng','ibest','PN','maxc1','maxc2','vouti','mip1','mip2','aci','minv','mod'])
    t8 = uitable(f8,'Data',inv_df,'ColumnName',cnames8,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title9 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH DIFFUSE INSTALLATION')

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')