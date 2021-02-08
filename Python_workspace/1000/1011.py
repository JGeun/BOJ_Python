T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    length = y-x
    std = 1
    while std**2 <= length:
        std += 1

    if (std - 1) ** 2 == length:
        print((std-1)**2 - (std-2)**2)
    else:
        value = std**2 - (std-1)**2
        if std**2 - std >= length:
            print(value-1)
        else:
            print(value)
