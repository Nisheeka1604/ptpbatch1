#2pointer approach
def remove_duplicates_two_pointer(arr):
    if not arr:
        return []

    i = 0  
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:  
            i += 1
            arr[i] = arr[j]  

    return arr[:i+1]  

arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates_two_pointer(arr))
ui