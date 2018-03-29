#!/usr/bin/python

import mysql.connector as sql
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import wlutils as wl
import numpy as np
from pyowm import OWM
import time
import datetime
import os

def plot_year():
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    #str = "Select datatime,temperature FROM real_time_data where datatime>=\"2018-01-01\""
    str="Select datatime,temperature_ave FROM daily_data where datatime>=\"2018-01-01\"" 

    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
                        
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df[0],wl.medfilt(array,5))
    
    fname = os.environ["WSDATAPATH"]+"/ave.csv"
    fc = pd.read_csv(fname, sep=',', decimal='.',index_col=0)
    ax.plot(fc.index,fc.values)
                            
    
    plt.grid()
    
    fname = os.environ["WWWDATAPATH"]+"/img/img-year.png"
    plt.savefig(fname)
    plt.close()

def plot_month():
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()

    ts = time.time()-2592000
    one_month_ago = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    today = datetime.datetime.fromtimestamp(time.time()+864000).strftime('%Y-%m-%d')
    fourty_days_ago = datetime.datetime.fromtimestamp(ts-864000).strftime('%Y-%m-%d')
    str = "Select datatime,temperature FROM real_time_data where datatime>=\""+one_month_ago+"\""
    #str="Select datatime,temperature_ave FROM daily_data where datatime>=\"2018-01-01\"" 
    

    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
                                                    
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df[0],wl.medfilt(array,5))
                                                                  
    fname = os.environ["WSDATAPATH"]+"/ave.csv"
    fc = pd.read_csv(fname, sep=',', decimal='.',index_col=0)
    ii = (fc.index>=fourty_days_ago) & (fc.index<=today) 

    ax.plot(fc.index[ii],fc.values[ii])
    #ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
    #ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))   #to get a tick every 15 minutes
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m\n%Y'))     #optional formatting
    plt.subplots_adjust(bottom=0.15)
                                                                                              
    plt.grid()
                                                                                                                        
    fname = os.environ["WWWDATAPATH"]+"/img/img-month.png"
    
    plt.savefig(fname)
    plt.close()
    return

def plot_forecast(time_min,time_max):
    
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    str = "Select datatime,temperature FROM real_time_data where datatime<=\""+time_max+"\" and datatime>=\""+time_min+"\""
               
    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())
                           
    ndarray = df.values
    array = ndarray[:,1]

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(df[0],wl.medfilt(array,5))
    plt.grid()
                                                
    fname = os.environ["WSDATAPATH"]+"/forecast.csv"
    fc = pd.read_csv(fname, sep=',', decimal='.',index_col=0)
    #fc.plot(ax=ax)
    ax.plot(fc.index,fc.values)

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

    ax.set_ylabel('forecast')
    fname = os.environ["WWWDATAPATH"]+"/img/img-forecast.png"
    plt.savefig(fname)
    plt.close()

    return None


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
 
    #if field=='temperature':
    #    fname = os.environ["WSDATAPATH"]+"/forecast.csv"
    #    fc = pd.read_csv(fname, sep=',', decimal='.',index_col=0)
    #    #fc.plot(ax=ax)
    #    ax.plot(fc.index,fc.values)

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
    fname = os.environ["WWWDATAPATH"]+"/img/img-"+field+".png"
    plt.savefig(fname)
    plt.close()
    return None
