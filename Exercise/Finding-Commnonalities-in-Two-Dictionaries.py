#### to find out what two dictionaries have in common ####
#### perform common set operations using keys() or items() methods
a = {
    'Bryant': 8,
    'Oneil': 34,
    'Odom': 7
}
b = {
    'Bryant': 24,
    'Bynum': 17,
    'Odom': 7
}

# Find keys in common
result = a.keys() & b.keys()

# Find keys in a not in b
result = a.keys() - b.keys()

# Find (key, value) pairs in common
result = a.items() & b.items()

# Make a new dictionary with certain keys removed
result = {key:a[key] for key in a.keys() - {'Oneil'}}
print(result)

