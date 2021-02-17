from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        queue.insert(0, command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue.popleft()+'\n')
    elif command[0] == 'pop_back':
        if len(queue) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue.pop()+'\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(queue))+'\n')
    elif command[0] == 'empty':
       if len(queue) == 0:
           sys.stdout.write('1\n')
       else:
           sys.stdout.write('0\n')
    elif command[0] == 'front':
        if len(queue) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(queue[0])+'\n')

    elif command[0] == 'back':
        if len(queue) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(queue[len(queue)-1])+'\n')