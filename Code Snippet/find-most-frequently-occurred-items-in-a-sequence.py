#### To determine the most frequently occurred items in a hashable sequence ####
#### Using collections.Counter class ####

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# Any sequence of hashable items can be input
# >>> Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
# The results can be accessed like a dictionary

top_three = word_counts.most_common(3)
# >>> [('eyes', 8), ('the', 5), ('look', 4)]