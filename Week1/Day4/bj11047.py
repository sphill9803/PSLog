'''
동전 0
https://www.acmicpc.net/problem/11047
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

num_coins = 0
for c in reversed(coins):
    if K >= c:
        num_coins += K // c
        K = K % c

print(num_coins)