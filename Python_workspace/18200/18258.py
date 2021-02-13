from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            sys.stdout.write(str(queue.popleft()) + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(queue)) + '\n')
    elif command[0] == 'empty':
        if queue:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    elif command[0] == 'front':
        if queue:
            sys.stdout.write(str(queue[0]) + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'back':
        if queue:
            sys.stdout.write(str(queue[len(queue) - 1]) + '\n')
        else:
            sys.stdout.write('-1\n')
