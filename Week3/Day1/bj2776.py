'''
암기왕
https://www.acmicpc.net/problem/2776
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())

    A_set = set(map(int, input().split()))

    M = int(input())

    num_list = list(map(int, input().split()))

    for n in num_list:
        if n not in A_set:
            print(0)
        else:
            print(1)