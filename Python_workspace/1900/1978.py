def prime(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(len(nums)):
    if prime(nums[i]):
        count += 1
print(count)
