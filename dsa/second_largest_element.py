# Find the second largest element.


# Solution 1
def second_largest_element(array: list[int]):
    array.sort()
    return array[-2]


# Solution 2
def second_largest_element(array: list[int]):
    pass


range(2,-1,-1)



lists = [13, -2, 37, 4, 59, 696, 9]


second_largest_array = second_largest_element(lists)
print(second_largest_array)