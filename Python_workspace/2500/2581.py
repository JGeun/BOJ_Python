def get_prime(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


M = int(input())
N = int(input())
sum = 0
minPrime = -1

for i in range(M, N+1):
    if get_prime(i):
        sum += i
        if minPrime == -1:
            minPrime = i

if sum != 0:
    print(sum)
print(minPrime)
