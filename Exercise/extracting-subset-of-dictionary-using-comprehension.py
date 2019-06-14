#### To extract a subset of a dictionary ####
#### Using dictionary comprehension ####
#### Hint: dict_object.items() returns a list of (key, value) pair ####

prices = { 
    'ACME': 45.23, 
    'AAPL': 612.78, 
    'IBM': 205.55,
    'HPQ': 37.20, 
    'FB': 10.75
}

p1 = {key:value for key, value in prices.items() if value>200}
# prices.items() returns a list of (key, value) pair
# for key, value in list of tuples can go through the list of pairs
print(p1)