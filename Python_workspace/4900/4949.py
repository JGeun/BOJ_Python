def is_vps(sentence):
    checkList = []
    for letter in sentence:
        if letter == "(" or letter == "[":
            checkList.append(letter)
        elif letter == ')':
            if len(checkList) != 0 and checkList[len(checkList) - 1] == '(':
                checkList.pop()
            else:
                return False
        elif letter == ']':
            if len(checkList) != 0 and checkList[len(checkList) - 1] == '[':
                checkList.pop()
            else:
                return False
    if len(checkList) != 0:
        return False
    else:
        return True

import sys
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    if is_vps(sentence):
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")