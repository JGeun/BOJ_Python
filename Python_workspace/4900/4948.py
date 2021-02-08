length = 123456*2
primeList = [1]*(length+1)
for i in range(2, length+1):
    if primeList[i] == 1:
        for j in range(2, length//i+1):
            primeList[i*j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):
        if i != 1 and primeList[i] == 1:
            count += 1
    print(count)