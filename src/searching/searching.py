def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (high + low) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess < target:
            low = middle + 1
        if guess > target:
            high = middle - 1
    return -1  # not found
