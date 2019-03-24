#this is the solution for Q8

from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%A, %B %d %Y at %I : %M %p ")
print (dt_string)