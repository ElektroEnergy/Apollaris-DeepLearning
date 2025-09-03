import numpy as np
    
def pvl_perez(SurfTilt = None,SurfAz = None,DHI = None,DNI = None,HExtra = None,SunZen = None,SunAz = None,AM = None,model = None): 
    # PVL_PEREZ Determine diffuse irradiance from the sky on a tilted surface using the Perez model
    
    # Syntax
#   [SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor] = pvl_perez(SurfTilt, SurfAz, DHI, DNI, HExtra, SunZen, SunAz, AM)
#   [SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor] = pvl_perez(SurfTilt, SurfAz, DHI, DNI, HExtra, SunZen, SunAz, AM, model)
    
    # Description
#   The Perez model [3] determines the sky diffuse irradiance on a tilted
#   surface using the surface tilt angle, surface azimuth angle, diffuse
#   horizontal irradiance, direct normal irradiance, extraterrestrial
#   irradiance, sun zenith angle, sun azimuth angle, and relative (not
#   pressure-corrected) airmass. An optional selector may be used to specify
#   any of Perez's model coefficient sets.
    
    # Inputs:
#   SurfTilt - a scalar or vector of surface tilt angles in decimal degrees.
#     If SurfTilt is a vector it must be of the same size as all other vector
#     inputs. SurfTilt must be >=0 and <=180. The tilt angle is defined as
#     degrees from horizontal (e.g. surface facing up = 0, surface facing
#     horizon = 90)
#   SurfAz - a scalar or vector of surface azimuth angles in decimal degrees.
#     If SurfAz is a vector it must be of the same size as all other vector
#     inputs. SurfAz must be >=0 and <=360. The Azimuth convention is defined
#     as degrees east of north (e.g. North = 0, East = 90, West = 270).
#   DHI - a scalar or vector of diffuse horizontal irradiance in W/m^2. If DHI
#     is a vector it must be of the same size as all other vector inputs.
#     DHI must be >=0.
#   DNI - a scalar or vector of direct normal irradiance in W/m^2. If DNI
#     is a vector it must be of the same size as all other vector inputs.
#     DNI must be >=0.
#   HExtra - a scalar or vector of extraterrestrial normal irradiance in
#     W/m^2. If HExtra is a vector it must be of the same size as
#     all other vector inputs. HExtra must be >=0.
#   SunZen - a scalar or vector of apparent (refraction-corrected) zenith
#     angles in decimal degrees. If SunZen is a vector it must be of the
#     same size as all other vector inputs. SunZen must be >=0 and <=180.
#   SunAz - a scalar or vector of sun azimuth angles in decimal degrees.
#     If SunAz is a vector it must be of the same size as all other vector
#     inputs. SunAz must be >=0 and <=360. The Azimuth convention is defined
#     as degrees east of north (e.g. North = 0, East = 90, West = 270).
#   AM - a scalar or vector of relative (not pressure-corrected) airmass
#     values. If AM is a vector it must be of the same size as all other
#     vector inputs. AM must be >=0 (careful using the 1/sec(z) model of AM
#     generation).
#   model - a character string which selects the desired set of Perez
#     coefficients. If model is not provided as an input, the default,
#     '1990' will be used.
#     All possible model selections are:
#       '1990', 'allsitescomposite1990' (same as '1990'),
#       'allsitescomposite1988', 'sandiacomposite1988',
#       'usacomposite1988', 'france1988', 'phoenix1988',
#       'elmonte1988', 'osage1988', 'albuquerque1988',
#       'capecanaveral1988', or 'albany1988'
    
    # Output:
