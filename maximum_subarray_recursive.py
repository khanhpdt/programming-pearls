def find_max_subarray_from_one_end(array, range_subarray):
    # starts at one end of the subarray. this end is stored as the left-most element of the given range.
    max_index = range_subarray[0]
    max_subarray_sum = array[max_index]

    # find the right-end index giving the maximum-sum subarray
    subarray_sum = max_subarray_sum
    for i in range_subarray[1:]:
        subarray_sum += array[i]
        if subarray_sum > max_subarray_sum:
            max_subarray_sum = subarray_sum
            max_index = i

    return max_index, max_subarray_sum


def find_max_crossing_subarray(array, low, mid, high):
    (left_index, left_sum) = find_max_subarray_from_one_end(array, range(mid, low - 1, -1))
    (right_index, right_sum) = find_max_subarray_from_one_end(array, range(mid + 1, high + 1, 1))
    return left_index, right_index, left_sum + right_sum


# see [1, Section 4.1] for more details
def find_max_subarray(array, low, high):
    # base case
    if low == high:
        return low, high, array[low]

    # divide and conquer
    mid = (low + high) // 2
    (left_low, left_high, left_sum) = find_max_subarray(array, low, mid)
    (right_low, right_high, right_sum) = find_max_subarray(array, (mid + 1), high)
    (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(array, low, mid, high)

    # combine
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def main(array):
    return find_max_subarray(array, 0, len(array) - 1)
