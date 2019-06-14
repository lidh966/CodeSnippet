#### Filterting sequence elements ####
#### Using itertools.compress ####
#### 1st, to create a sequence of Booleans that indicates which elements satisfy filtering ####
#### 2nd, using compress to select the elements with corrsponding True in Booleans sequence ####

# Suppose I want to filter the addresses with N
from itertools import compress
addresses = [
    '5412 N CLARK', 
    '5148 N CLARK', 
    '5800 E 58TH', 
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON', 
    '4801 N BROADWAY', 
    '1039 W GRANVILLE',
]
is_N = []
for address in addresses:
    if address.split(' ')[1] == 'N':
        is_N.append(True)
    else:
        is_N.append(False)
result_filter = compress(addresses, is_N)