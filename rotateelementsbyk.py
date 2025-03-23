def rotate_array(arr, k, direction):
    n = len(arr)
    k = k % n  

    if direction == "right":
        rotated_arr = arr[-k:] + arr[:-k]
    elif direction == "left":
        rotated_arr = arr[k:] + arr[:k]
    else:
        return "Invalid direction"

    return rotated_arr

arr1 = [1, 2, 3, 4, 5, 6, 7]
k1, direction1 = 2, "right"
print(*rotate_array(arr1, k1, direction1))

arr2 = [3, 7, 8, 9, 10, 11]
k2, direction2 = 3, "left"
print(*rotate_array(arr2, k2, direction2))
