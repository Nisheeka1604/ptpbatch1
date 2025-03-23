def sortedSquares(nums):
    squared = [num ** 2 for num in nums]
    squared.sort()
    return squared

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
