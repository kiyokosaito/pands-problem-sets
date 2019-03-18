# Kiyoko Saito, 2019-03-03
# Is today begin with T?

import datetime

if datetime.datetime.today().weekday() == 1 and 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
