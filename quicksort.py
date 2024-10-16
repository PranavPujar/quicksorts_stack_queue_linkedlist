# PRANAV UMAKANT PUJAR 1001965075

import random

def partition(arr, low, high):
    """Partitions the array around a pivot element.

    Args:
        arr: The input array
        low: The starting index of the subarray
        high: The ending index of the subarray

    Returns:
        The index of the pivot element
    """

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, i):
    """Finds the i-th smallest element in an array using the quicksort algorithm.

    Args:
        arr: The input array.
        low: The starting index of the subarray
        high: The ending index of the subarray
        i: The index of the desired element (1-based)

    Returns:
        The i-th smallest element in the array
    """

    if low == high:
        return arr[high]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1  # Position of pivot element in sorted order

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quicksort(arr, low, pivot_index - 1, i)
    else:
        return quicksort(arr, pivot_index + 1, high, i - k)

# Example usage
arr = [7, 1, 43, 5, 2, 5435, 23, 32, 22]
n = len(arr)
i = 6 
result = quicksort(arr, 0, n - 1, i)
print(f'Input Array: {arr}')
print(f"The {i}th order statistic ({i}th smallest element) is: {result}")

