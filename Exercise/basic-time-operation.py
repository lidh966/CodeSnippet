#### Basic time conversions using datetime module ####

from datetime import datetime, timedelta

# Creating an interval of time
a = timedelta(days=2, hours=6)

# Creating specific dates and times
now = datetime.today()
b = datetime(2019, 6, 15, 20, 32, 4)
print(b-a)