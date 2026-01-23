'''
수 찾기
https://www.acmicpc.net/problem/1920
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

A_set = set(map(int, input().split()))

M = int(input())

num_list = list(map(int, input().split()))

for n in num_list:
    if n not in A_set:
        print(0)
    else:
        print(1)