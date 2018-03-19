""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep
from time import gmtime, strftime 
import datetime

import Adafruit_DHT 
import mysql.connector
import weatherlib as wl
import wlutils
import weatherplotlib as wlplot
import owm_api as owm 

myAPI = "<your API code here>" 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18) 
   return (RH, T) 

def main(): 
   print 'starting...'
   
   # connect to real_time_data db
   cnx = mysql.connector.connect(user='pi',passwd='dadopi', database='weather_station')
   cursor = cnx.cursor()
   
   add_value = ("INSERT INTO real_time_data "
                "(temperature,humidity,dew_point,heat_index) "
                "VALUES (%s, %s, %s, %s)")
   # add_value to daily_data
   add_daily_values = ("INSERT INTO daily_data "
                   "(datatime,temperature_min,temperature_max,temperature_ave) "
                   "VALUES (%s,%s,%s,%s)")

   today = datetime.date.today()

   #open file
   #out_file = open("db.txt","w")
   #initialization 
   print "running start @"
   print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
   RH, T = getSensorData()
   if RH is not None and T is not None:
       Tmax = T
       Tmin = T
       Tave = T
       dt = wlutils.secs_from_midnight()

   while True: 
       RH, T = getSensorData() 
       if RH is not None and T is not None and (RH <100):
           #write on file
           #timestr=strftime("%Y-%m-%d %H:%M:%S",gmtime())
           #out_file.write('{0},{1:0.1f},{2:0.1f}\n'.format(timestr, T, RH))
           #out_file.flush()
           
           Tdp = wl.dew_point(T,RH)
           HI = wl.heat_index(T,RH)

           #insert to db - real time data
           value = (T, RH, Tdp, HI)

           cursor.execute(add_value, value)
                 
           # Make sure data is committed to the database
           cnx.commit()

           if today == datetime.date.today():
               if T < Tmin:
                   Tmin = T
               if T > Tmax:
                   Tmax = T
               
               # compute average
               Tave = Tave*dt + T*(wlutils.secs_from_midnight()-dt)
               dt = wlutils.secs_from_midnight()
               Tave = Tave/dt
               #print("today actuals:")
               #print(Tmin,Tmax,Tave)
               wlplot.plot_year()
           else:
               print("day changed: update day_table")
               
               # update the forecast - OpenWeatherMap
               owm.update_forecast()
               
               # update daily_data table
               values = (today,Tmin,Tmax,Tave)
               cursor.execute(add_daily_values,values)
               cnx.commit()

               print("day changed: reset Tmin-Tmax")
               Tmax=T
               Tmin=T
               Tave=T
               
               dt = wlutils.secs_from_midnight()
               today = datetime.date.today()
               
               # update year graph
               wlplot.plot_year()

           tmax = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           tmin = (datetime.datetime.now() - datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
           wlplot.plot_field(tmin, tmax, "temperature")
           wlplot.plot_field(tmin, tmax, "humidity")
           wlutils.fwrite(tmax,Tmin,Tmax,Tave,T,RH)
           sleep(300)

       else:
           print('Failed to get reading. Try again!')
 
# call main 
if __name__ == '__main__': 
   main()  
