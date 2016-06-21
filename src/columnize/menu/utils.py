from array import array
from copy import deepcopy
from itertools import groupby

def split(values, by):
    groups = array('i', (0,)*len(values))
    best = deepcopy(groups)

    for _, items in groupby(zip(groups, values), lambda x: x[0]):
        yield (i[1] for i in items)
