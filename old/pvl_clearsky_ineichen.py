import numpy as np
    
def pvl_clearsky_ineichen(n = None,hora = None,lat = None,lon = None,alt = None,sunZen = None,AMa = None): 
    # PVL_CLEARSKY_INEICHEN Determine clear sky GHI, DNI, and DHI from Ineichen/Perez model
    
    # Syntax
#   [ClearSkyGHI, ClearSkyDNI, ClearSkyDHI]= pvl_clearsky_ineichen(Time, Location)
#   [ClearSkyGHI, ClearSkyDNI, ClearSkyDHI]= pvl_clearsky_ineichen(Time, Location, LinkeTurbidityInput)
    
    # Description
#   Implements the Ineichen and Perez clear sky model for global horizontal
#   irradiance (GHI), direct normal irradiance (DNI), and calculates
#   the clear-sky diffuse horizontal (DHI) component as the difference
#   between GHI and DNI*cos(zenith) as presented in [1, 2]. A report on clear
#   sky models found the Ineichen/Perez model to have excellent performance
#   with a minimal input data set [3]. Default values for Linke turbidity
#   provided by SoDa [4, 5].
    
    # Input Parameters:
#   Time - a struct with the following elements, note that all elements
#       can be column vectors, but they must all be the same length.
#       pvl_maketimestruct may be used to generate the Time input.
#   Time.year = The year in the gregorian calendar
#   Time.month = the month of the year (January = 1 to December = 12)
#   Time.day = the day of the month
#   Time.hour = the hour of the day
#   Time.minute = the minute of the hour
#   Time.second = the second of the minute
#   Time.UTCOffset = the UTC offset code, using the convention
#      that a positive UTC offset is for time zones east of the prime meridian
#      (e.g. EST = -5)
    
    #   Location - a struct with the following elements, note that all
#      elements may scalars or column vectors, but they must all be the same
#      length (e.g. Time.hour(i) must correspond to Location.latitude(i)).
#      pvl_makelocationstruct may be used to make scalar (stationary)
#      location files.
#   Location.latitude = vector or scalar latitude in decimal degrees (positive is
#      northern hemisphere)
#   Location.longitude = vector or scalar longitude in decimal degrees (positive is
#      east of prime meridian)
#   Location.altitude = vector or scalar height above sea level in meters.
#      While altitude is optional in many uses, it is required in this
#      model implmentation.
    
    #   LinkeTurbidityInput - An optional input to provide your own Linke
#      turbidity. If this input is omitted, the default Linke turbidity
#      maps will be used. LinkeTurbidityInput may be a scalar or column
#      vector of Linke turbidities. If scalar is provided, the same
#      turbidity will be used for all time/location sets. If a vector is
#      provided, it must be of the same size as any time/location vectors
#      and each element of the vector corresponds to any time and location
#      elements.
    
    # Output:
#   ClearSkyGHI - the modeled global horizonal irradiance in W/m^2 provided
#      by the Ineichen clear-sky model.
#   ClearSkyDNI - the modeled direct normal irradiance in W/m^2 provided
#      by the Ineichen clear-sky model.
#   ClearSkyDHI - the calculated diffuse horizonal irradiance in W/m^2
#      provided by the Ineichen clear-sky model.
    
    # Notes:
#    This implementation of the Ineichen model requires a number of other
#    PV_LIB functions including pvl_ephemeris, pvl_date2doy,
#    pvl_extraradiation, pvl_absoluteairmass, pvl_relativeairmass, and
#    pvl_alt2pres. It also requires the file "LinkeTurbidities.mat" to be
#    in a subfolder named "/Required Data". If you are using pvl_ineichen
#    in a loop, it may be faster to load LinkeTurbidities.mat outside of
#    the loop and feed it into pvl_ineichen as a variable, rather than
#    having pvl_ineichen open the file each time it is called (or utilize
#    column vectors of time/location instead of a loop).
    
    #    Initial implementation of this algorithm by Matthew Reno.
    
    # Sources:
    
    # [1] P. Ineichen and R. Perez, "A New airmass independent formulation for
