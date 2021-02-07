X = int(input())

order = 1
sumOrder = 0

while X > sumOrder + order:
    sumOrder += order
    order += 1

if order % 2 != 0:
    print("{}/{}".format(order+1 - (X - sumOrder), (X - sumOrder)))
else:
    print("{}/{}".format((X - sumOrder), order + 1 - (X - sumOrder)))


