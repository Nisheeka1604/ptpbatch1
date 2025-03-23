def max_consecutive_ones(arr):
    max_count = count = 0
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

arr = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(arr)) 
