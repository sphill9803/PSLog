'''
부분합
https://www.acmicpc.net/problem/1806
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, S = map(int, input().split())
seqs = list(map(int, input().split()))

left = 0
current_sum = 0
ans = float('inf')

for right in range(N):
    current_sum += seqs[right]
    while current_sum >= S:
        ans = min(ans, right - left + 1)
        current_sum -= seqs[left]
        left += 1

print(0 if ans == float('inf') else ans)