def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)
    
    num_iteration:
    Integer to set the number of iterations

    If there is only one given value, the distribution does't change.

    If there are only two given values, the neighbour with the max value changes every iteration, 
    but the distribution stays the same.

    From three values onwards, the value is distributed as specified.
    """

    values_new = values.copy()

    for _ in range(num_iterations):
        max_value = max(values_new)
        max_value_index = values_new.index(max_value)

        # Check if there is a left neighbor
        if (max_value_index - 1) >= 0:
            values_new[max_value_index - 1] += max_value * share
        else:
            values_new[-1] += max_value * share

        # Check if there is a right neighbor
        if (max_value_index + 1) < len(values_new):
            values_new[max_value_index + 1] += max_value * share
        else:
            values_new[0] += max_value * share

        values_new[max_value_index] -= (max_value * share) * 2
    return values_new
