'''
색종이
https://www.acmicpc.net/problem/2563
'''

"""
핵심은 -> 검은색 종이가 들어간다는 것을 1로 쓴다고 치환해서 생각하는 것.
"""

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

w_paper = [[0 for _ in range(100)] for _ in range(100)] # 100 * 100 배열 생성

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10): # 조건에 맞게 1 채워넣기
        for j in range(y, y + 10):
            w_paper[i][j] = 1

b_squares = 0
for s in w_paper: # 1의 개수 = 검은색 지역의 넓이이다.
    b_squares += s.count(1)

print(b_squares)