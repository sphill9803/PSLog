'''
오큰수
https://www.acmicpc.net/problem/17298
'''
import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

A_seq = deque(list(map(int, input().split())))

NGE_stack = deque()
NGE_seq = []
for i in range(N - 1, -1, -1):
    if len(NGE_stack) == 0:
        NGE_stack.append(A_seq[i])
        NGE_seq.append(i)
    else:
        seq_cnt = NGE_seq[-1]
        while NGE_stack and NGE_stack[-1] < A_seq[i]:
            NGE_stack.pop()
        NGE_stack.append(A_seq[i])
        NGE_seq.append(i)

print(NGE_seq)