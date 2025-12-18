'''
회전하는 큐
https://www.acmicpc.net/problem/1021
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

q = deque(i + 1 for i in range(N))

targets = list(map(int, input().split()))

cmds = 0

idx = 0

while q:
    if idx == M:
        break
    if targets[idx] == q[0]:
        idx += 1
        q.popleft()
    else:
        q_idx = 0
        while targets[idx] != q[q_idx]:
            q_idx += 1
            if targets[idx] == q[q_idx]:
                break
        if q_idx >= len(q) / 2:
            q.rotate(len(q) - q_idx)
            cmds += (len(q) - q_idx)
        else:
            q.rotate(-q_idx)
            cmds += q_idx

print(cmds)