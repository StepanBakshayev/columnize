from collections import Counter, deque
from math import log2
from itertools import chain

from django import template
from django.db import models


register = template.Library()


def split_in_half(values):
    if not values:
        return [deque(), deque()]

    head_width = 0
    tail_width = 0
    head = []
    tail = []

    values = values.copy()
    head.append(values.popleft())
    head_width += head[-1][1]

    while values:
        while head_width < tail_width and values:
            head.append(values.popleft())
            head_width += head[-1][1]
        while tail_width <= head_width and values:
            tail.append(values.pop())
            tail_width += tail[-1][1]

    head.sort()
    tail.sort()
    return [deque(head), deque(tail)]


def split(values, parts):
    result = [values,]
    for _ in range(parts):
        splitted = []
        for v in result:
            head, tail = split_in_half(v)
            if head:
                splitted.append(head)
            if tail:
                splitted.append(tail)
        result = splitted
    return result


@register.filter
def columns(items, number):
    letters = Counter()
    for name in items.only('name').values_list('name', flat=True):
        letters[name[:1]] += 1

    ordered = items.order_by('name')
    for d in split(deque(sorted(letters.items())), int(log2(number))):
        q = models.Q()
        for x in d:
            q |= models.Q(name__startswith=x[0])
        yield ordered.filter(q)
