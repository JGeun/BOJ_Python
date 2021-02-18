import sys
N = int(sys.stdin.readline())
person = sorted(list(map(int, sys.stdin.readline().split())))
waitTime = 0
for i in range(0, N):
    waitTime += person[i]*(N-i)
sys.stdout.write(str(waitTime)+'\n')