#   SkyDiffuse - the total diffuse component of the solar radiation on an
#     arbitrarily tilted surface defined by the Perez model as given in
#     reference [3].
#     SkyDiffuse is the diffuse component ONLY and does not include the ground
#     reflected irradiance or the irradiance due to the beam.
#     SkyDiffuse is a column vector vector with a number of elements equal to
#     the input vector(s).
#   SkyDiffuse_Iso - the isotropic diffuse component of the solar radiation on an
#     arbitrarily tilted surface defined by the Perez model as given in
#     reference [3].
#     SkyDiffuse_Iso is the isotropic diffuse component ONLY and does not include the ground
#     reflected irradiance or the irradiance due to the beam.
#     SkyDiffuse is a column vector vector with a number of elements equal to
#     the input vector(s).
#   SkyDiffuse_Cir - the circumsolar diffuse component of the solar radiation on an
#     arbitrarily tilted surface defined by the Perez model as given in
#     reference [3].
#     SkyDiffuse_Cir is the circumsolar diffuse component ONLY and does not include the ground
#     reflected irradiance or the irradiance due to the beam.
#     SkyDiffuse is a column vector vector with a number of elements equal to
#     the input vector(s).
#   SkyDiffuse_Hor - the horizon brightening diffuse component of the solar radiation on an
#     arbitrarily tilted surface defined by the Perez model as given in
#     reference [3].
#     SkyDiffuse_Cir is the horizon brightening diffuse component ONLY and does not include the ground
#     reflected irradiance or the irradiance due to the beam.
#     SkyDiffuse is a column vector vector with a number of elements equal to
#     the input vector(s).
    
    # References
#   [1] Loutzenhiser P.G. et. al., 2007. Empirical validation of models to compute
#   solar irradiance on inclined surfaces for building energy simulation,
#   Solar Energy vol. 81. pp. 254-267.
#   [2] Perez, R., Seals, R., Ineichen, P., Stewart, R., Menicucci, D., 1987. A new
#   simplified version of the Perez diffuse irradiance model for tilted
#   surfaces. Solar Energy 39 (3), 221–232.
#   [3] Perez, R., Ineichen, P., Seals, R., Michalsky, J., Stewart, R., 1990.
#   Modeling daylight availability and irradiance components from direct
#   and global irradiance. Solar Energy 44 (5), 271–289.
#   [4] Perez, R. et. al 1988. The Development and Verification of the
#   Perez Diffuse Radiation Model,.SAND88-7030, Sandia National
#   Laboratories.
    
    # See also PVL_EPHEMERIS   PVL_EXTRARADIATION   PVL_ISOTROPICSKY
#       PVL_HAYDAVIES1980   PVL_REINDL1990   PVL_KLUCHER1979   PVL_KINGDIFFUSE
#       PVL_RELATIVEAIRMASS
    
    # Notes: pvl_perez original code by Sandia National Laboratories. Extension
# of pvl_perez to output components of sky diffuse irradiance, i.e.,
# circumsolar, horizon brightening and rest-of-sky, contributed by Xingshu
# Sun of Purdue University, 2018.
    
    
    # p=inputParser;
# p.addRequired('SurfTilt', @(x) (isnumeric(x) && all(x<=180) && all(x>=0) && isvector(x)))
# p.addRequired('SurfAz', @(x) isnumeric(x) && all(x<=360) && all(x>=0) && isvector(x))
# p.addRequired('DHI', @(x) (isnumeric(x) && isvector(x) && all((x>=0) | isnan(x))))
# p.addRequired('DNI', @(x) isnumeric(x) && isvector(x) && all((x>=0) | isnan(x)))
# p.addRequired('HExtra', @(x) isnumeric(x) && isvector(x) && all((x>=0) | isnan(x)))
# p.addRequired('SunZen', @(x) isnumeric(x) && all(x<=180) && all((x>=0) | isnan(x)) && isvector(x))
# p.addRequired('SunAz', @(x) (isnumeric(x) && all(x<=360) && all((x>=0) | isnan(x)) && isvector(x)))
# p.addRequired('AM', @(x) (all(((isnumeric(x) & x>=0) | isnan(x))) & isvector(x)))
# p.addOptional('model', '1990', @(x) ischar(x))
# p.parse(SurfTilt, SurfAz, DHI, DNI, HExtra, SunZen, SunAz, AM, model)
    
    # model = p.Results.model
