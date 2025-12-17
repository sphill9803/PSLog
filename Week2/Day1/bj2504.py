'''
괄호의 값
https://www.acmicpc.net/problem/2504
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

brackets_str = input().strip()
brackets_stack = []

brackets = {')' : ['(', 2], ']' : ['[', 3]}

is_valid = True

for b in brackets_str:
    if b in '([':
        brackets_stack.append(b)
    else:
        if not brackets_stack:
            is_valid = False
            break
        if brackets_stack[-1] == brackets[b][0]:
            brackets_stack.pop()
            brackets_stack.append(brackets[b][1])
        elif type(brackets_stack[-1]) == int:
            temp = 0
            while brackets_stack:
                if type(brackets_stack[-1]) == int:
                    temp += brackets_stack.pop()
                else:
                    break
            if not brackets_stack or brackets_stack[-1] != brackets[b][0]:
                is_valid = False
                break
            brackets_stack.pop()
            brackets_stack.append(temp * brackets[b][1])
        else:
            is_valid = False
            break
temp = 0
for b in brackets_stack:
    if type(b) == int:
        temp += b
    else:
        is_valid = False
        break

if is_valid:
    print(temp)
else:
    print(0)