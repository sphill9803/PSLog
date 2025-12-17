'''
후위표기식 2
https://www.acmicpc.net/problem/1935
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

expr_str = input().strip()
expr_stack = []

# 기존 코드

# var_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# var_dict = {}
#
# for i in range(N):
#     var_dict[var_str[i]] = int(input())

values = [int(input()) for _ in range(N)] # 값 미리 다 받기

for e in expr_str:
    if e in "+-*/":
        v2 = expr_stack.pop()
        v1 = expr_stack.pop()
        if e == "+":
            expr_stack.append(v1 + v2)
        elif e == "*":
            expr_stack.append(v1 * v2)
        elif e == "/":
            expr_stack.append(v1 / v2)
        elif e == "-":
            expr_stack.append(v1 - v2)
    else:
        # ord를 쓰면 간편하게 체크 가능, 메모리 절약도 가능.
        expr_stack.append(values[ord(e) - ord('A')])

print("{:.2f}".format(expr_stack.pop()))