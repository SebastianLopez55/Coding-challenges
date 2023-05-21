def quick_sort(arr):
    """
    Sorts an array of integers in ascending order using the Quick Sort algorithm.
    """
    # If the array is empty or contains only one element, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Choose the pivot element as the median of the first, middle, and last elements in the array.
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    # O(1) time as it does not scale with size of array
    pivot = sorted([first, middle, last])[1]

    # Partition the array into two sub-arrays based on the pivot element.
    low = []
    high = []
    pivot_count = 0  # To keep track of the number of elements equal to the pivot.

    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            pivot_count += 1

    # Recursively sort the sub-arrays.
    sorted_low = quick_sort(low)
    sorted_high = quick_sort(high)

    # Combine the sorted sub-arrays and the pivot element to get the final sorted array.
    sorted_arr = []
    for num in sorted_low:
        sorted_arr.append(num)
    print("first combination")
    print(sorted_arr)
    for i in range(pivot_count):
        sorted_arr.append(pivot)
    print("second combination")
    print(sorted_arr)
    for num in sorted_high:
        sorted_arr.append(num)

    return sorted_arr


# Test case 1
arr1 = [5, 2, 8, 4, 7, 1, 3, 9, 6]
sorted_arr1 = quick_sort(arr1)
print(sorted_arr1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Test case 2
# arr2 = [4, 4, 4, 4, 4, 4, 4]
# sorted_arr2 = quick_sort(arr2)
# print(sorted_arr2)  # Output: [4, 4, 4, 4, 4, 4, 4]
#
# # Test case 3
# arr3 = [1, 2, 3, 4, 5]
# sorted_arr3 = quick_sort(arr3)
# print(sorted_arr3)  # Output: [1, 2, 3, 4, 5]
#
# # Test case 4
# arr4 = [5, 4, 3, 2, 1]
# sorted_arr4 = quick_sort(arr4)
# print(sorted_arr4)  # Output: [1, 2, 3, 4, 5]
#
# # Test case 5
# arr5 = []
# sorted_arr5 = quick_sort(arr5)
# print(sorted_arr5)  # Output: []
