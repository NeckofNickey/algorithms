check_num = 204

for n in range(1, 1000):

    n_bin = bin(n)[2:]

    for _ in range(2):

        ones_count = n_bin.count("1")

        if ones_count % 2 == 0:
            n_bin += "0"
        else:
            n_bin += "1"

    r = int(n_bin, 2)

    if r > check_num:
        print(r)
        break

    