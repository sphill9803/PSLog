'''
N과 M(1)
https://www.acmicpc.net/problem/15649
'''

import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

q = deque()
p_set = deque([i for i in range(1, N+1)])
used = [False for i in range(N+1)]
ans = []
def permutation(K):
    if K == 0:
        ans.append(list(q))
        return
    for p in p_set:
        if not used[p]:
            q.append(p)
            used[p] = True
            permutation(K-1)
            used[p] = False
            q.pop()
permutation(M)
ans.sort()
for a in ans:
    print(*a)