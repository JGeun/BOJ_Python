def is_hansu(n):
    if n < 10:
        return True
    else:
        dif = int(str(n)[1]) - int(str(n)[0])
        for i in range(2, len(str(n))):
             if not dif == int(str(n)[i]) - int(str(n)[i-1]):
                 return False
        return True

N = int(input())
count = 0
for i in range(1, N+1):
    if is_hansu(i):
        count += 1
print(count)