'''
적록색약
https://www.acmicpc.net/problem/10026
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

normal_board = []
weak_board = []

for _ in range(N):
    board_str = input().strip()
    normal_board.append(list(board_str))
    weak_board.append(list(board_str.replace('R', 'G')))

def normal_BFS(start, c_str):
    q = deque([start])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and normal_board[nx][ny] == c_str:
                q.append((nx, ny))
                normal_board[nx][ny] = 'W'

def weak_BFS(start, c_str):
    q = deque([start])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and weak_board[nx][ny] == c_str:
                q.append((nx, ny))
                weak_board[nx][ny] = 'W'

counts = [0, 0]

for i in range(N):
    for j in range(N):
        normal_str = normal_board[i][j]
        weak_str = weak_board[i][j]
        if normal_str != 'W':
            normal_board[i][j] = 'W'
            normal_BFS((i, j), normal_str)
            counts[0] += 1
        if weak_str != 'W':
            weak_board[i][j] = 'W'
            weak_BFS((i, j), weak_str)
            counts[1] += 1

print(*counts)