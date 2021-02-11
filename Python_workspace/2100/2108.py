N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
print(round(sum(nums)/N, 0))
nums.sort()
print(nums[N//2])

print(nums[N-1]-nums[0])