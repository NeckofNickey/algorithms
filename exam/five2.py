check_num = 116

for n in range(1, 1000):

    n_bin = bin(n)[2:]

    count_ones = n_bin.count("1")

    if count_ones % 2 == 0:
        n_bin = "11" + n_bin
    else:
        n_bin += "00"

    num = int(n_bin, 2)

    if num > check_num:
        print(n)
        break