C = int(input())
for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1
    print("{:.3f}%".format(count / nums[0] * 100))