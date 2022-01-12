# 1) Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)

Sort_dict = dict( sorted(d.items(), key=operator.itemgetter(1)))
print('Ascending order by value : ',Sort_dict)

Sort_dict = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order by value : ',Sort_dict)

"""
Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order by value :  {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
Descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
"""