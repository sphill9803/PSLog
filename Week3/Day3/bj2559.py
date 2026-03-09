'''
수열
https://www.acmicpc.net/problem/2559
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))
sum_temps = sum(temps[0:K])
ans = sum_temps
h, t = 0, K - 1
while t < N - 1:
    t += 1
    sum_temps = sum_temps + temps[t] - temps[h]
    h += 1
    if ans < sum_temps:
        ans = sum_temps

print(ans)