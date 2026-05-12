# Check if a sorted array has two numbers that sum to target
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

sorted_array = [1,4,5,6,7,9]
print(two_sum_sorted(sorted_array, 9))


# Anagrams
def is_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for item in s1:
        freq[item] = freq.get(item, 0) + 1

    for item in s2:
        if item not in freq:
            return False
        freq[item] = freq.get(item, 0) - 1 
    
    for item in freq.values():
        if item != 0:
            return False
    return True

print(is_anagrams("listen","silent"))


# Most frequent element in a list
def most_frequent(arr):
    if len(arr) == 0:
        return None
    
    freq = {}
    max = 0
    frequent = None
    for item in arr:
        freq[item] = freq.get(item, 0) + 1

    for item in arr:
        if freq[item] > max:
            max = freq[item]
            frequent = item
    return  frequent

print(most_frequent([1, 3, 3, 2, 1])) # Should return 1 (1 and 3 both appear twice, but 1 was first)
print(most_frequent([10, 20, 20, 10, 20])) # Should return 20