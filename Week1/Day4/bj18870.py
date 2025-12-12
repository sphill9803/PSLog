'''
좌표 압축
https://www.acmicpc.net/problem/18870
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))
coords_set = set(coords)
nums = sorted(list(coords_set))
coords_dict = {}
for i in range(len(nums)):
    coords_dict[nums[i]] = i
for c in coords:
    print(coords_dict[c], end=" ")