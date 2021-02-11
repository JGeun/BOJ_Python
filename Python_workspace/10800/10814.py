import sys

N = int(sys.stdin.readline())
users = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    users.append([int(age), name])
users.sort(key=lambda x: (x[0]))

for user in users:
    sys.stdout.write("{} {}\n".format(user[0], user[1]))