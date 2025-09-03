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
# # 1 - LOCATION AND SYSTEM INFORMATION
# # Enter the geographical coordinates where the panels will be installed
# disp('######################################################################################################################')
# disp('#IF YOU DO NOT KNOW THAT, GO TO GOOGLE\MAPS, SET THE LOCATION AND OVER THE LOCATION SET WHAT IS HERE                 #')
# disp('Write just one digit after the comma, use only "." for numbers not ","                                               #')                                                                                 #')
# disp('######################################################################################################################')
options.Resize = 'On'

options.WindowStyle = 'modal'

options.Interpreter = 'tex'

prompt = np.array(['Enter the longitude:','Enter the latitude:','Enter the annual average of wind speed for day times in (m/s)','Enter the annual average temperature for day times in (ºC)','Enter the annual maximum temperature for day times in (ºC)','Enter the annual minimum temperature for day times in (ºC)','Enter the altitud in (m)','Enter the annual minimum humidity in (%)','Enter the area without shadding for the PV installation (m²)','Enter the number of phases avaliable in the nearest system. Type [1], [2] or [3]','Enter the distribution/transmission system voltage phase-pneutro.','Enter the frequency of the grid in (Hz)','Enter [2]-ON-grid optimum design or [4]-ON-grid optimum design choosing the PV model','Enter the load demand [1]-per month; [2]-annual average; [3]-Light criteria','Enter the shadding factor [0 to 1]','Enter the PV inclination angle (roof angle) [in graus] or [Nan] for optimal angle design','Enter the PV azimuth angle [in graus], North is 0 graus or [Nan] for optimal angle design'])
dlg_title = 'Location and System Information'
num_lines = np.array([1,100])
defaultans = np.array(['-43.22','-22.91','3.98','23.15','41','14','20','99','100','3','127','60','2','2','1','Nan','Nan'])
DadosForm = inputdlg(prompt,dlg_title,num_lines,defaultans)
lon = str2double(DadosForm(1))
lat = str2double(DadosForm(2))
wind_speed = str2double(DadosForm(3))
x_atemp = str2double(DadosForm(4))
max_atemp = str2double(DadosForm(5))
min_atemp = str2double(DadosForm(6))
alt = str2double(DadosForm(7))
hum = str2double(DadosForm(8))
area = str2double(DadosForm(9))
nf = str2double(DadosForm(10))
vfn = str2double(DadosForm(11))
freq = str2double(DadosForm(12))
pro = str2double(DadosForm(13))
#[proj] = str2double(DadosForm(14));
#[criteria] = str2double(DadosForm(15));
sel = str2double(DadosForm(14))
FS = str2double(DadosForm(15))
stil = str2double(DadosForm(16))
sazi = str2double(DadosForm(17))
proj = 4
# [x_temp]=temp_data(x_temp);
# [wind_speed]=wind_data(wind_speed);

# Data_sheet
froS,froN = inverter_parameters(pro)
#[bat]=battery_parameters(pro);
sunS,sunN,brandpv = pv_parameters(pro)
#[lcc]=lc_parameters(pro);
Fc = 0.8

# For choosing PV model
#pv_mo=1;
if pro == 4:
    pv_mo = brapv(sunS,brandpv)

# 2 - ELECTRICITY CONSUPTION
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
    # # OPTIMIZATION AND SELECTION CRITERIA