# SurfTilt = p.Results.SurfTilt(:)
# SurfAz = p.Results.SurfAz(:)
# DHI = p.Results.DHI(:)
# DNI = p.Results.DNI(:)
# HExtra = p.Results.HExtra(:)
# SunZen = p.Results.SunZen(:)
# SunAz = p.Results.SunAz(:)
# AM = p.Results.AM(:)
    
    VectorSizes = np.array([np.asarray(SurfTilt).size,np.asarray(SurfAz).size,np.asarray(DHI).size,np.asarray(DNI).size,np.asarray(HExtra).size,np.asarray(SunZen).size,np.asarray(SunAz).size,np.asarray(AM).size])
    MaxVectorSize = np.amax(VectorSizes)
    if not_(np.all(np.logical_or((VectorSizes == MaxVectorSize),(VectorSizes == 1)))):
        raise Exception(np.array(['Input parameters SurfTilt, SurfAz, DHI, DNI, HExtra, SunZen, SunAz, and AM',' must either be scalars or vectors of the same length.']))
    
    # If any input variable is not a scalar, then make any scalar input values
# into a column vector of the correct size.
    if MaxVectorSize > 1:
        if VectorSizes(1) < MaxVectorSize:
            SurfTilt = np.multiply(SurfTilt,np.ones((MaxVectorSize,1)))
        if VectorSizes(2) < MaxVectorSize:
            SurfAz = np.multiply(SurfAz,np.ones((MaxVectorSize,1)))
        if VectorSizes(3) < MaxVectorSize:
            DHI = np.multiply(DHI,np.ones((MaxVectorSize,1)))
        if VectorSizes(4) < MaxVectorSize:
            DNI = np.multiply(DNI,np.ones((MaxVectorSize,1)))
        if VectorSizes(5) < MaxVectorSize:
            HExtra = np.multiply(HExtra,np.ones((MaxVectorSize,1)))
        if VectorSizes(6) < MaxVectorSize:
            SunZen = np.multiply(SunZen,np.ones((MaxVectorSize,1)))
        if VectorSizes(7) < MaxVectorSize:
            SunAz = np.multiply(SunAz,np.ones((MaxVectorSize,1)))
        if VectorSizes(8) < MaxVectorSize:
            AM = np.multiply(AM,np.ones((MaxVectorSize,1)))
    
    kappa = 1.041
    
    z = (SunZen * np.pi / 180)
    
    e = np.zeros((len(DHI),1))
    Dhfilter = DHI > 0
    e[Dhfilter] = ((DHI(Dhfilter) + DNI(Dhfilter)) / DHI(Dhfilter) + np.multiply(kappa,z(Dhfilter) ** 3)) / (1 + np.multiply(kappa,z(Dhfilter) ** 3))
    ebin = np.zeros((np.asarray(DHI).size,1))
    # Select which bin e falls into
    ebin[np.logical_and[[e >= 1],[e < 1.065]]] = 1
    ebin[np.logical_and[[e >= 1.065],[e < 1.23]]] = 2
    ebin[np.logical_and[[e >= 1.23],[e < 1.5]]] = 3
    ebin[np.logical_and[[e >= 1.5],[e < 1.95]]] = 4
    ebin[np.logical_and[[e >= 1.95],[e < 2.8]]] = 5
    ebin[np.logical_and[[e >= 2.8],[e < 4.5]]] = 6
    ebin[np.logical_and[[e >= 4.5],[e < 6.2]]] = 7
    ebin[e >= 6.2] = 8
    # This is added because in cases where the sun is below the horizon
# (SunZen > 90) but there is still diffuse horizontal light (DHI>0), it is
# possible that the airmass (AM) could be NaN, which messes up later
# calculations. Instead, if the sun is down, and there is still DHI, we set
# the airmass to the airmass value on the horizon (approximately 37-38).
    AM[SunZen >= np.logical_and[90,DHI] > 0] = 37
    del_ = np.multiply(DHI,AM) / HExtra
    ebinfilter = ebin > 0
    # The various possible sets of Perez coefficients are contained
