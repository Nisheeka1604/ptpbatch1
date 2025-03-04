def find_missing_number(arr, n):
    xor1 = 0
    xor2 = 0
    
    for num in arr:
        xor1 ^= num
    
    for i in range(1, n + 1):
        xor2 ^= i
    
    return xor1 ^ xor2

print(find_missing_number([1, 2, 4, 5, 6], 6))
print(find_missing_number([1, 3], 3))
