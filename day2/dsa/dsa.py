# DSA

"""
you are given  a list of integers and the orer of the elements would be increasing and then decreasing. your task is to find the peak (highest) of that order

eg:
5,3,6 4,2,0
Output: 6 because 6 is the peak (highest).



edge cases:
if value is decreasing only:
    eg: 4,3,2,1,0

then peak would be 4 and increasing case too.

and if array is empty then return -1
"""


def find_peak(dsa_list: list[int]):
    if not dsa_list:
        return -1
    # Step 1 --- find the mid value
    length = len(dsa_list)
    peak_value = dsa_list[0]
    mid_idx = length // 2 - 1
    if length % 2 == 0:
        prev_mid = dsa_list[mid_idx]
        next_mid = dsa_list[mid_idx + 1]
        if prev_mid >= next_mid:
            peak_value = prev_mid
        else:
            peak_value = next_mid
    else:
        peak_value = dsa_list[mid_idx]

    print(peak_value)

    return peak_value


lists = [5, 3, 6, 5, 4, 2, 0]

peak_value = find_peak(lists)
print(peak_value)


# What i now feel that, it just a way to find the highest value na ? that's nonnsense. just find the highest value what .
