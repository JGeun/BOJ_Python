import sys

def stack_sequence(n):
    index = 0
    stack = []
    result = []
    for _ in range(0, n):
        checkNUM = int(sys.stdin.readline())

        while index < checkNUM:
            index += 1
            stack.append(index)
            result.append('+')

        if stack[-1] == checkNUM:
            stack.pop()
            result.append('-')
        else:
            print("NO")
            return False
    print('\n'.join(result))
    return True

# 2번째 방법
# n = int(sys.stdin.readline())
# stack_sequence(n)
#
# import sys
# n = int(sys.stdin.readline())
#
# checkList = []
# for _ in range(n):
#     checkList.append(int(sys.stdin.readline()))
#
# index = 0
# stack = []
# result = []
# for i in range(1, n+1):
#     stack.append(i)
#     result.append('+')
#     while len(stack) != 0 and stack[len(stack)-1] == checkList[index]:
#         stack.pop()
#         result.append('-')
#         index += 1
#
# if len(stack) != 0:
#     sys.stdout.write("No\n")
# else:
#     for char in result:
#         sys.stdout.write(char+"\n")