#if criteria==4
    Nto,Nito,pto,pito,Npito,Nfto,Npt1o,tto,NFTo,NSto,pato,disto,dmaxo = optm2ttopsis(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria==3
    Nta,Nita,pta,pita,Npita,Nfta,Npt1a,tta,NFTa,NSta,pata,Mta,lta,xta,dista,dmaxa = optm2ta(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria==2
    Ntc,Nitc,ptc,pitc,Npitc,Nftc,Npt1c,ttc,NFTc,NStc,patc,distc,dmaxc = optm2tc(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria==1
    Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,pat,dist,dmax = optm2t(ptt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end

if pro == 4:
    # 4 - PV DESIGN
    Ntt,pt,p = pv4(area,M_tilt,sunN1,froN,pv_mo)
    # 7 - INVERTER AND MPPT DESIGN
    Nit,Cit,pit,Nt,Ct,Npit,Nft,Npt1,tt,NS = inverter4t(M_tilt,min_atemp,max_atemp,p,pt,Ntt,vfn,nf,alt,hum,freq)
    # OPTIMIZATION AND SELECTION CRITERIA
#if criteria==4
    Nto,Nito,pto,pito,Npito,Nfto,Npt1o,tto,NFTo,NSto,Niito,piito,disto,dmaxo = optm4ttopsis(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria ==3
    Nta,Nita,pta,pita,Npita,Nfta,Npt1a,tta,NFTa,NSta,Cta,Niita,piita,dista,dmaxa = optm4ta(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria==2
    Ntc,Nitc,ptc,pitc,Npitc,Nftc,Npt1c,ttc,NFTc,NStc,Niitc,piitc,distc,dmaxc = optm4tc(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end
#if criteria==1
    Nt,Nit,pt,pit,Npit,Nft,Npt1,tt,NFT,NSt,Niit,piit,dist,dmax = optm4t(pt,Nt,Ct,pit,Nit,Cit,froN,sunN1,Npit,Nft,Npt1,tt,NS)
    #end

P_tilt = cor_P(pit,P_tilt)
# 8 - CABLES DESIGN

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
# Figure 1 - Day Insollation
f1 = plt.figure(1)
format('bank')
d_t = sum(y / 12)
Tm_t = sum(Tm / 12)
h_t = np.array([[y,d_t],[Tm,Tm_t]])
yy = np.array([h_t])
rnames1 = np.array(['Hours of sun with 1000W/m² Irr [h]','Hours of sun'])
cnames1 = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Annual'])
t1 = uitable(f1,'Data',yy,'ColumnName',cnames1,'RowName',rnames1,'units','normalized','ColumnWidth',np.array([69]))
#'Position',[400 93 121 243],...
subplot(2,1,1,'position')
x = np.array([np.arange(1,12+1,1)])
plt.plot(x,y,'--or')
hold('on')
plt.plot(x,Tm,'--xb')
grid
plt.xlabel('Months')
plt.ylabel('Hours [h]')
plt.title('AVERAGE HOURS OF SUN PER DAY')
plt.legend('Hours of sun with 1000W/m² irradiation','Hours of sun')
subplot(2,1,2)
pos1 = get(subplot(2,1,2),'position')
os.delete(subplot(2,1,2))
set(t1,'position',pos1)
# Figure 2 - Solar power
f2 = plt.figure(2)
Pger_t = (np.multiply(np.multiply(pt(1,6) * Nt,h(1,:)),Fc)) / 1000
Pger_a = (np.multiply(np.multiply(pta(1,6) * Nta,h(1,:)),Fc)) / 1000
Pger_o = (np.multiply(np.multiply(pto(1,6) * Nto,h(1,:)),Fc)) / 1000
Pger_c = (np.multiply(np.multiply(ptc(1,6) * Ntc,h(1,:)),Fc)) / 1000
Mger_t = sum(Pger_t / 12)
Mger_a = sum(Pger_a / 12)
Mger_o = sum(Pger_o / 12)
Mger_c = sum(Pger_c / 12)
ger_t = np.array([Pger_t,Mger_t])
ger_a = np.array([Pger_a,Mger_a])
ger_o = np.array([Pger_o,Mger_o])
ger_c = np.array([Pger_c,Mger_c])
dtot = mean(demand(1,:)) / 1000
demand_tot = np.array([demand / 1000,dtot])
#P = [demand_tot; ger_t];
P = np.array([[demand_tot],[ger_t],[ger_a],[ger_o],[ger_c]])
rnames2 = np.array(['Load[kWh]','Performance[kWh]','Optimal[kWh]','Topsis[kWh]','Cost[kWh]'])
cnames2 = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Annual'])
t2 = uitable(f2,'Data',P,'ColumnName',cnames2,'RowName',rnames2,'units','normalized','ColumnWidth',np.array([69]))
#'Position',[400 93 121 243],...
subplot(2,1,1,'position')
x = np.array([np.arange(1,12+1,1)])
plt.plot(x,demand / 1000,'-+b')
grid
plt.xlabel('Months')
plt.ylabel('Energy [kWh]')
plt.title('ENERGY PRODUCED BY MONTH')
hold('on')
plt.plot(x,Pger_t,'--or')
plt.plot(x,Pger_a,':*m')
plt.plot(x,Pger_o,'-.+g')
plt.plot(x,Pger_c,'-.k')
plt.legend('Load[kWh]','Performance[kWh]','Optimal[kWh]','Topsis[kWh]','Cost[kWh]')
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
St,Sit,Sta,Sita,Sto,Sito,Stc,Sitc = pv_inv_string2(pt,pta,pto,ptc,sunS,pit,pita,pito,pitc,froS)
if Nt != 0:
    incl = incl
    ori = ori
else:
    incl = 0
    ori = 0

if Nta != 0:
    incla = incl
    oria = ori
else:
    incla = 0
    oria = 0

if Nto != 0:
    inclo = incl
    orio = ori
else:
    inclo = 0
    orio = 0

if Ntc != 0:
    inclc = incl
    oric = ori
else:
    inclc = 0
    oric = 0

nt = np.array([Nt,Nit,Npit,Npt1,NSt,tt,incl,ori,dist,dmax])
nta = np.array([Nta,Nita,Npita,Npt1a,NSta,tta,incla,oria,dista,dmaxa])
nto = np.array([Nto,Nito,Npito,Npt1o,NSto,tto,inclo,orio,disto,dmaxo])
ntc = np.array([Ntc,Nitc,Npitc,Npt1c,NStc,ttc,inclc,oric,distc,dmaxc])
nft,nfta,nftc,nfto = checking(Nt,Nto,Ntc,Nta,NFT,NFTa,NFTo,NFTc)
# nftaco=[nft;nfta;nfto;nftc];
# ntaco=[Nt;Nta;Nto;Ntc];
# nitaco=[Nit;Nita;Nito;Nitc];

svv = np.array([[St],[Sta],[Sto],[Stc]])
sinv = np.array([[Sit],[Sita],[Sito],[Sitc]])
pvv = np.array([[pt(1,np.arange(2,25+1))],[pta(1,np.arange(2,25+1))],[pto(1,np.arange(2,25+1))],[ptc(1,np.arange(2,25+1))]])
inv = np.array([[pit(1,np.arange(2,32+1))],[pita(1,np.arange(2,32+1))],[pito(1,np.arange(2,32+1))],[pitc(1,np.arange(2,32+1))]])
pvvv = np.array([svv,num2cell(pvv)])
invv = np.array([sinv,num2cell(inv)])
voc_stringT,sec_stringT,Is_minT,Is_maxT,VdioT,IdioT,voc_arranjoT,sec_arranjoT,Ia_minT,Ia_maxT,dps_caT,sec_caT,Id_minT,Id_maxT,txt = protection_system(pt,pit,nft,max_atemp,Nt,Nit,wind_speed,NSt)
voc_stringTA,sec_stringTA,Is_minTA,Is_maxTA,VdioTA,IdioTA,voc_arranjoTA,sec_arranjoTA,Ia_minTA,Ia_maxTA,dps_caTA,sec_caTA,Id_minTA,Id_maxTA,txtA = protection_system(pta,pita,nfta,max_atemp,Nta,Nita,wind_speed,NSta)
voc_stringTO,sec_stringTO,Is_minTO,Is_maxTO,VdioTO,IdioTO,voc_arranjoTO,sec_arranjoTO,Ia_minTO,Ia_maxTO,dps_caTO,sec_caTO,Id_minTO,Id_maxTO,txtO = protection_system(pto,pito,nfto,max_atemp,Nto,Nito,wind_speed,NSto)
voc_stringTC,sec_stringTC,Is_minTC,Is_maxTC,VdioTC,IdioTC,voc_arranjoTC,sec_arranjoTC,Ia_minTC,Ia_maxTC,dps_caTC,sec_caTC,Id_minTC,Id_maxTC,txtC = protection_system(ptc,pitc,nftc,max_atemp,Ntc,Nitc,wind_speed,NStc)
ntt = np.array([num2cell(nt),nft,sec_stringT,voc_stringT,IdioT,VdioT,Is_minT,Is_maxT,voc_stringT,sec_arranjoT,voc_arranjoT,Ia_minT,Ia_maxT,voc_arranjoT,sec_caT,dps_caT,Id_minT,Id_maxT,dps_caT,txt,txt,txt])
ntta = np.array([num2cell(nta),nfta,sec_stringTA,voc_stringTA,IdioTA,VdioTA,Is_minTA,Is_maxTA,voc_stringTA,sec_arranjoTA,voc_arranjoTA,Ia_minTA,Ia_maxTA,voc_arranjoTA,sec_caTA,dps_caTA,Id_minTA,Id_maxTA,dps_caTA,txtA,txtA,txtA])
ntto = np.array([num2cell(nto),nfto,sec_stringTO,voc_stringTO,IdioTO,VdioTO,Is_minTO,Is_maxTO,voc_stringTO,sec_arranjoTO,voc_arranjoTO,Ia_minTO,Ia_maxTO,voc_arranjoTO,sec_caTO,dps_caTO,Id_minTO,Id_maxTO,dps_caTO,txtO,txtO,txtO])
nttc = np.array([num2cell(ntc),nftc,sec_stringTC,voc_stringTC,IdioTC,VdioTC,Is_minTC,Is_maxTC,voc_stringTC,sec_arranjoTC,voc_arranjoTC,Ia_minTC,Ia_maxTC,voc_arranjoTC,sec_caTC,dps_caTC,Id_minTC,Id_maxTC,dps_caTC,txtC,txtC,txtC])
#nin=[nt' nta' nto' ntc'];
nin = np.array([np.transpose(ntt),np.transpose(ntta),np.transpose(ntto),np.transpose(nttc)])
cnames3 = np.array(['Number of PV modules','Number of Inverters','Number of PV modules per inverter','Max. Number of MPPT per inverter','Max. Number of Strings per MPPT','Number of Power Transformer','Module tilt angle - Inclination in [degree]','Module Azimuth angle - Orientation in [degree]','Distance of arrays in [m]','Distance of arrays for maximum power in [m]','Strings distribution per inverter/MPPT/NoDC','Elastômero cable section per string [mm²]','Min. cable voltage insulation per string [V]','Min. diode current per string [A]','Min. diode voltage per string [V]','Min. current for breaker/fuse/disconnector per string [A]','Max. current for breaker/fuse/disconnector per string [A]','Min. Voltage for surge protector type II per string [V]','Elastômero cable section per arrangement [mm²]','Min. cable voltage insulation per arrangement [V]','Min. current for breaker/fuse/disconnector per arrangement [A]','Max. current for breaker/fuse/disconnector per arrangement [A]','Min. Voltage for surge protector type II per arrangement [V]','Cable section in AC side [mm²]','Min. cable voltage insulation in AC side [V]','Min. current for breaker/disconnector in AC side [A]','Max. current for breaker/disconnector in AC side [A]','Min. Voltage for surge protector type II in AC side [V]','Equipotencialize modules/inverters/structure','See local power distributor regulation','Check voltage drop design for cables'])
rnames3 = np.array(['Performance Design','Optimal Design','Topsis Design','Cost Design'])
t3 = uitable(f3,'Data',nin,'ColumnName',rnames3,'RowName',cnames3,'Position',np.array([50,350,1320,350]),'ColumnWidth',np.array([150]))
#txt_title3 = uicontrol('Style', 'text', 'Position', [600 635 200 20], 'String', 'RESULTS');

cnames4 = np.array(['model','ocv','scc','vmp','imp','pmp','Vmax','otvoc','otvmp','tcisc','weig','deph','widt','leng','ibest','ef','ncell','tol+','dur','tcell','tier','temp','TEMP','NOCT','Inop'])
rnames4 = np.array(['Performance PV data','Optimal PV data','Topsis PV data','Cost PV data'])
t4 = uitable(f3,'Data',pvvv,'ColumnName',cnames4,'RowName',rnames4,'Position',np.array([50,200,1400,115]),'ColumnWidth',np.array([60]))
#txt_title4 = uicontrol('Style', 'text', 'Position', [600 430 200 20], 'String', 'SOLAR PAINEL PARAMETERS');

cnames5 = np.array(['model','Imppt','Nmpp','Icc','Vmpptm','VmpptM','mVn','MVn','Nodc','Pdc','Iac','Pac','Sac','mVac','MVac','mf','Mf','THD','FP','Ef','minT','maxT','weig','heig','widt','leng','ibest','Phase','Hum','Alt','mod','tier'])
rnames5 = np.array(['Performance Inverter data','Optimal Inverter data','Topsis Inverter data','Cost Inverter data'])
t5 = uitable(f3,'Data',invv,'ColumnName',cnames5,'RowName',rnames5,'Position',np.array([50,50,1400,115]),'ColumnWidth',np.array([60]))
#txt_title5 = uicontrol('Style', 'text', 'Position', [600 225 200 20], 'String', 'INVERTER PARAMETERS WITH MPPT');

if pro == 4:
    St,Sit,Sta,Sita,Sto,Sito,Stc,Sitc = pv_inv_string4(pt,pta,pto,ptc,sunS,piit,piita,piitc,piito,froS)
    # Figure 4 - Other possible inverters
    f6 = plt.figure(6)
    format('bank')
    inv_t = np.array([num2cell(np.transpose(Niit)),np.transpose(Sit),num2cell(piit(:,np.arange(2,32+1)))])
    cnames6 = np.array(['no','model','Imppt','Nmpp','Icc','Vmpptm','VmpptM','mVn','MVn','Nodc','Pdc','Iac','Pac','Sac','mVac','MVac','mf','Mf','THD','FP','Ef','minT','maxT','weig','heig','widt','leng','ibest','Phase','Hum','Alt','mod','tier'])
    t6 = uitable(f6,'Data',inv_t,'ColumnName',cnames6,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title6 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH MAXIMUM PERFORMANCE DESIGN')
    # Figure 5 - Other possible inverters
    f7 = plt.figure(7)
    format('bank')
    inv_ta = np.array([num2cell(Niita),np.transpose(Sita),num2cell(piita(:,np.arange(2,32+1)))])
    cnames7 = np.array(['no','model','Imppt','Nmpp','Icc','Vmpptm','VmpptM','mVn','MVn','Nodc','Pdc','Iac','Pac','Sac','mVac','MVac','mf','Mf','THD','FP','Ef','minT','maxT','weig','heig','widt','leng','ibest','Phase','Hum','Alt','mod','tier'])
    t7 = uitable(f7,'Data',inv_ta,'ColumnName',cnames7,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title8 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH OPTIMAL DESIGN')
    # Figure 4 - Other possible inverters
    f8 = plt.figure(8)
    format('bank')
    inv_to = np.array([num2cell(np.transpose(Niito)),np.transpose(Sito),num2cell(piito(:,np.arange(2,32+1)))])
    cnames8 = np.array(['no','model','Imppt','Nmpp','Icc','Vmpptm','VmpptM','mVn','MVn','Nodc','Pdc','Iac','Pac','Sac','mVac','MVac','mf','Mf','THD','FP','Ef','minT','maxT','weig','heig','widt','leng','ibest','Phase','Hum','Alt','mod','tier'])
    t8 = uitable(f8,'Data',inv_to,'ColumnName',cnames8,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title9 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH TOPSIS DESIGN')
    f9 = plt.figure(9)
    format('bank')
    inv_tc = np.array([num2cell(np.transpose(Niitc)),np.transpose(Sitc),num2cell(piitc(:,np.arange(2,32+1)))])
    cnames9 = np.array(['no','model','Imppt','Nmpp','Icc','Vmpptm','VmpptM','mVn','MVn','Nodc','Pdc','Iac','Pac','Sac','mVac','MVac','mf','Mf','THD','FP','Ef','minT','maxT','weig','heig','widt','leng','ibest','Phase','Hum','Alt','mod','tier'])
    t6 = uitable(f9,'Data',inv_tc,'ColumnName',cnames6,'Position',np.array([50,50,1290,550]),'ColumnWidth',np.array([50]))
    txt_title6 = uicontrol('Style','text','Position',np.array([400,610,600,15]),'String','POSSIBLES INVERTERS FOR THE PV CHOOSEN WITH MINIMUM COST DESIGN')

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')