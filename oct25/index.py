# Bin2Dec


def binary_to_dec(bin: int) -> int:
    str_bin = str(bin)
    length = len(str_bin) - 1

    dec = 0
    for i, _ in enumerate(str_bin):
        value = str_bin[length - i]
        print(int(value) * pow(2, i), "index=", i)
        dec = int(value) * pow(2, i) + dec

    print(dec)


binary_to_dec(1101)
