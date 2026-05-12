# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

    return arr

array = [3,9,8,5,4,1,7,6]
print(bubble_sort(array))


# # Selection sort
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min]:
#                 min = j

#         arr[i], arr[min] = arr[min], arr[i]
#     return arr

# nums = [64, 25, 12, 22, 11]
# print(selection_sort(nums))


# # Sorting dictionary

# def sort(dictionary):
#     n = len(dictionary)
#     for i in range(n):
#         max = i
#         for j in range(i + 1, n):
#             if dictionary[j]['avg'] > dictionary[max]['avg']:
#                 max = j
#         dictionary[i],  dictionary[max] = dictionary[max], dictionary[i]
#     return dictionary

# students = [
#     {"name": "Arun", "avg": 85},
#     {"name": "Sara", "avg": 72},
#     {"name": "Raj", "avg": 91}
# ]
# print(sort(students))