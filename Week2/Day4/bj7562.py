'''
나이트의 이동
https://www.acmicpc.net/problem/7562
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

T = int(input())

dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [2, -2, 1, -1, 2, -2, 1, -1]

def knight_bfs(start, target):
    if start == target: # 연산량을 가볍게 하기 위한 엣지케이스
        return
    q = deque([start])
    while q:
        cr, cc = q.popleft()
        curr_d = board[cr][cc]
        for i in range(8):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < I and 0 <= nc < I and board[nr][nc] == -1:
                board[nr][nc] = curr_d + 1
                if nr == target[0] and nc == target[1]:
                    return
                q.append((nr, nc))


for t in range(T):
    I = int(input())
    board = [[-1 for _ in range(I)] for _ in range(I)]
    sr, sc= map(int, input().split())
    board[sr][sc] = 0
    tr, tc = map(int, input().split())
    knight_bfs((sr, sc), (tr, tc))
    print(board[tr][tc])
