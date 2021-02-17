from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
checkList = list(map(int, sys.stdin.readline().split()))
queue = deque()
for i in range(1, N + 1):
    queue.append(int(i))

count = 0
while len(checkList) != 0:
    if queue[0] == checkList[0]:
        queue.popleft()
        checkList.pop(0)
    else:
        index = queue.index(checkList[0])
        if len(queue) // 2 >= index:
            while queue[0] != checkList[0]:
                queue.append(queue.popleft())
                count += 1
        else:
            while queue[0] != checkList[0]:
                num = queue.pop()
                queue.insert(0, num)
                count += 1
sys.stdout.write(str(count)+'\n')
