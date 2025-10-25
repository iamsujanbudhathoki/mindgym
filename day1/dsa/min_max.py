# Find the maximum and minimum element in an array.

# Solution 1 
def find_min_max(array: list[int]):
    min = array[0]
    max = array[0]
    for item in array:
        if min > item:
            min = item
        if max < item:
            max = item

    return min, max




# Solution 2
def find_min_max(array: list[int]):
    array.sort()
    return array[0], array[len(array)-1]



# ----------------- || ---------------------------
# Execution

lists = [13, -2, 37, 4, 59, 696, 9]

min, max = find_min_max(lists)


print(min,max)