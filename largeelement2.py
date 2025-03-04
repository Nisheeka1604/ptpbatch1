# Normal solution using iteration
def find_largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

print(find_largest_element([1, 8, 7, 56, 90]))  
print(find_largest_element([5, 5, 5, 5]))       
print(find_largest_element([10]))               
