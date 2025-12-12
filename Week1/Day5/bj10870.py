'''
피보나치 수 5
https://www.acmicpc.net/problem/10870
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(N))