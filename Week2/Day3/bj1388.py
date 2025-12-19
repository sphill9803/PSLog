'''
바닥장식
https://www.acmicpc.net/problem/1388
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

tiles = [list(input().strip()) for _ in range(N)]

woods = 0

for i in range(N):
    for j in range(M):
        if tiles[i][j] == '-':
            woods += 1
            tiles[i][j] = '+'
            for k in range(j+1, M):
                if tiles[i][k] != '-':
                    break
                tiles[i][k] = '+'
        elif tiles[i][j] == '|':
            woods += 1
            tiles[i][j] = '+'
            for k in range(i+1, N):
                if tiles[k][j] != '|':
                    break
                tiles[k][j] = '+'
print(woods)
