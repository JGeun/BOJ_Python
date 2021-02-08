M, N = map(int, input().split())
primeList = [1]*(N+1)

for i in range(2, N):
    if primeList[i] == 1:
        for j in range(2, N//i+1):
            primeList[i*j] = 0

for i in range(M, N+1):
    if i != 1 and primeList[i] == 1:
        print(i)