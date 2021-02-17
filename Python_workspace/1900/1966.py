import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    queue = [num for num in nums]
    findValue = nums[M]
    queue[M] = 'check'
    nums.sort()
    count = 1
    index = len(nums)-1
    while nums[index] != findValue:
        if queue[0] != nums[index]:
            queue.append(queue.pop(0))
        else:
            queue.pop(0)
            count += 1
            index -= 1

    for i in range(len(queue)):
        if queue[i] == findValue:
            count += 1
        elif queue[i] == 'check':
            sys.stdout.write(str(count)+'\n')
            break
