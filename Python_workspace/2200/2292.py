N = int(input())
std = 6
block = 1

while N > block:
    block += std
    std += 6

print((std-6) // 6 +1)