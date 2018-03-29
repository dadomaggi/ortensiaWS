#!/usr/bin/python

import datetime
import json
from pyowm import OWM
import pandas as pd
import subprocess
import os

def update_forecast():
    API_key = 'ffdb44d857dd60cbdc3016e1ff59536b'
    owm = OWM(API_key)
    fc = owm.three_hours_forecast('Garlate,it')
    f = fc.get_forecast()
    f_time=[]
    f_temp=[]
    for weather in f:
        f_temp.append(weather.get_temperature(unit='celsius')['temp'])
        f_time.append(weather.get_reference_time('iso'))
        
    df = pd.DataFrame(f_temp,index=f_time,columns=['temp'])
    fname = os.environ["WSDATAPATH"]+"/forecast.csv" 
    df.to_csv(fname, sep=',', decimal='.', index=True)
    subprocess.call('head -n 9 forecast.csv | tail -n 8 >> one_day_forecast.csv',shell=True)
    return

def scale_forecast(time,data):
    return