# in a subfunction to clean up the code.
    F1c,F2c = GetPerezCoefficients(model)
    F11 = np.zeros((np.asarray(DHI).size,1))
    F12 = np.zeros((np.asarray(DHI).size,1))
    F13 = np.zeros((np.asarray(DHI).size,1))
    F11[ebinfilter] = F1c(ebin(ebinfilter),1)
    F12[ebinfilter] = F1c(ebin(ebinfilter),2)
    F13[ebinfilter] = F1c(ebin(ebinfilter),3)
    F1 = np.zeros((np.asarray(DHI).size,1))
    F1[ebinfilter] = F11(ebinfilter) + np.multiply(F12(ebinfilter),del_(ebinfilter)) + np.multiply(F13(ebinfilter),z(ebinfilter))
    F1[F1 < 0] = 0
    F21 = np.zeros((np.asarray(DHI).size,1))
    F22 = np.zeros((np.asarray(DHI).size,1))
    F23 = np.zeros((np.asarray(DHI).size,1))
    F21[ebinfilter] = F2c(ebin(ebinfilter),1)
    F22[ebinfilter] = F2c(ebin(ebinfilter),2)
    F23[ebinfilter] = F2c(ebin(ebinfilter),3)
    F2 = np.zeros((len(DHI),1))
    F2[ebinfilter] = F21(ebinfilter) + np.multiply(F22(ebinfilter),del_(ebinfilter)) + np.multiply(F23(ebinfilter),z(ebinfilter))
    
    # Dec 2012: A bug was identified by Rob Andrews (Queens University) in this equation in PV_LIB
# Version 1.0.  Fixed in Version 1.1.
    A = np.multiply(np.cos(np.pi/180*SurfTilt),np.cos(np.pi/180*SunZen)) + np.multiply(np.multiply(np.sin(np.pi/180*SurfTilt),np.sin(np.pi/180*SunZen)),np.cos(np.pi/180*SunAz - SurfAz))
    A[A < 0] = 0
    B = np.cos(np.pi/180*SunZen)
    B[B < np.cos[np.pi/180*85]] = np.cos(np.pi/180*85)
    #Calculate Diffuse POA from sky dome
    SkyDiffuse = np.zeros((len(DHI),1))
    # Dec 2012: A bug was identified by Rob Andrews (Queens University) in this equation in PV_LIB
# Version 1.0.  Fixed in Version 1.1.
    SkyDiffuse[ebinfilter] = np.multiply(DHI(ebinfilter),(np.multiply(np.multiply(0.5,(1 - F1(ebinfilter))),(1 + np.cos(np.pi/180*SurfTilt(ebinfilter)))) + np.multiply(F1(ebinfilter),A(ebinfilter)) / B(ebinfilter) + np.multiply(F2(ebinfilter),np.sin(np.pi/180*SurfTilt(ebinfilter)))))
    SkyDiffuse_Iso[ebinfilter] = np.multiply(DHI(ebinfilter),(np.multiply(np.multiply(0.5,(1 - F1(ebinfilter))),(1 + np.cos(np.pi/180*SurfTilt(ebinfilter))))))
    SkyDiffuse_Cir[ebinfilter] = np.multiply(np.multiply(DHI(ebinfilter),F1(ebinfilter)),A(ebinfilter)) / B(ebinfilter)
    SkyDiffuse_Hor[ebinfilter] = np.multiply(np.multiply(DHI(ebinfilter),F2(ebinfilter)),np.sin(np.pi/180*SurfTilt(ebinfilter)))
    # SkyDiffuse(ebinfilter) = DHI(ebinfilter).* 0.5.* (1-F1(ebinfilter)).*(1+cosd(SurfTilt)) +...
#     F1(ebinfilter) .* A(ebinfilter)./ B(ebinfilter) + F2(ebinfilter).* sind(SurfTilt);
    con = (SkyDiffuse <= 0)
    SkyDiffuse[con] = 0
    SkyDiffuse_Iso[con] = 0
    SkyDiffuse_Cir[con] = 0
    SkyDiffuse_Hor[con] = 0
    SkyDiffuse = SkyDiffuse
    SkyDiffuse_Iso = SkyDiffuse_Iso
    SkyDiffuse_Cir = SkyDiffuse_Cir
    SkyDiffuse_Hor = SkyDiffuse_Hor
    return SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor
    
    
