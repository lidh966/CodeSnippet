#### To sort a list of dictionaries by a common key ####
#### Using operator.itmegetter

from operator import itemgetter

rows = [ 
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() can also accept multiple keys
rows_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
print(rows_by_lfname)

#### The technique can also be used to get min/max ####
min_by_uid = min(rows, key=itemgetter('uid'))
max_by_uid = max(rows, key=itemgetter('uid'))
print(min_by_uid, max_by_uid)