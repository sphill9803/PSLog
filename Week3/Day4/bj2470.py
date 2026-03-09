'''
두 용액
https://www.acmicpc.net/problem/2470
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
liquids = sorted(map(int, input().split()))

left, right = 0, N - 1
ans, ans_liqs = float('inf'), []
while left < right:
    liq_A, liq_B = liquids[left], liquids[right]
    current_sum = liq_A + liq_B
    if abs(current_sum) <= ans:
        ans_liqs = [liq_A, liq_B]
        ans = abs(current_sum)
    if current_sum <= 0:
        left += 1
    else:
        right -= 1

print(*ans_liqs)
