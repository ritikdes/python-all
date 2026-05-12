def linear_search(arr, target):
    for i, num in enumerate(arr):
        print(f"Index: {i}: {arr} | Value:{arr[i]}")
        if num == target:
            return i
    return -1

def binary_search(arr, target): 
    left, right = 0, len(arr) - 1   
    while left <= right:
        mid  = (left + right) // 2
        print(f"Low: {left}, High: {right}, Mid Index: {mid} (Value: {arr[mid]})")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left  = mid + 1
            print(left)
        else:
            right = mid - 1
            print(right)
    return -1

def bubble_sort(arr):
    n  = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr


def  most_frequent(arr):
    freq = {}
    max_count = 0
    winner = 0
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        print(freq)
    
    for item in arr:
        if freq[item] > max_count:
            max_count = freq[item]
            winner = item
    return winner


def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return -1




arr = list(map(int, input("Enter a list of numbers separated by space: ").split()))

while True:
    print("--------MENU--------")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Bubble Sort")
    print("4. Find most frequent")
    print("5. Two Sum")
    print("6. Exit")

    choice = input("Enter your choice: ")
    arr_copy = arr.copy()

    if choice == "6":
        print("Goodbye!")
        break

    elif choice == "1":
        target = int(input("Enter the target to search: "))
        idx = linear_search(arr,target)
        if idx == -1:
            print(f"{target} not found.")
        else:
            print(f"The target is in index {idx}")
    
    elif choice == "2":
        target = int(input("Target: "))
        arr_copy = sorted(arr_copy)
        binary_search(arr_copy, target)

    elif choice == "3":
        sorted_list = bubble_sort(arr_copy)
        print(f"The sorted array: {sorted_list}")

    elif choice == "4":
        frequent = most_frequent(arr)
        if frequent:
            print(f"The most frequent number is {frequent}")
        else:
            print("Doesnt exist")

    elif choice == "5":
        target = int(input("Enter the target to search: "))
        result = two_sum(arr, target)
        if result == -1:
            print("No pair found")
        else:
            left, right = result
            print(f"Pair: {arr[left]} + {arr[right]} = {target}")

    else:
        print("Invalid choice!")