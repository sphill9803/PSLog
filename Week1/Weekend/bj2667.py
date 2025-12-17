'''
단지번호붙이기
https://www.acmicpc.net/problem/2667
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def BFS(start):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    bfs_queue = deque([start])
    graph[start[0]][start[1]] = '0'
    apt_cnt = 1
    while bfs_queue:
        current = bfs_queue.popleft()
        cx, cy = current[0], current[1]
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1':
                bfs_queue.append((nx, ny))
                apt_cnt += 1
                graph[nx][ny] = '0'
    return apt_cnt

N = int(input())
graph, apts = [], []
for i in range(N):
    graph.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            apts.append(BFS((i, j)))

apts.sort()
print(len(apts))
for apt in apts:
    print(apt)