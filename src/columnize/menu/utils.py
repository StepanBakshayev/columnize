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

    head = values_len - by
    groups = [0,]*(head) + list(range(by))
    weights = [sum(values[:head]),] + values[head:]
    best_groups = deepcopy(groups)
    max_weight = max(weights)
    best_score = sum((max_weight-w for w in weights))
    assert sum(weights) == sum(values)

    while groups[0] == 0:
        print(groups)
        items = iter(groups)
        previous_index = 0
        previous_group = next(items)
        for index, group in enumerate(items, 1):
            if previous_group != group:
                groups[previous_index] += 1

                weights = []
                for _, items in groupby(zip(groups, values), lambda x: x[0]):
                    weights.append(sum(i[1] for i in items))
                max_weight = max(weights)
                score = sum((max_weight-w for w in weights))
                print('w', weights)
                print('best', best_score, 'score', score)
                if best_score > score:
                    best_groups = deepcopy(groups)
                    best_score = score

                break

            previous_index, previous_group = index, group


    print()
    print()
    for _, items in groupby(zip(best_groups, values), lambda x: x[0]):
        yield (i[1] for i in items)
