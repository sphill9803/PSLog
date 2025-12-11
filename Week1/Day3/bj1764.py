'''
듣보잡
https://www.acmicpc.net/problem/1764
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

non_heard, non_seen = set(), set()

for _ in range(N):
    non_heard.add(input().strip())

for _ in range(M):
    non_seen.add(input().strip())

result = sorted(list(non_heard & non_seen)) # set에서 &는 intersection 연산자임.

print(len(result))

for name in result:
    print(name)