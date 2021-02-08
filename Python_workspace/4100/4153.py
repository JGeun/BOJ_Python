import math

while True:
    listNum = sorted(list(map(int, input().split())))
    if listNum[0] == 0 and listNum[1] == 0 and listNum[2] == 0:
        break
    if math.pow(listNum[2], 2) == math.pow(listNum[1],2) + math.pow(listNum[0],2):
        print("right")
    else:
        print("wrong")
