#function [SunAz, SunEl, ApparentSunEl, SolarTime]= pvl_ephemeris(Time, Location, varargin)
# PVL_EPHEMERIS Calculates the position of the sun given time, location, and optionally pressure and temperature

# Syntax
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location)
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, Pressure)
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, Pressure, Temperature)
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, 'temperature', Temperature)
#
# Description
#  [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location)
#      Uses the given time and location structs to give sun positions with
#      the pressure assumed to be 1 atm (101325 Pa) and the temperature
#      assumed to be 12 C.
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, Pressure)
#      Uses the given time and location structs with the given pressure to
#      determine sun positions. The temperature is assumed to be 12C.
#      Pressure must be given in Pascals (1atm = 101325 Pa). If site pressure
#      is unknown but site altitude is known, a conversion function may be
#      used.
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, Pressure, Temperature)
#      Uses the given time and location structs with the given pressure and
#      temperature to determine sun positions. Pressure must be given in
#      Pascals, and temperature must be given in C.
#   [SunAz, SunEl, ApparentSunEl, SolarTime]=pvl_ephemeris(Time, Location, 'temperature', Temperature)
#      Uses the given time and location structs with the given temperature
#      (in C) to determine sun positions. Default pressure is 101325 Pa.
#
# Input Parameters:
#   Time is a struct with the following elements, note that all elements
#     can be column vectors, but they must all be the same length. Time is
#     entered as a struct which must include a value for the offset from
#     UTC. Time is absolutely specified by the date, time, and the number
#     of hours of offset from that date and time to UTC. For example, if
#     you live in Boston, USA, and your data is timestamped in local standard
#     time, your UTC offset should be -5.
#
#   Time.year = The year in the gregorian calendar
#   Time.month = the month of the year (January = 1 to December = 12)
#   Time.day = the day of the month
#   Time.hour = the hour of the day
#   Time.minute = the minute of the hour
#   Time.second = the second of the minute
#   Time.UTCOffset = the UTC offset code, using the convention
#     that a positive UTC offset is for time zones east of the prime meridian
#     (e.g. EST = -5)
#
#   Location is a struct with the following elements
#   Location.latitude = vector or scalar latitude in decimal degrees (positive is
#     northern hemisphere)
#   Location.longitude = vector or scalar longitude in decimal degrees (positive is
#     east of prime meridian)
#   Location.altitude = an optional component of the Location struct, not
#     used in the ephemeris code directly, but it may be used to calculate
#     standard site pressure (see pvl_alt2pres function)
#
# Output Parameters:
#   SunAz = Azimuth of the sun in decimal degrees from North. 0 = North to 270 = West
#   SunEl = Actual elevation (not accounting for refraction)of the sun
#     in decimal degrees, 0 = on horizon. The complement of the True Zenith
#     Angle.
#   ApparentSunEl = Apparent sun elevation accounting for atmospheric
#     refraction. This is the complement of the Apparent Zenith Angle.
#   SolarTime = solar time in decimal hours (solar noon is 12.00).
#
# References
#   Grover Hughes' class and related class materials on Engineering
#   Astronomy at Sandia National Laboratories, 1985.
#
# See also PVL_MAKETIMESTRUCT PVL_MAKELOCATIONSTRUCT PVL_ALT2PRES
#          PVL_GETAOI PVL_SPA

# p = inputParser;
# p.addRequired('Time',@isstruct);
# p.addRequired('Location',@isstruct);
# p.addOptional('pressure',101325, @(x) all(isvector(x) & isnumeric(x) & x>=0));
# p.addOptional('temperature',12, @(x) all(isvector(x) & isnumeric(x) & x>=-273.15));
# p.parse(Time, Location, varargin{:});

