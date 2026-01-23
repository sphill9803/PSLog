'''
IF문 좀 대신 써줘
https://www.acmicpc.net/problem/19637
'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

game_name = {}
powers = []

for i in range(N):
    name, power = input().split()
    power = int(power)
    if power not in game_name:
        powers.append(power)
        game_name[power] = name

def find_name(t_power, start, end):
    ans_idx = 0
    while start <= end:
        mid = (start + end) // 2
        if t_power <= powers[mid]:
            ans_idx = mid
            end = mid - 1
        else:
            start = mid + 1
    print(game_name[powers[ans_idx]])

for i in range(M):
    p = int(input())
    find_name(p, 0, (len(powers) - 1))