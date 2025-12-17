'''
유기농배추
https://www.acmicpc.net/problem/1012
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline
# 방향 벡터 전역 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    graph[start_r][start_c] = 0 # 방문 처리
    
    while q:
        curr_r, curr_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = curr_r + dx[i], curr_c + dy[i]
            
            # 범위 체크 & 배추 확인
            if 0 <= next_r < N and 0 <= next_c < M and graph[next_r][next_c] == 1:
                graph[next_r][next_c] = 0
                q.append((next_r, next_c))
    return 1

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split()) # M(가로), N(세로)
    
    # 2차원 배열 초기화 (N행 M열)
    graph = [[0] * M for _ in range(N)]

    # 배추 심기
    for _ in range(K):
        c, r = map(int, input().split()) # 문제의 X(가로), Y(세로)
        graph[r][c] = 1 # graph[행][열]

    bug_cnt = 0
    # 전체 맵 탐색
    for r in range(N):     # 행(세로)
        for c in range(M): # 열(가로)
            if graph[r][c] == 1:
                bug_cnt += bfs(r, c)

    print(bug_cnt)
