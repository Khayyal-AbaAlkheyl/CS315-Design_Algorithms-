def optimized_algo(cargo_list, weight):
    n = len(cargo_list)
    mmory_2D = [[None] * (weight + 1) for _ in range(n + 1)]
    return algo(cargo_list, n, weight, mmory_2D)

def algo(cargo_list, index, weight, mmory_2D):
    #base case
    if index == 0 or weight == 0:
        return 0, []
    # if we got it be for
    if mmory_2D[index][weight] is not None:
        return mmory_2D[index][weight]

    value, w , _ = cargo_list[index - 1]

    # if item weight is larger than max weight
    if w > weight:
        result = algo(cargo_list, index - 1, weight, mmory_2D)
        mmory_2D[index][weight] = result
        return result

    # Take item:
    with_val, with_list = algo(cargo_list, index - 1, weight - w, mmory_2D)
    with_val += value
    with_list = with_list + [index - 1]  
    # Skip item
    without_val, without_list = algo(cargo_list, index - 1, weight, mmory_2D)

    #take the max value subset and log it to mmory_2D
    if with_val > without_val:
        mmory_2D[index][weight] = (with_val, with_list)
        return with_val, with_list
    else:
        mmory_2D[index][weight] = (without_val, without_list)
        return without_val, without_list
    