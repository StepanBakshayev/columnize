from copy import deepcopy
from itertools import groupby


def split(values, by):
    assert by > 0

    if by == 1:
        yield values
        return

    if not values:
        yield ()
        return

    values_len = len(values)

    if values_len == 1:
        yield (values[0],)
        return

    if values_len <= by:
        for v in values:
            yield (v,)
        return

    head = values_len - by
    groups = [0,]*(head) + list(range(by))
    counts = [head+1] + [1] * (by-1)
    best_groups = deepcopy(groups)
    weights = [sum(values[:head]),] + values[head:]
    max_weight = max(weights)
    best_score = sum((max_weight-w for w in weights))

    while True:
        items = iter(groups)
        previous_index = 0
        previous_group = next(items)
        for index, group in enumerate(items, 1):
            if previous_group != group and counts[previous_group] > 1:
                groups[previous_index] += 1
                counts[previous_group] -= 1
                counts[group] += 1

                weights = [0] * by
                for number, items in groupby(zip(groups, values), lambda x: x[0]):
                    weights[number] = sum(i[1] for i in items)
                max_weight = max(weights)
                score = sum((max_weight-w for w in weights))
                if best_score > score:
                    best_groups = deepcopy(groups)
                    best_score = score

                if sum(weights[:group]) > sum(weights[group:]):
                    break

            if group + 1 == by:
                break

            previous_index, previous_group = index, group

        if sum(counts[:-1]) == by - 1:
            break

    for _, items in groupby(zip(best_groups, values), lambda x: x[0]):
        yield (i[1] for i in items)
