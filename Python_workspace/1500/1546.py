N = int(input())
arr = sorted(list(map(int, input().split())))
sum = 0
for i in range(0, len(arr)):
    sum += arr[i] * 100 / arr[len(arr)-1]
print(sum/N)
