def find_element(arr, num):
    if num in arr:
        return arr.index(num)
    return -1

arr = [2, 4, 6, 8, 10]
num = 6
print(find_element(arr, num))
