'''
촌수계산
https://www.acmicpc.net/problem/2644
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())

visited = [-1 for _ in range(N)]
family = [[] for _ in range(N)]

def bfs(start, target):
    q = deque([start])
    visited[start] = 0
    while q:
        curr_family = q.popleft()
        curr_relation = visited[curr_family]
        for next_family in family[curr_family]:
            if visited[next_family] == -1:
                visited[next_family] = curr_relation + 1
                q.append(next_family)
    return visited[target]



for _ in range(M):
    x, y = map(int, input().split())
    family[x - 1].append(y - 1)
    family[y - 1].append(x - 1)

print(bfs(A - 1, B - 1))