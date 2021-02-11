def is_vps(parenthesis):
    checkList = []
    for ps in parenthesis:
        if ps == "(":
            checkList.append(ps)
        elif ps == ")" and len(checkList) != 0 and checkList[len(checkList)-1] == "(":
            checkList.pop()
        else:
            return False

    if len(checkList) != 0:
        return False
    else:
        return True

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    parenthesis = sys.stdin.readline().rstrip()
    if is_vps(parenthesis):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")