'''
나무 자르기
https://www.acmicpc.net/problem/2805
'''
import sys

sys.stdin = open("../../input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

def find_length(start, end):
    ans = 0
    while start <= end:
        lan_len = (start + end) // 2
        lan_cnt = 0
        for l in lans:
            lan_cnt += l // lan_len
        if lan_cnt >= N:
            ans = lan_len
            start = lan_len + 1
        else:
            end = lan_len - 1
    return ans

lans = []

for _ in range(K):
    lans.append(int(input()))

max_len = max(lans)

print(find_length(1, max_len))