'''
평균
https://www.acmicpc.net/problem/1546
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
avg_score = 0.0
for s in score_list:
    avg_score += (s * 100 / max_score)
print(avg_score / N)