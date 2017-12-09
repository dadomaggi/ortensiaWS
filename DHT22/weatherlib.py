#!/usr/bin/python

import math as mt

#Magnus-Tetens
def dew_point (T, RH):
    a = 17.27 
    b = 237.7
    gamma = mt.log(RH/100) + (a * T)/( b + T)
    return (b*gamma) / (a - gamma)

# da verificare
def humidex (T, RH):
    a = 6.11
    b = 5417.7530
    c = 273.16
    d = 273.15
    e = 0.5555
    dp = dew_point (T, RH)
    alfa = b * (1 / c - 1 / (d + dp))
    return T + d * ( mt.exp(alfa - 10)) 

def heat_index (T, RH):
    if ( T < 27.0 ):
        return None
    if ( RH < 40 ):
        return None
    
    Tf  = T*9.0/5.0 + 32.0

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199
    
    HIf = c1 + c2*Tf + c3*RH + c4*Tf*RH + c5*Tf*Tf + c6*RH*RH + c7*Tf*Tf*RH + c8*Tf*RH*RH + c9*Tf*Tf*RH*RH

    return (HIf - 32.0)*5.0/9.0

    

