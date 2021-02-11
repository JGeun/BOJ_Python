import sys
N = int(input())
nums = [0]*10000
for _ in range(N):
    nums[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if nums[i] > 0:
        for _ in range(nums[i]):
            sys.stdout.write(str(i+1)+"\n") #pypy3의 경우
            #print(i+1) - 그냥 python3으로 채점할 경우