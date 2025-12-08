'''
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
'''

"""
핵심은 -> 완성된 체스판과 비교해보면서 최소 개수 구하면 된다.
"""

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
A, B = "WBWBWBWB", "BWBWBWBW"

board_A = [A, B, A, B, A, B, A, B]

board = []
for _ in range(N):
    board.append(input().strip())

min_count = 64 # 어차피 맥스로 뒤집는 건 64개임
count_A = 0

for i in range(N-7):
    for j in range(M-7):
        count_A = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != board_A[k][l]:
                    count_A += 1
        min_count = min(count_A, 64 - count_A, min_count) # 체스판은 64개라서 뒤집는 경우의 수면 64 - count 하면 대칭 형태가 됨.


print(min_count)
