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
import Adafruit_DHT 
import mysql.connector
 
myAPI = "<your API code here>" 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18) 
   return (RH, T) 

def main(): 
   print 'starting...'
   
   # connect to db
   cnx = mysql.connector.connect(user='pi',passwd='dadopi', database='weather_station')
   cursor = cnx.cursor()
   
   add_value = ("INSERT INTO real_time_data "
                "(temperature,humidity) "
                "VALUES (%s, %s)")

   #open file
   out_file = open("db.txt","w")

   print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
   while True: 
       RH, T = getSensorData() 
       if RH is not None and T is not None:
           #write on file
           timestr=strftime("%Y-%m-%d %H:%M:%S",gmtime())
           out_file.write('{0},{1:0.1f},{2:0.1f}\n'.format(timestr, T, RH))
           out_file.flush()
           
           #insert to db
           value = (T,RH)
           cursor.execute(add_value, value)
                 
           # Make sure data is committed to the database
           cnx.commit()

           sleep(60)
       else:
           print('Failed to get reading. Try again!')
 
# call main 
if __name__ == '__main__': 
   main()  
