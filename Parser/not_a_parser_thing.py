
import datetime

current_date = datetime.datetime.now()


# Retrieving each component of the date
# i.e year,month,day,hour,minute,second and
# Multiplying with multiples of 100
# year - 10000000000
# month - 100000000
# day - 1000000
# hour - 10000
# minute - 100
# second - nothing

current_time = current_date.hour * 100 + current_date.minute

if current_time < 2300 and 800 < current_time:
    print("condition ok")
else:
    print("condition not ok")