#     the Linke turbidity coefficient", Solar Energy, vol 73, pp. 151-157, 2002.
    
    # [2] R. Perez et. al., "A New Operational Model for Satellite-Derived
#     Irradiances: Description and Validation", Solar Energy, vol 73, pp.
#     307-317, 2002.
    
    # [3] M. Reno, C. Hansen, and J. Stein, "Global Horizontal Irradiance Clear
#     Sky Models: Implementation and Analysis", Sandia National
#     Laboratories, SAND2012-2389, 2012.
    
    # [4] http://www.soda-is.com/eng/services/climat_free_eng.php#c5 (obtained
#     July 17, 2012).
    
    # [5] J. Remund, et. al., "Worldwide Linke Turbidity Information", Proc.
#     ISES Solar World Congress, June 2003. Goteborg, Sweden.
    
    
    # See also
#   PVL_MAKETIMESTRUCT    PVL_MAKELOCATIONSTRUCT   PVL_EPHEMERIS
#   PVL_CLEARSKY_HAURWITZ
    Time.minute = 0
    Time.second = 0
    Time.UTCOffset = - 3
    Time.year = 2019
    Location.latitude = lat
    Location.longitude = lon
    Location.altitude = alt
    fh1 = np.exp(np.multiply(Location.altitude,(- 1 / 8000)))
    fh2 = np.exp(np.multiply(Location.altitude,(- 1 / 1250)))
    cg1 = (np.multiply(5.09e-05,Location.altitude) + 0.868)
    cg2 = np.multiply(3.92e-05,Location.altitude) + 0.0387
    b = 0.664 + 0.163 / fh1
    Deg2Rad = np.pi / 180
    for i in np.arange(1,12+1).reshape(-1):
        for j in np.arange(np.arange(1,len(hora(,,1))+1)):
            Time.month = i
            Time.day = n(i)
            Time.hour = hora(j)
            # Require the field Location.altitude
            p = inputParser
            p.addRequired('Time',isstruct)
            p.addRequired('Location',lambda x = None: np.all(np.logical_and(isstruct(x),isfield(x,'altitude'))))
            p.addOptional('LinkeTurbidityInput',0,lambda x = None: (isnumeric(x)))
            #p.parse(Time, Location, varargin{:});
            # Determine day of year and extraterrestrial normal radiation for each time
# instant in Time.
            I0[i] = pvl_extraradiation(n(i))
            # Assumptions made in this step:
# 1. Pressure is local standard pressure (per pvl_alt2pres)
# 2. Temperature is 12C (default for pvl_ephemeris)
#[~, ~, ApparentSunElevation, ~]=pvl_ephemeris(Time, Location, pvl_alt2pres(Location.altitude));
            # If LinkeTurbidity was not provided as an input, use the default data set
            defaultchecker = np.array(['LinkeTurbidityInput'])
            #if any(strcmp(defaultchecker,p.UsingDefaults))
# The .mat file 'LinkeTurbidities.mat' contains a single 2160 x 4320 x 12
# matrix of type uint8 called 'LinkeTurbidity'. The rows represent global
# latitudes from 90 to -90 degrees; the columns represent global longitudes
# from -180 to 180; and the depth (third dimension) represents months of
# the year from January (1) to December (12). To determine the Linke
# turbidity for a position on the Earth's surface for a given month do the
# following: LT = LinkeTurbidity(LatitudeIndex, LongitudeIndex, month). To
# do this on a series of locations, utilize a 3 dimensional array
# lookup. Note that the numbers within the matrix are 20 * Linke
# Turbidity, so divide the number from the file by 20 to get the
# turbidity.
#load(['Required Data' filesep 'LinkeTurbidities.mat']);
            scipy.io.loadmat('LinkeTurbidities.mat')
            # Find the appropriate indices for the given Latitude and Longitude
            LatitudeIndex = np.round(LinearlyScale(Location.latitude,90,- 90,1,2160))
            LongitudeIndex = np.round(LinearlyScale(Location.longitude,- 180,180,1,4320))
            # Create the "Lookup3D" function to allow fast vector searches into a 3D
