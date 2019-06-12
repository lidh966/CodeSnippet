#### Problem: you want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items ####
#### Basic idea: using set ####

# Solution 1. for hashable sequence (e.g., list)
def dedupe_hashable(items):
    """
    items: the sequence to be operated
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    return seen

# Solution 2. for unhashanble sequence (e.g., dictionary)
def dedupe_unhashable(dict_in):
    """
    items: [dict]
    """
    result = {}
    for key,value in dict_in.items():
        if value not in result.values():
            result[key] = value
    return result

if __name__ == '__main__':
    x = [1,2,4,5,7,2,4,3,7,7,7]
    xx = dedupe_hashable(x)

    y = {
        'a': 1,
        'b': 2,
        'a': 1
    }
    yy = dedupe_unhashable(y)
    print(yy)