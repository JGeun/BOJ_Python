import sys
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    n = int(sys.stdin.readline())
    nums.append(n)

# 산술평균
print(round(sum(nums) / N))

# 중앙값
nums.sort()
print(nums[N // 2])

from collections import Counter
countArray = Counter(nums).most_common()
if len(countArray) > 1:
    if countArray[0][1] == countArray[1][1]:
        print(countArray[1][0])
    else:
        print(countArray[0][0])
else:
    print(countArray[0][0])
# frequency = []
# index = 0
# for i in range(len(nums)):
#     if len(frequency) == 0:
#         frequency.append([nums[i], nums.count(nums[i])])
#     elif frequency[len(frequency) - 1][0] != nums[i]:
#         frequency.append([nums[i], nums.count(nums[i])])
# frequency.sort(key=lambda x: (-x[1], x[0]))
# if len(frequency) > 1 and frequency[0][1] == frequency[1][1]:
#     print(frequency[1][0])
# else:
#     print(frequency[0][0])

# 범위
print(nums[N - 1] - nums[0])
