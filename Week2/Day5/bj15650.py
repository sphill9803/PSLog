'''
N과 M(2)
https://www.acmicpc.net/problem/15650
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

q = deque()
used = [False for i in range(N+1)]
ans = []
def permutation(K):
    if K == 0:
        ans.append(list(q))
        return
    for p in range(1, N+1):
        if not used[p]:
            if len(q) > 0 and q[-1] >= p:
                continue
            q.append(p)
            used[p] = True
            permutation(K - 1)
            used[p] = False
            q.pop()

permutation(M)

ans.sort()
for a in ans:
    print(*a)