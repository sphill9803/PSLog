'''
공유기 설치
https://www.acmicpc.net/problem/2110
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_nums = [0]
for i in range(N):
    sum_nums.append(sum_nums[i] + nums[i])

for _ in range(M):
    n_left, n_right = map(int, input().split())
    print(sum_nums[n_right] - sum_nums[n_left - 1])