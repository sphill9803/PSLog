'''
미로탐색
https://www.acmicpc.net/problem/2178
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def BFS(start):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    bfs_queue = deque([start])
    visited[start[0]][start[1]] = 1
    while bfs_queue:
        current = bfs_queue.popleft()
        cx, cy = current[0], current[1]
        cd = visited[cx][cy]
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 1 <= nx <= N and 1 <= ny <= M and visited[nx][ny] == 0 and graph[nx][ny] == '1':
                if (nx, ny) == (N, M):
                    return cd + 1
                visited[nx][ny] = cd + 1
                bfs_queue.append((nx, ny))


N, M = map(int, input().split())
graph = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    maze_str = input().strip()
    for j in range(1, M + 1):
        graph[i][j] = maze_str[j - 1]

visited = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

print(BFS((1, 1)))