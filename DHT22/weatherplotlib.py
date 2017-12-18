#!/usr/bin/python

import mysql.connector as sql
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import wlutils as wl

def plot_field(time_min,time_max,field):
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    str = "Select datatime,"+field+" FROM real_time_data where datatime<=\""+time_max+"\" and datatime>=\""+time_min+"\""
    
    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
    
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df[0],wl.medfilt(array,5))
    plt.grid()
    
    #fig.autofmt_xdate()
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))   #to get a tick every 15 minutes
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))     #optional formatting 

    ax.set_ylabel(field)
    fname = "/home/pi/workspace/WS/www/img/img-"+field+".png"
    plt.savefig(fname)
    plt.close()
    return None
