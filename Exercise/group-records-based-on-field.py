#### To group records based on a field ####
#### The records are stored in a list of dictionaries ####
#### Using itertools.groupy() ####

from itertools import groupby
from operator import itemgetter

rows = [ 
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, 
    {'address': '5148 N CLARK', 'date': '07/04/2012'}, 
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, 
    {'address': '2122 N CLARK', 'date': '07/03/2012'}, 
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, 
    {'address': '1060 W ADDISON', 'date': '07/02/2012'}, 
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, 
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field first, which is a required process due to groupby() can only scan consequtive sequences
rows.sort(key=itemgetter('date'))
# Group the records based on date
grouped_records = {}
for date, items in groupby(rows, key=itemgetter('date')):
    grouped_records[date] = []
    for item in items:
        grouped_records[date].append(item)