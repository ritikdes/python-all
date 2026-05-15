# Given an array of 0s and 1s, find the maximum number of consecutive 1s.
def consecutive_ones(arr):
    current = 0
    max_length = 0
    for num in arr:
        if num == 1:
            current += 1
        else:
            current = 0
        max_length = max(max_length, current)
    return max_length

print(consecutive_ones([0,1,1,0,0,1,0,1,1,1]))