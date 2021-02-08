def print_star(star, x, y, n):
    if n == 1:
        star[y][x] = 1
        return
    else:
        n //= 3
        for i in range(0, 3):
            for j in range(0, 3):
                if i == 1 and j == 1:
                    continue
                print_star(star, x+(j*n), y+(n*i), n)


N = int(input())
star = [[0 for col in range(N)] for row in range(N)]
print_star(star, 0, 0, N)

for i in range(0, N):
    for j in range(0, N):
        if star[i][j] == 1:
            print("*", end='')
        else:
            print(' ', end='')
    print()
