'''
숫자의 개수
https://www.acmicpc.net/problem/2577
'''

import sys

sys.stdin = open("../../input.txt", "r")

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

N = A * B * C

str_N = str(N)

for i in range(10):
    print(str_N.count(str(i)))