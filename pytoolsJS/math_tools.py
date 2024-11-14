import numpy as np


def average_ragged_array(arr: list[np.ndarray], return_counts: bool = False) -> np.ndarray:
    '''
    takes the average of a ragged 2d array across axis 0
    '''

    longest_array_size = max(len(x) for x in arr)

    sum_array = np.zeros(longest_array_size)
    count_array = np.zeros(longest_array_size)

    for subarray in arr:
        length = len(subarray)
        sum_array[:length] += subarray
        count_array[:length] += 1
    
    average = sum_array / count_array

    if return_counts:
        return average, count_array
    return average



