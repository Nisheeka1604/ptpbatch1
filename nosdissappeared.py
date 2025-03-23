def findDisappearedNumbers(nums):
    res = []
    for i in range(1, len(nums) + 1):
        if i not in nums:
            res.append(i)
    return res

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
