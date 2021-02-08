import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    length = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    if length == 0 and abs(r2-r1) == 0:
        print(-1)
    elif length == 0 and abs(r2-r1) != 0:
        print(0)
    elif length == r1+r2 or length == abs(r2-r1): #두 원의 접점이 하나일 경우
        print(1)
    elif abs(r2-r1) < length < r1+r2:
        print(2)
    else:
        print(0)