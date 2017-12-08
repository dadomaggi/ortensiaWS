#!/us/bin/python
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='pi',passwd='dadopi', database='weather_station')
cursor = cnx.cursor()

query = ("select id,temperature,humidity from real_time_data;")

cursor.execute(query)

for (id,temperature,humidity) in cursor:
      print("{}, {}, {}".format(
              id, temperature, humidity))

add_value = ("INSERT INTO real_time_data "
                       "(temperature,humidity) "
                                      "VALUES (%s, %s)")
value = (26.4,78.9)
cursor.execute(add_value, value)
      
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

