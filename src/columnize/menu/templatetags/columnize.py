from collections import Counter, deque
from math import log2
from itertools import chain

from django import template
from django.db import models

from ..utils import split


register = template.Library()


@register.filter
def columns(items, number):
    counter = Counter()
    for name in items.only('name').values_list('name', flat=True):
        counter[name[:1]] += 1

    ordered = items.order_by('name')
    letters = sorted(counter.items())

    index = 0
    for group in split([l[1] for l in letters], number):
        q = models.Q()
        for _ in group:
            q |= models.Q(name__startswith=letters[index][0])
            index += 1
        yield ordered.filter(q)
