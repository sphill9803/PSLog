'''
토마토
https://www.acmicpc.net/problem/7576
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline
# 방향 벡터 전역 설정
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(start_pts):
    q = deque(start_pts)
    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            next_r, next_c = curr_r + dr[i], curr_c + dc[i]
            if 0 <= next_c < Cols and 0 <= next_r < Rows and graph[next_r][next_c] == 0:
                graph[next_r][next_c] = graph[curr_r][curr_c] + 1
                q.append((next_r, next_c))

Cols, Rows = map(int, input().split())

graph = []

for _ in range(Rows):
    graph.append(list(map(int, input().split())))

start_points = []

for r in range(Rows):
    for c in range(Cols):
        if graph[r][c] == 1:
            start_points.append((r, c))

bfs(start_points)
is_possible = True
min_day = 0
for r in range(Rows):
    for c in range(Cols):
        if graph[r][c] == 0:
            print(-1)
            exit()
        min_day = max(min_day, graph[r][c])

print(min_day - 1)