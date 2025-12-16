'''
DFS와 BFS
https://www.acmicpc.net/problem/1260
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def DFS(graph, start):
    if not visited[start]:
        visited[start] = True
        visited_queue.append(start)
        for node in graph[start]:
            DFS(graph, node)


def BFS(graph, start):
    bfs_queue = deque([start])
    visited[start] = True
    while bfs_queue:
        current = bfs_queue.popleft()
        visited_queue.append(current)
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                bfs_queue.append(node)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [False] * (N + 1)
visited_queue = []
DFS(graph, V)
print(*visited_queue)

visited = [False] * (N + 1)
visited_queue = []
BFS(graph, V)
print(*visited_queue)