# table. This essentially creates a linear index based on the input indices
# and the size of the array, then indexes into the array.
            Lookup3D = lambda array_ = None,a = None,b = None,c = None: array_((np.multiply((c - 1),np.asarray(array_(:,:,1)).size) + np.multiply((b - 1),np.asarray(array_(:,1,1)).size) + (a - 1) + 1))
            L1[i] = Lookup3D(LinkeTurbidity,LatitudeIndex,LongitudeIndex,Time.month)
            TL[i] = double(L1(i)) / 20
            # else
#     TL = p.Results.LinkeTurbidityInput;
# end
            # Get the absolute airmass assuming standard local pressure (per
# pvl_alt2pres) using Kasten and Young's 1989 formula for airmass.
#AMabsolute = pvl_absoluteairmass(pvl_relativeairmass(ApparentZenith, 'kastenyoung1989'), pvl_alt2pres(Location.altitude));
            # Dan's note on the TL correction: By my reading of the publication on
# pages 151-157, Ineichen and Perez introduce (among other things) three
# things. 1) Beam model in eqn. 8, 2) new turbidity factor in eqn 9 and
# appendix A, and 3) Global horizontal model in eqn. 11. They do NOT appear
# to use the new turbidity factor (item 2 above) in either the beam or GHI
# models. The phrasing of appendix A seems as if there are two separate
# corrections, the first correction is used to correct the beam/GHI models,
# and the second correction is used to correct the revised turibidity
# factor. In my estimation, there is no need to correct the turbidity
# factor used in the beam/GHI models.
            # Create the corrected TL for TL < 2
# TLcorr = TL;
# TLcorr(TL < 2) = TLcorr(TL < 2) - 0.25 .* (2-TLcorr(TL < 2)) .^ (0.5);
            sunZen(j,i)
            #AMa(j,i) = pvl_absoluteairmass(pvl_relativeairmass(sunZen(j,i), 'kastenyoung1989'), pvl_alt2pres(Location.altitude))
# This equation is found in Solar Energy 73, pg 311. It is slightly
# different than the equation given in Solar Energy 73, pg 156. We used the
# equation from pg 311 because of the existence of known typos in the pg 156
# publication (notably the fh2-(TL-1) should be fh2 * (TL-1)).
            ClearSkyGHI[j,i] = np.multiply(np.multiply(np.multiply(np.multiply(cg1,I0(i)),np.cos(np.pi/180*sunZen(j,i))),np.exp(np.multiply(np.multiply(- cg2,AMa(j,i)),(fh1 + np.multiply(fh2,(TL(i) - 1)))))),np.exp(np.multiply(0.01,(AMa(j,i)) ** (1.8))))
            if ClearSkyGHI(j,i) < 0:
                ClearSkyGHI[j,i] = 0
            BncI[i] = np.multiply(np.multiply(b,I0(i)),np.exp(np.multiply(np.multiply(- 0.09,AMa(j,i)),(TL(i) - 1))))
            # Take the minimum of BncI and the equation given
            ClearSkyDNI[j,i] = np.amin(BncI(i),np.multiply(ClearSkyGHI(j,i),(1 - (0.1 - np.multiply(0.2,np.exp(- TL(i)))) / (0.1 + 0.882 / fh1))) / np.cos(np.pi/180*sunZen(j,i)))
            ClearSkyDHI[j,i] = ClearSkyGHI(j,i) - np.multiply(ClearSkyDNI(j,i),np.cos(np.pi/180*sunZen(j,i)))
    
    return ClearSkyGHI,ClearSkyDNI,ClearSkyDHI
    
    
def LinearlyScale(inputmatrix = None,inputmin = None,inputmax = None,outputmin = None,outputmax = None): 
    # OutputMatrix = LinearlyScale(inputmatrix, inputmin, inputmax, outputmin, outputmax)
# Linearly scales the inputmatrix. Maps all values from inputmin to
# outputmin, and from inputmax to outputmax. Linear mapping from one point
# to the other.
    inputrange = inputmax - inputmin
    outputrange = outputmax - outputmin
    OutputMatrix = (inputmatrix - inputmin) * outputrange / inputrange + outputmin
    return OutputMatrix
    
    return ClearSkyGHI,ClearSkyDNI,ClearSkyDHI