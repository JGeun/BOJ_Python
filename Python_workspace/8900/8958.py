T = int(input())
for i in range(T):
    quiz = input()
    score = 0
    count = 1
    for q in quiz:
        if q == "O":
            score += count
            count += 1
        else:
            count = 1
    print(score)