'''
최소, 최대
https://www.acmicpc.net/problem/10818
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

print(min(N_list), max(N_list))