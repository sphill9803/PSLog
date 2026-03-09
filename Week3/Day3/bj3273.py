'''
두 수의 합
https://www.acmicpc.net/problem/3273
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
target = int(input())

left, right = 0, N - 1

cnt = 0

while left < right:
    temp = nums[left] + nums[right]
    if temp > target:
        right -= 1
    elif temp < target:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)