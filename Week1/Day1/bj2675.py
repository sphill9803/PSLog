'''
문자열 반복
https://www.acmicpc.net/problem/2675
'''

import sys

sys.stdin = open("../../input.txt", "r")

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, S = input().split()
    N = int(N)
    target_S = ""
    for s in S:
        target_S += (s * N)
    print(target_S)
