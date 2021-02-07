import sys


def get_bigger(nums):
    for i in range(2, -1, -1):
        if int(nums[0][i]) > int(nums[1][i]):
            return nums[0]
        elif int(nums[0][i]) < int(nums[1][i]):
            return nums[1]
    return nums[0]


nums = sys.stdin.readline().rstrip().split()
print(get_bigger(nums)[::-1])