import numpy as np
clear('all')
lat = - 22.9
lon = - 43.1
#Latitude = p.Results.Location.latitude(:);
Latitude = lat
# the inversion of longitude is due to the fact that this code was
# originally written for the convention that positive longitude were for
# locations west of the prime meridian. However, the correct convention (as
# of 2009) is to use negative longitudes for locations west of the prime
# meridian. Therefore, the user should input longitude values under the
# correct convention (e.g. Albuquerque is at -106 longitude), but it needs
# to be inverted for use in the code.
Longitude = - 1 * lon
#Solar time per month
Tm,Tx,sunrise_min,sunset_min,hora = sol_por_dia(lon,lat)
Year = 2019
Month = 1
Day = 15
Hour = 0
Minute = 0
Second = 0
# the inversion of UTC offset is due to the fact that this code was
# originally written for the convention that positive offset values were
# positive for locations west of the prime merdian. However, the correct
# convention (as of 2009) is to use negative offset codes for locaitons
# west of the prime merdian. Therefore, the user should input offset values
# under the correct convention (e.g. EST = -5), but it needs to be inverted
# for use in the following code.
TZone = - 1 * (- 3)
pressure = 1013
temperature = 23
temperature = temperature + 273.15
DecHours = 12
RadtoDeg = 180 / np.pi
DegtoRad = np.pi / 180
Abber = 20 / 3600
LatR = Latitude * DegtoRad
Yr = Year - 1900
YrBegin = 365 * Yr + int(np.floor((Yr - 1) / 4)) - 0.5
# calculating day mean per month
mon = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
sumM = 0
for i in np.arange(1,12+1).reshape(-1):
    for j in np.arange(np.arange(1,len(DecHours(,,1))+1)):
        n[i] = int(np.floor(mon(1,i) / 2)) + sumM
        sumM = sum(mon(np.arange(1,i+1)))
        DayOfYear[i] = n(i)
        UnivDate[i] = DayOfYear(i) + int(np.floor((DecHours + TZone) / 24))
        UnivHr = np.mod((DecHours + TZone),24)
        Ezero[i] = YrBegin + UnivDate(i)
        T[i] = Ezero(i) / 36525
        GMST0[i] = 6 / 24 + 38 / 1440 + (45.836 + 8640184.542 * T(i) + 0.0929 * T(i) ** 2) / 86400
        GMST0[i] = 360 * (GMST0(i) - int(np.floor(GMST0(i))))
        GMSTi[i] = np.mod(GMST0(i) + 360 * (1.0027379093 * UnivHr / 24),360)
        LocAST[i] = np.mod((360 + GMSTi(i) - Longitude),360)
        EpochDate[i] = Ezero(i) + UnivHr / 24
        T1[i] = EpochDate(i) / 36525
        ObliquityR[i] = DegtoRad * (23.452294 - 0.0130125 * T1(i) - 1.64e-06 * T1(i) ** 2 + 5.03e-07 * (i) ** 3)
        MlPerigee[i] = 281.22083 + 4.70684e-05 * EpochDate(i) + 0.000453 * T1(i) ** 2 + 3e-06 * T1(i) ** 3
        MeanAnom[i] = np.mod((358.47583 + 0.985600267 * EpochDate(i) - 0.00015 * T1(i) ** 2 - 3e-06 * T1(i) ** 3),360)
        Eccen[i] = 0.01675104 - 4.18e-05 * T1(i) - 1.26e-07 * T1(i) ** 2
        EccenAnom[i] = MeanAnom(i)
        E[i] = 0
        while np.amax(np.abs(EccenAnom(i) - E(i))) > 0.001:

            E[i] = EccenAnom(i)
            EccenAnom[i] = MeanAnom(i) + np.multiply(np.multiply(RadtoDeg,Eccen(i)),np.sin(np.multiply(DegtoRad,E(i))))

        TrueAnom[i] = 2 * np.mod(RadtoDeg * atan2(np.multiply(((1 + Eccen(i)) / (1 - Eccen(i))) ** 0.5,np.tan(DegtoRad * EccenAnom(i) / 2)),1),360)
        EcLon[i] = np.mod(MlPerigee(i) + TrueAnom(i),360) - Abber
        EcLonR[i] = DegtoRad * EcLon(i)
        DecR[i] = np.arcsin(np.multiply(np.sin(ObliquityR(i)),np.sin(EcLonR(i))))
        Dec[i] = RadtoDeg * DecR(i)
        RtAscen[i] = RadtoDeg * atan2(np.multiply(np.cos(ObliquityR(i)),(np.sin(EcLonR(i)))),np.cos(EcLonR(i)))
        HrAngle[i] = LocAST(i) - RtAscen(i)
        HrAngleR[i] = np.multiply(DegtoRad,HrAngle(i))
        # HrAngle(i)=(15.*Tm(i)) - 180
# HrAngleR(i) = DegtoRad .* HrAngle(i)
        HrAngle[i] = HrAngle(i) - (np.multiply(np.multiply(360,np.sign(HrAngle(i))),(np.abs(HrAngle(i)) > 180)))
        SunAz[i] = np.multiply(RadtoDeg,atan2(- 1 * np.sin(HrAngleR(i)),np.multiply(np.cos(LatR),np.tan(DecR(i))) - np.multiply(np.sin(LatR),np.cos(HrAngleR(i)))))
        SunAz[i] = SunAz(i) + (SunAz(i) < 0) * 360
        SunEl[i] = asind(np.multiply(np.multiply(np.cos(LatR),np.cos(DecR(i))),np.cos(HrAngleR(i))) + np.multiply(np.sin(LatR),np.sin(DecR(i))))
        SolarTime[i] = (180 + HrAngle(i)) / 15
        # Calculate the refraction of the sun until the actual center of the sun is
# 1 degree below the horizon.
        TanEl[i] = np.tan(DegtoRad * SunEl(i))
        Refract[i] = np.zeros((len(SunEl(i)),1)) + (np.multiply(and_(SunEl(i) > 5,SunEl(i) <= 85),(58.1 / TanEl(i) - 0.07 / (TanEl(i) ** 3) + 8.6e-05 / (TanEl(i) ** 5)))) + (np.multiply(and_(SunEl(i) > - 0.575,SunEl(i) <= 5),(np.multiply(SunEl(i),(- 518.2 + np.multiply(SunEl(i),(103.4 + np.multiply(SunEl(i),(- 12.79 + np.multiply(SunEl(i),0.711))))))) + 1735))) + (np.multiply(and_(SunEl(i) > - 1,SunEl(i) <= - 0.575),((- 20.774 / TanEl(i)))))
        Refract[i] = np.multiply(np.multiply(Refract(i),(283 / (273 + temperature))),pressure) / 101325 / 3600
        # Generate apparent sun elevation including refraction
        ApparentSunEl[i] = SunEl(i) + Refract(i)
        sunZen[j,i] = (90 - SunEl(j,i))
    i = i + 1
