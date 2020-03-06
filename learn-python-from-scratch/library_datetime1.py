#!/usr/bin/env python3

import datetime # Importing modules at the beginning of the program is a good practice

date_today = datetime.date.today() # Current date
print (date_today)

time_today = datetime.datetime.now()
print (time_today.strftime("%H:%M:%S"))# Current time
