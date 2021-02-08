def listcheck(listPos, n):
    if n in listPos:
        listPos.remove(n)
    else:
        listPos.append(n)


listX = []
listY = []

for _ in range(3):
    X, Y = map(int, input().split())
    listcheck(listX, X)
    listcheck(listY, Y)

print(listX[0], listY[0])
