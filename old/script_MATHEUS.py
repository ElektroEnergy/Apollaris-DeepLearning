import matplotlib.pyplot as plt
import numpy as np
plt.figure(6)
x = np.array([np.arange(1,12+1,1)])
if vff == 380:
    demand2 = np.array([1360,1293,1310,1267,1184,1156,1148,1212,1289,1379,1355,1470])
    pvsol = np.array([1766,1597,1625,1282,1279,1118,1317,1641,1510,1636,1733,1812])
    conv = np.array([375.65,371.97,401.38,366.22,333.21,308.33,303.3,364.52,335.93,377.73,357.47,363.12])
else:
    demand2 = np.array([360,356,328,380,364,250,223,248,276,289,346,369])
    pvsol = np.array([400,363,403,331,351,287,358,358,331,364,361,387])
    conv = np.array([375.65,371.97,401.38,366.22,333.21,308.33,303.3,364.52,335.93,377.73,357.47,363.12])

#d=[demand2; pvsol; ger_t; ger_d; ger_df];
d = np.array([[demand2],[pvsol],[conv],[Pger_t]])
plt.plot(x,demand2,'-.b','LineWidth',2)
grid
plt.xlabel('Months')
plt.ylabel('Energy [kWh]')
plt.title('ENERGY PRODUCED BY MONTH')
hold('on')
plt.plot(x,pvsol,'-.+g','LineWidth',2)
plt.plot(x,conv,'-.ok','LineWidth',2)
plt.plot(x,Pger_t,'--xr','LineWidth',2)
plt.legend('Demand','PV*Sol','Conventional','Customized')