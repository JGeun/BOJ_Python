import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    queue = [num for num in nums]
    findValue = nums[M]
    nums.sort()
    count = 0
    index = len(nums)-1
    while nums[index] != findValue:
        if queue[0] != nums[index]:
            queue.append(queue[0])
            queue.remove(queue[0])
        else:
            queue.remove(queue[0])
            count += 1

