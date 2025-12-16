'''
N-Queen
https://www.acmicpc.net/problem/9663
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

def isValidQueen(queens):
    current_row = len(queens) - 1  # 방금 놓은 퀸의 행
    current_col = queens[-1]  # 방금 놓은 퀸의 열

    # 이전 퀸들과 비교
    for row in range(current_row):
        col = queens[row]
        # 열이 같거나 (이미 윗단에서 걸러지긴 함)
        # 대각선 차이가 같으면 (행 차이 == 열 차이 절댓값)
        if col == current_col or abs(current_row - row) == abs(current_col - col):
            return False
    return True

def findQueen(idx, queens):
    ans = 0
    if idx == 0:
        return 1

    for i in range(N):
        queens.append(i)
        if isValidQueen(queens):
            ans += findQueen(idx - 1, queens)
        queens.pop()
    return ans

print(findQueen(N, []))