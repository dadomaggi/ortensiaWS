#!/usr/bin/python

import mysql.connector as sql
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import wlutils as wl
import numpy as np
from pyowm import OWM
import time

def plot_year():
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    #str = "Select datatime,temperature FROM real_time_data where datatime>=\"2018-01-01\""
    str="Select datatime,temperature_ave FROM daily_data where datatime>=\"2018-01-01\"" 

    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
                        
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(16, 3))
    ax.plot(df[0],wl.medfilt(array,5))
    
    fc = pd.read_csv('ave.csv', sep=',', decimal='.',index_col=0)
    ax.plot(fc.index,fc.values)
                            
    
    plt.grid()

    fname = "/home/pi/workspace/WS/www/img/img-year.png"
    plt.savefig(fname)
    plt.close()



def plot_field(time_min,time_max,field):
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    str = "Select datatime,"+field+" FROM real_time_data where datatime<=\""+time_max+"\" and datatime>=\""+time_min+"\""
    
    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
    
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(16, 3))
    ax.plot(df[0],wl.medfilt(array,5))
    plt.grid()
 
    if field=='temperature':
        
        fc = pd.read_csv('forecast.csv', sep=',', decimal='.',index_col=0)
        #fc.plot(ax=ax)
        ax.plot(fc.index,fc.values)

    print field
    #fig.autofmt_xdate()
    plt.minorticks_on()
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))   #to get a tick every 15 minutes
    ax.xaxis.set_major_formatter(mdates.DateFormatter('\n%d-%m-%Y'))     #optional formatting
    #plt.margins(x=0.1)
    plt.subplots_adjust(bottom=0.15)

    plt.grid(b=True, which='minor', color='r', linestyle='--',linewidth=0.5)
    plt.grid(b=True, which='major', color='k', linestyle='-',linewidth=1)

    ax.set_ylabel(field)
    fname = "/home/pi/workspace/WS/www/img/img-"+field+".png"
    plt.savefig(fname)
    plt.close()
    return None
