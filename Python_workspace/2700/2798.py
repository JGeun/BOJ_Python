# 1번

# N, M = map(int, input().split())
# cardList = list(map(int, input().split()))
# maxSum = 0
# for i in range(len(cardList)):
#     for j in range(i+1, len(cardList)):
#         for k in range(j+1, len(cardList)):
#             if maxSum < cardList[i]+cardList[j]+cardList[k] <= M:
#                 maxSum = cardList[i]+cardList[j]+cardList[k]
#
# print(maxSum)

from itertools import combinations
N, M = map(int, input().split())
cardList = list(map(int, input().split()))
maxSum = 0

for cards in combinations(cardList, 3):
    cardSum  = sum(cards)
    if maxSum < cardSum <= M:
        maxSum = cardSum
print(maxSum)