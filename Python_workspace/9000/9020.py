length = 10000*2
primeList = [1]*(length+1)
for i in range(2, length+1):
    if primeList[i] == 1:
        for j in range(2, length//i+1):
            primeList[i*j] = 0

T = int(input())
for _ in range(T):
    n = int(input())
    p1 = 2; p2 = 5000
    for i in range(2, n//2+1):
        A = i; B = n-i
        if i != 1 and primeList[A] == 1 and primeList[B] == 1:
            if p2-p1 > B-A:
                p1 = A; p2 = B
    print(p1, p2)
