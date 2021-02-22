import sys
N = int(sys.stdin.readline())
list = sorted(list(map(int, sys.stdin.readline().split())))
sys.stdout.write(str(list[0]*list[-1])+'\n')