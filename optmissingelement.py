def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing_number([1, 2, 4, 5, 6], 6))  
print(find_missing_number([1, 3], 3))          
