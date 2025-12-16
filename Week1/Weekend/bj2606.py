'''
바이러스
https://www.acmicpc.net/problem/2606
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def BFS(graph, start):
    mal_cpus = 0
    bfs_queue = deque([start])
    visited[start] = True
    while bfs_queue:
        current = bfs_queue.popleft()
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                bfs_queue.append(node)
                mal_cpus += 1
    return mal_cpus


V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (V + 1)

print(BFS(graph, 1))