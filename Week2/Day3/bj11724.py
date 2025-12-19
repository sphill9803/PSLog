'''
연결 요소의 개수
https://www.acmicpc.net/problem/11724
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    while q:
        curr_v = q.popleft()
        for next_v in graph[curr_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)

V, E = map(int, input().split())

graph = [[] for _ in range(V)]
visited = [False for _ in range(V)]

for e in range(E):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)

connected = 0

for v in range(V):
    if not visited[v]:
        visited[v] = True
        bfs(v)
        connected += 1
print(connected)