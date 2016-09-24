# see [1, Exercise 4.1.5] for more details
def find_max_subarray(array):
    max_subarray_low = 0
    max_subarray_high = 0
    max_subarray = array[0]

    # sum of the elements from (max_index + 1) to the current index
    max_subarray_end_at_current_index_low = 0
    max_subarray_end_at_current_index = array[0]

    for i in range(1, len(array)):
        max_subarray_end_at_current_index += array[i]
        if max_subarray_end_at_current_index < array[i]:
            max_subarray_end_at_current_index = array[i]
            max_subarray_end_at_current_index_low = i

        # The maximum subarray is either the maximum one in [1..(i-1)] or the one ending at i.
        # It is very important we know that the latter alternative ends at i.
        if max_subarray_end_at_current_index > max_subarray:
            max_subarray = max_subarray_end_at_current_index
            max_subarray_low = max_subarray_end_at_current_index_low
            max_subarray_high = i

    return max_subarray_low, max_subarray_high, max_subarray


def main(array):
    return find_max_subarray(array)
