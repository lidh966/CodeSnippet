from collections import defaultdict

"""
dict uses list/set/... to map a single key to mutiple values
"""

#### Using dict ####
#### In this approach, you need to initialize the multivalue container (i.e., list) when first met ####
def cons_multi_dict_1(pairs):
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)
    return d
        
#### Using defaultdict ####
def cons_multi_dict_2(pairs):
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
    return d

if __name__ == '__main__':
    pairs = [
        ('First Name', 'Donghui'),
        ('Last Name', 'Li'),
        ('Birth Date', '1996-06-10')
    ]
    
    d1 = cons_multi_dict_1(pairs)
    d2 = cons_multi_dict_2(pairs)
    
    print(d1)
    print(d2)