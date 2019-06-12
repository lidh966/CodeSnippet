#### to perform useful calculations on dictionary contents, it is often useful to convert the keys and values of the dictionary using zip() ####
#### zip() creates an iterator, which can only be consumed once ####

numbers = {
    'Bryrant': 24,
    'Gasol': 16,
    'Bynum': 17,
    'Odom': 7,
    'Fisher': 2
}

# find min/max value with its key
min_number = min(zip(numbers.values(), numbers.keys()))
max_number = max(zip(numbers.values(), numbers.keys()))

# sort the dictionary
numbers_sorted = sorted(zip(numbers.values(), numbers.keys()))    # sort by values
numbers_sorted = sorted(zip(numbers.keys(), numbers.values()))    # sort by keys
