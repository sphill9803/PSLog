'''
스택
https://www.acmicpc.net/problem/10828
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    commands = list(input().split())
    if commands[0] == "push":
        stack.append(int(commands[1]))
    elif commands[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == "size":
        print(len(stack))
    elif commands[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
