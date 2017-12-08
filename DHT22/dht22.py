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

 
myAPI = "<your API code here>" 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18) 
   return (RH, T) 

def main(): 
   print 'starting...'
   
   out_file = open("test.txt","w")

   print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
   while True: 
       RH, T = getSensorData() 
       if RH is not None and T is not None:
           #timestr=strftime("%a, %d %b %Y %H:%M:%S", gmtime())
           timestr=strftime("%Y-%m-%d %H:%M:%S",gmtime())
           out_file.write('{0},{1:0.1f},{2:0.1f}\n'.format(timestr, T, RH))
           out_file.flush()
           sleep(60)
       else:
           print('Failed to get reading. Try again!')
 
# call main 
if __name__ == '__main__': 
   main()  
