#solution 
def remove_duplicates_brute_force(arr):
    unique_sorted_arr = sorted(set(arr))
    return unique_sorted_arr

arr = [3, 1, 2, 3, 2, 4, 1]
print(remove_duplicates_brute_force(arr))
