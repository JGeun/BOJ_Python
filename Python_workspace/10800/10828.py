import sys
N = int(sys.stdin.readline())
numList = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        numList.append(int(command[1]))
    elif command[0] == 'pop':
        if len(numList) != 0:
            sys.stdout.write(str(numList.pop())+"\n")
        else:
            sys.stdout.write(str(-1)+"\n")
    elif command[0] == 'size':
        sys.stdout.write(str(len(numList))+ "\n")
    elif command[0] == 'empty':
        if len(numList) == 0:
            sys.stdout.write(str(1)+"\n")
        else:
            sys.stdout.write(str(0)+"\n")
    elif command[0] == 'top':
        if len(numList) != 0:
            sys.stdout.write(str(numList[len(numList)-1]) + "\n")
        else:
            sys.stdout.write(str(-1)+'\n')
