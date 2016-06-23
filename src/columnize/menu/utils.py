from copy import deepcopy
from itertools import groupby, chain


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


    def make_choice(best_score, best_groups, groups, values, by):
        weights = [0] * by
        for number, items in groupby(zip(groups, values), lambda x: x[0]):
            weights[number] = sum(i[1] for i in items)
        max_weight = max(weights)
        score = (sum((max_weight-w for w in weights)), max_weight-min(weights))
        if best_score > score:
            return score, deepcopy(groups), weights
        return best_score, best_groups, weights


    head = values_len - by
    groups = [0,]*(head) + list(range(by))
    #counts = [head+1] + [1] * (by-1)
    best_groups = deepcopy(groups)
    weights = [sum(values[:head]),] + values[head:]
    max_weight = max(weights)
    best_score = (sum((max_weight-w for w in weights)), max_weight-min(weights))
    under_pressure = 0
    moved = False

    #print('start', groups)
    while under_pressure+1 < by:
        items = groupby(enumerate(groups), lambda x: x[1])
        for column, group in items:
            if column != under_pressure:
                continue

            if moved:
                break

            last_index, _ = next(group)
            group_count = 1
            for i, _ in group:
                last_index = i
                group_count += 1

            if group_count == 1:
                under_pressure += 1
            else:
                groups[last_index] += 1
                #print('press', under_pressure, groups)
                best_score, best_groups, weights = make_choice(best_score, best_groups, groups, values, by)

            break

        column, group = next(items)
        if column == under_pressure:
            continue

        moved = False
        for column, group in chain(((column, group),), items):
            if column+1 == by:
                break

            last_index, _ = next(group)
            group_count = 1
            for i, _ in group:
                last_index = i
                group_count += 1

            if weights[column] > weights[column+1]:
                groups[last_index] += 1
                #print('wave', under_pressure, groups)
                best_score, best_groups, weights = make_choice(best_score, best_groups, groups, values, by)
                moved = True

    #print()
    #print()

    for _, items in groupby(zip(best_groups, values), lambda x: x[0]):
        yield (i[1] for i in items)
