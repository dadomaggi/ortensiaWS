#!/usr/bin/python

import datetime
import numpy as np
import os

def secs_from_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    return(now - midnight).seconds

def medfilt (x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.median (y, axis=1)

def fwrite(now,Tmin,Tmax,Tave,T,RH):
    
    fname = os.environ["WWWDATAPATH"]+"/base-index.html"
    base_file = open(fname,"r")
    text = base_file.readlines()
    base_file.close()

    strng = "\t<table>\n"\
    "\t\t<tr><td>time</td><td> {} </td></tr>\n"\
    "\t\t<tr><td>Actual Temp.</td><td> {:4.1f} </td></tr>\n"\
    "\t\t<tr><td>Actual RH</td><td> {:5.2f} </td></tr>\n"\
    "\t\t<tr><td>Tmin</td><td> {:4.1f} </td></tr>\n"\
    "\t\t<tr><td>Tmax</td><td> {:4.1f} </td></tr>\n"\
    "\t\t<tr><td>Tave</td><td> {:4.1f} </td></tr>\n"\
    "\t</table>\n".format(now, T, RH, Tmin, Tmax, Tave )
    
    out_str = ''.join(text[:16])+strng+''.join(text[16:18])
    #print(out_str)

    fname = os.environ["WWWDATAPATH"]+"/index.html"
    out_file = open(fname,"w")
    out_file.write(out_str)
    out_file.close()

    return

