'''
정수 제곱근
https://www.acmicpc.net/problem/2417
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

def find_q(start, end):
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 < N:
            start = mid + 1
        else:
            ans = mid
            end = mid -1
    return ans

print(find_q(0, N))