def GetPerezCoefficients(perezmodel = None): 
    if np.array(['allsitescomposite1990']) == perezmodel.lower():
        PerezCoeffs = np.array([- 0.008,0.588,- 0.062,- 0.06,0.072,- 0.022,0.13,0.683,- 0.151,- 0.019,0.066,- 0.029,0.33,0.487,- 0.221,0.055,- 0.064,- 0.026,0.568,0.187,- 0.295,0.109,- 0.152,- 0.014,0.873,- 0.392,- 0.362,0.226,- 0.462,0.001,1.132,- 1.237,- 0.412,0.288,- 0.823,0.056,1.06,- 1.6,- 0.359,0.264,- 1.127,0.131,0.678,- 0.327,- 0.25,0.156,- 1.377,0.251])
    else:
        if np.array(['allsitescomposite1988']) == perezmodel.lower():
            PerezCoeffs = np.array([- 0.018,0.705,- 0.071,- 0.058,0.102,- 0.026,0.191,0.645,- 0.171,0.012,0.009,- 0.027,0.44,0.378,- 0.256,0.087,- 0.104,- 0.025,0.756,- 0.121,- 0.346,0.179,- 0.321,- 0.008,0.996,- 0.645,- 0.405,0.26,- 0.59,0.017,1.098,- 1.29,- 0.393,0.269,- 0.832,0.075,0.973,- 1.135,- 0.378,0.124,- 0.258,0.149,0.689,- 0.412,- 0.273,0.199,- 1.675,0.237])
        else:
            if np.array(['sandiacomposite1988']) == perezmodel.lower():
                PerezCoeffs = np.array([- 0.196,1.084,- 0.006,- 0.114,0.18,- 0.019,0.236,0.519,- 0.18,- 0.011,0.02,- 0.038,0.454,0.321,- 0.255,0.072,- 0.098,- 0.046,0.866,- 0.381,- 0.375,0.203,- 0.403,- 0.049,1.026,- 0.711,- 0.426,0.273,- 0.602,- 0.061,0.978,- 0.986,- 0.35,0.28,- 0.915,- 0.024,0.748,- 0.913,- 0.236,0.173,- 1.045,0.065,0.318,- 0.757,0.103,0.062,- 1.698,0.236])
            else:
                if np.array(['usacomposite1988']) == perezmodel.lower():
                    PerezCoeffs = np.array([- 0.034,0.671,- 0.059,- 0.059,0.086,- 0.028,0.255,0.474,- 0.191,0.018,- 0.014,- 0.033,0.427,0.349,- 0.245,0.093,- 0.121,- 0.039,0.756,- 0.213,- 0.328,0.175,- 0.304,- 0.027,1.02,- 0.857,- 0.385,0.28,- 0.638,- 0.019,1.05,- 1.344,- 0.348,0.28,- 0.893,0.037,0.974,- 1.507,- 0.37,0.154,- 0.568,0.109,0.744,- 1.817,- 0.256,0.246,- 2.618,0.23])
                else:
                    if np.array(['france1988']) == perezmodel.lower():
                        PerezCoeffs = np.array([0.013,0.764,- 0.1,- 0.058,0.127,- 0.023,0.095,0.92,- 0.152,0,0.051,- 0.02,0.464,0.421,- 0.28,0.064,- 0.051,- 0.002,0.759,- 0.009,- 0.373,0.201,- 0.382,0.01,0.976,- 0.4,- 0.436,0.271,- 0.638,0.051,1.176,- 1.254,- 0.462,0.295,- 0.975,0.129,1.106,- 1.563,- 0.398,0.301,- 1.442,0.212,0.934,- 1.501,- 0.271,0.42,- 2.917,0.249])
                    else:
                        if np.array(['phoenix1988']) == perezmodel.lower():
                            PerezCoeffs = np.array([- 0.003,0.728,- 0.097,- 0.075,0.142,- 0.043,0.279,0.354,- 0.176,0.03,- 0.055,- 0.054,0.469,0.168,- 0.246,0.048,- 0.042,- 0.057,0.856,- 0.519,- 0.34,0.176,- 0.38,- 0.031,0.941,- 0.625,- 0.391,0.188,- 0.36,- 0.049,1.056,- 1.134,- 0.41,0.281,- 0.794,- 0.065,0.901,- 2.139,- 0.269,0.118,- 0.665,0.046,0.107,0.481,0.143,- 0.111,- 0.137,0.234])
                        else:
                            if np.array(['elmonte1988']) == perezmodel.lower():
                                PerezCoeffs = np.array([0.027,0.701,- 0.119,- 0.058,0.107,- 0.06,0.181,0.671,- 0.178,- 0.079,0.194,- 0.035,0.476,0.407,- 0.288,0.054,- 0.032,- 0.055,0.875,- 0.218,- 0.403,0.187,- 0.309,- 0.061,1.166,- 1.014,- 0.454,0.211,- 0.41,- 0.044,1.143,- 2.064,- 0.291,0.097,- 0.319,0.053,1.094,- 2.632,- 0.259,0.029,- 0.422,0.147,0.155,1.723,0.163,- 0.131,- 0.019,0.277])
                            else:
                                if np.array(['osage1988']) == perezmodel.lower():
                                    PerezCoeffs = np.array([- 0.353,1.474,0.057,- 0.175,0.312,0.009,0.363,0.218,- 0.212,0.019,- 0.034,- 0.059,- 0.031,1.262,- 0.084,- 0.082,0.231,- 0.017,0.691,0.039,- 0.295,0.091,- 0.131,- 0.035,1.182,- 1.35,- 0.321,0.408,- 0.985,- 0.088,0.764,0.019,- 0.203,0.217,- 0.294,- 0.103,0.219,1.412,0.244,0.471,- 2.988,0.034,3.578,22.231,- 10.745,2.426,4.892,- 5.687])
                                else:
                                    if np.array(['albuquerque1988']) == perezmodel.lower():
                                        PerezCoeffs = np.array([0.034,0.501,- 0.094,- 0.063,0.106,- 0.044,0.229,0.467,- 0.156,- 0.005,- 0.019,- 0.023,0.486,0.241,- 0.253,0.053,- 0.064,- 0.022,0.874,- 0.393,- 0.397,0.181,- 0.327,- 0.037,1.193,- 1.296,- 0.501,0.281,- 0.656,- 0.045,1.056,- 1.758,- 0.374,0.226,- 0.759,0.034,0.901,- 4.783,- 0.109,0.063,- 0.97,0.196,0.851,- 7.055,- 0.053,0.06,- 2.833,0.33])
                                    else:
                                        if np.array(['capecanaveral1988']) == perezmodel.lower():
                                            PerezCoeffs = np.array([0.075,0.533,- 0.124,- 0.067,0.042,- 0.02,0.295,0.497,- 0.218,- 0.008,0.003,- 0.029,0.514,0.081,- 0.261,0.075,- 0.16,- 0.029,0.747,- 0.329,- 0.325,0.181,- 0.416,- 0.03,0.901,- 0.883,- 0.297,0.178,- 0.489,0.008,0.591,- 0.044,- 0.116,0.235,- 0.999,0.098,0.537,- 2.402,0.32,0.169,- 1.971,0.31,- 0.805,4.546,1.072,- 0.258,- 0.95,0.753])
                                        else:
                                            if np.array(['albany1988']) == perezmodel.lower():
                                                PerezCoeffs = np.array([0.012,0.554,- 0.076,- 0.052,0.084,- 0.029,0.267,0.437,- 0.194,0.016,0.022,- 0.036,0.42,0.336,- 0.237,0.074,- 0.052,- 0.032,0.638,- 0.001,- 0.281,0.138,- 0.189,- 0.012,1.019,- 1.027,- 0.342,0.271,- 0.628,0.014,1.149,- 1.94,- 0.331,0.322,- 1.097,0.08,1.434,- 3.994,- 0.492,0.453,- 2.376,0.117,1.007,- 2.292,- 0.482,0.39,- 3.368,0.229])
                                            else:
                                                raise Exception('Incorrect coefficient set name entered for Perez radiation model')
    
    F1coeffs = PerezCoeffs(:,np.arange(1,3+1))
    F2coeffs = PerezCoeffs(:,np.arange(4,6+1))
    return F1coeffs,F2coeffs
    
    return SkyDiffuse,SkyDiffuse_Iso,SkyDiffuse_Cir,SkyDiffuse_Hor