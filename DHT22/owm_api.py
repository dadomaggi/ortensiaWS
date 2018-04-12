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
    f_rain=[]


    for weather in f:
        f_temp.append(weather.get_temperature(unit='celsius')['temp'])
        f_time.append(weather.get_reference_time('iso')[:19])
        if weather.get_status()=='Rain':
            f_rain.append(weather.get_rain()['3h'])
        else:
            f_rain.append(0.0)

    #df = pd.DataFrame(f_temp,index=f_time,columns=['temp'])
    d = {'temp': f_temp, 'rain': f_rain, 'time': f_time}
    df = pd.DataFrame(data=d)

    fname = os.environ["WSDATAPATH"]+"/forecast.csv" 
    df.to_csv(fname, sep=',', decimal='.', index=False)
    subprocess.call('head -n 9 forecast.csv | tail -n 8 >> one_day_forecast.csv',shell=True)
    return

