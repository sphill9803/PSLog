'''
포켓몬 마스터
https://www.acmicpc.net/problem/1620
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {}
for i in range(N):
    pokemon = input().strip()
    pokedex[pokemon] = i + 1
    pokedex[str(i + 1)] = pokemon

for i in range(M):
    target = input().strip()
    print(pokedex[target])