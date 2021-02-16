import sys

N, K = map(int, sys.stdin.readline().split())
queue = [int(i) for i in range(1, N+1)]
result = []
count = 0

sys.stdout.write('<')
while len(queue) > 1:
    count += 1
    if count == K:
        count = 0
        sys.stdout.write(str(queue[0])+", ")
        queue.remove(queue[0])
    else:
        queue.append(queue[0])
        queue.remove(queue[0])
sys.stdout.write(str(queue.pop())+'>')
