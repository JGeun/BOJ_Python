import sys
N = int(sys.stdin.readline())
timeTable = []
for _ in range(N):
    timeTable.append(list(map(int, sys.stdin.readline().split())))

timeTable.sort(key=lambda x: (x[1], x[0]))

count = 0
endTime = 0
for i in range(N):
     if endTime <= timeTable[i][0]:
         count += 1
         endTime = timeTable[i][1]

sys.stdout.write(str(count)+'\n')