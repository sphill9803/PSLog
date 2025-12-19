'''
섬의 개수
https://www.acmicpc.net/problem/4963
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

W, H = map(int, input().split())

dw = [0, 0, 1, 1, 1, -1, -1, -1]
dh = [1, -1, 0, 1, -1, 0, 1, -1]

def bfs(start):
    q = deque([start])
    while q:
        ch, cw = q.popleft()
        for i in range(8):
            nh, nw = ch + dh[i], cw + dw[i]
            if 0 <= nh < H and 0 <= nw < W and island_map[nh][nw] == 1:
                island_map[nh][nw] = 0
                q.append((nh, nw))


while W + H > 0:
    island_map = [list(map(int, input().split())) for _ in range(H)]
    islands = 0
    for h in range(H):
        for w in range(W):
            if island_map[h][w] == 1:
                island_map[h][w] = 0
                bfs((h, w))
                islands += 1
    print(islands)
    W, H = map(int, input().split())