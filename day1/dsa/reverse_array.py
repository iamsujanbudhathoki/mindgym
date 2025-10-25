def reverse_array(array: list[int]):
    length = len(array)
    for idx in range(length // 2):  # only loop until the middle
        new_idx = length - idx - 1

        # swap
        array[idx], array[new_idx] = array[new_idx], array[idx]

    print(array)


lists = [13, -2, 37, 4, 59, 696, 9]
reverse_array(lists)