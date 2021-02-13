import sys

N, K = map(int, sys.stdin.readline().split())
queue = [int(i) for i in range(1, N+1)]
result = []
count = 0
index = 0

while len(queue) > 1:
    print(index, queue[index])
    index = (index + 1) % len(queue)
    if queue[index] != 0:
        count += 1
        if count == K-1:
            print("count 성립")
            num = queue[index]
            result.append(num)
            queue.remove(num)
            count = 0

result.append(queue.pop())
sys.stdout.write('<')
sys.stdout.write(' '.join(map(str, result)))
sys.stdout.write('>')
