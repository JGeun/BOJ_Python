N = int(input())

index = 2
while N != 1:
    while N % index == 0:
        print(index)
        N //= index
    index += 1

