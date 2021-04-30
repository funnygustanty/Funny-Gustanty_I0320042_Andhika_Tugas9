A = [
                [23,11,54,38,76],
                [14,12,28,22,21],
                [10,13,18,17,24],
                [35,33,39,32,29]
        ]

# mengakses elemen array dua dimensi
for baris in A:
    for nilai in baris:
        print("%d " % nilai, end='')
    print()