T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = [num for num in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])