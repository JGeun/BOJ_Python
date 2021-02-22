import sys
while True:
    M, N = map(int, sys.stdin.readline().split())
    if M == 0 and N == 0:
        break
    if N%M == 0:
        sys.stdout.write('factor\n')
    elif M%N == 0:
        sys.stdout.write('multiple\n')
    else:
        sys.stdout.write('neither\n')