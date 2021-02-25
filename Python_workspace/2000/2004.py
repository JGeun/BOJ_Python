import sys
import math

# n, m = map(int, sys.stdin.readline().split())
# factorialStr = str(math.factorial(n) // math.factorial(n-m) // math.factorial(m))
# count = 0
# for i in range(1, len(factorialStr)):
#     if factorialStr[-i] == '0':
#         count += 1
#     else:
#         sys.stdout.write(str(count)+'\n')
#         break

for n in range(1, 101):
    print("{} fac 시작".format(n))
    for i in range(n+1):
        print(math.factorial(n) // math.factorial(n-i) // math.factorial(i))