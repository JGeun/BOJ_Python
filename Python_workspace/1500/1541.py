import sys
import re

exp = sys.stdin.readline().rstrip()
numList = list(map(int, re.findall("\d+", exp)))
operList = re.findall('-|\+', exp)
expCalc = 0
if operList.count('-') != 0:
    index = operList.index('-')
    for i in range(index+1, len(numList)):
        numList[i] = -1 * numList[i]
sys.stdout.write(str(sum(numList))+'\n')