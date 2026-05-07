numbers = [6,8,2,1,0,9,5]

def summarize_list(numbers):
    total_sum = 0
    count = 0
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
        total_sum += num
    count = len(numbers)
    average = total_sum / count

    return {"min":min_val, "max":max_val, "sum":total_sum, "average":average, "count":count}


print(summarize_list(numbers))