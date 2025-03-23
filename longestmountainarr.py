def longestMountain(arr):
    n = len(arr)
    max_length, i = 0, 1

    while i < n - 1:
        while i < n - 1 and arr[i] == arr[i - 1]:
            i += 1

        up, down = 0, 0
        while i < n and arr[i] > arr[i - 1]:
            up += 1
            i += 1

        while i < n and arr[i] < arr[i - 1]:
            down += 1
            i += 1

        if up > 0 and down > 0:
            max_length = max(max_length, up + down + 1)

    return max_length

arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))
