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
        t_len = 0
        mid_h = (start + end) // 2

        for t in trees:
            if t >= mid_h:
                t_len += (t - mid_h)

        if t_len >= M:
            ans = mid_h
            start = mid_h + 1
        else:
            end = mid_h - 1
    return ans

trees = list(map(int, input().split()))

max_len = max(trees)

print(find_length(0, max_len))