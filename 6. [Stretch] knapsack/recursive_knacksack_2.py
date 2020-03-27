items = [(1, 42, 81), (2, 42, 42), (3, 68, 56), (4, 68, 25), (5, 77, 14),
         (6, 57, 63), (7, 17, 75), (8, 19, 41), (9, 94, 19), (10, 34, 12)]
capacity = 100


def knapsack_hash(items, capacity):
    if len(items) == 0:
        return []

    elif items[-1][1] > capacity:
        return knapsack_hash(items[:-1], capacity)

    else:
        take_list = knapsack_hash(items[:-1],
                                  capacity - items[-1][1]) + [items[-1]]
        no_take_list = knapsack_hash(items[:-1], capacity)

        take_values = [x[2] for x in take_list]
        no_take_values = [x[2] for x in no_take_list]

        sum_take = sum(take_values)
        sum_no_take = sum(no_take_values)

        if sum_take > sum_no_take:
            return take_list
        else:
            return no_take_list

#  returns [(1, 42, 81), (7, 17, 75), (8, 19, 41)]