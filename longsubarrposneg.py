def longest_subarray_with_sum_k(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_length

arr = [10, 5, 2, 7, 1, -1, -3, 4]
k = 8
print(longest_subarray_with_sum_k(arr, k))
