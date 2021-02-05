index = 0
maxNum = 0
for i in range(9):
    num = int(input())
    if num > maxNum:
        maxNum = num
        index = i
print(maxNum)
print(index+1)
