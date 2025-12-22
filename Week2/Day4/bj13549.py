'''
숨바꼭질3
https://www.acmicpc.net/problem/13549
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 10 ** 6

visited = [-1 for _ in range(MAX + 1)]

def bfs(curr):
    visited[curr] = 0
    q = deque([curr])
    while q:
        v = q.popleft()
        curr_level = visited[v]
        if v == K:
            return curr_level
        for nv in (v - 1, v + 1, 2 * v):
            if 0 <= nv <= MAX and visited[nv] == -1:
                if nv  ==  2 * v:
                    visited[nv] = curr_level
                    q.appendleft(nv)
                else:
                    visited[nv] = curr_level + 1
                    q.append(nv)

print(bfs(N))