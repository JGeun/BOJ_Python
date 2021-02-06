N = input()
cycle = N;
count = 0
while True:
    if len(cycle) < 2:
        cycle = "0" + cycle
    cycle = cycle[1]+str((int(cycle[0])+int(cycle[1]))%10)
    count += 1
    if int(N) == int(cycle):
        print(count)
        break