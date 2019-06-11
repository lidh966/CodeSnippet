# star expression #

# Case 1. drop the first and last grades in grade records, and obtain the average of the others
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

# Case 2. Iterating over a sequence of tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Case 3.
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
# name='ACME', year=2012

#### Case 4 ####
items = [1, 2, 3, 4]
head, *tail = items
# head=1, tail=[2,3,4]