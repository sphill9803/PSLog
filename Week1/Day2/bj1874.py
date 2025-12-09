'''
스택 수열
https://www.acmicpc.net/problem/1874
'''
import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

origin_state = deque([(i + 1) for i in range(N)])
stack = deque()
push_count = []

fail_state = False

for _ in range(N):
    target_num = int(input())
    if len(stack) == 0:
        push_count.append('+')
        stack.append(origin_state.popleft())
    while target_num > stack[-1]:
        push_count.append('+')
        stack.append(origin_state.popleft())
    if target_num == stack[-1]:
        push_count.append('-')
        stack.pop()
    else:
        fail_state = True
        break

if fail_state:
    print("NO")
else:
    for p in push_count:
        print(p)