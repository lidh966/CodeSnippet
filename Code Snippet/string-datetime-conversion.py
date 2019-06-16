#### Converting string to timestamp and vise versa ####
#### Using datetime.strptime() & datetime.strftime() ####

from datetime import datetime

# string to datetime
date_text = '2019-06-16'
date = datetime.strptime(date_text, '%Y-%m-%d')    # >>> datetime.datetime(2019, 6, 16, 0, 0)

# datetime to string
date = datetime(2019, 6, 16, 16, 10)
date_text = datetime.strftime(date, '%A %B %d, %Y')    # >>> 'Sunday June 16, 2019'