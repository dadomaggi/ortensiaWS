#!/usr/bin/python

import mysql.connector as sql
import pandas as pd
import matplotlib.pyplot as plt

db_connection = sql.connect(database='weather_station', user='pi', password='dadopi')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM real_time_data')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)

#print(df)

fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes[0]
axes[0].plot(df[1],df[2])
axes[1].plot(df[1],df[3])
fig.autofmt_xdate()

axes[0].set_ylabel('temperature')
axes[1].set_ylabel('humidity')
plt.show()
