'''
배열 합치기
https://www.acmicpc.net/problem/11728
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
merged_list = []
a_ptr, b_ptr = 0, 0

while a_ptr < N and b_ptr < M:
    if list_A[a_ptr] <= list_B[b_ptr]:
        merged_list.append(list_A[a_ptr])
        a_ptr += 1
    else:
        merged_list.append(list_B[b_ptr])
        b_ptr += 1

if a_ptr < N:
    for i in range(a_ptr, N):
        merged_list.append(list_A[i])
if b_ptr < M:
    for i in range(b_ptr, M):
        merged_list.append(list_B[i])

print(*merged_list)