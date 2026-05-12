# Linear Search

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i  # Return Index
    return -1  # Not found
    
nums = [4, 7, 2, 9, 1, 5, 8, 3, 6]
print(linear_search(nums, 5))   # should return 5 (index)
print(linear_search(nums, 10))  # should return -1


# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid  = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_nums, 7))   # should return 3
print(binary_search(sorted_nums, 6))   # should return -1


# Counting the number of times target appears
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

count_target = [1,5,8,9,6,5,2,0,5]
print(count_occurrences(count_target, 5))