#!/usr/bin/python

import mysql.connector as sql
import pandas as pd
import matplotlib.pyplot as plt

def plot_field(time_min,time_max,field):
    db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
    db_cursor = db_connection.cursor()
    str = "Select datatime,"+field+" FROM real_time_data where datatime<=\""+time_max+"\" and datatime>=\""+time_min+"\""

    db_cursor.execute(str)
    df = pd.DataFrame(db_cursor.fetchall())


    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df[0],df[1])
    plt.grid()
    fig.autofmt_xdate()

    ax.set_ylabel(field)
    fname = "/home/pi/workspace/WS/www/img/img-"+field+".png"
    plt.savefig(fname)
    plt.close()
    return None
