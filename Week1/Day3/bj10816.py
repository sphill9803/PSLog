'''
숫자카드 2
https://www.acmicpc.net/problem/10816
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
cards = input().split()
counter = {}

for card in cards:
    # if card in counter:
    #     counter[card] += 1
    # else:
    #     counter[card] = 1
    counter[card] = counter.get(card, 0) + 1 # 딕셔너리의 get method 쓰면 이렇게 가능

M = int(input())
targets = input().split()

for t in targets:
    if t in counter:
        print(counter[t], end=" ")
    else:
        print(0, end=" ")


# Counter를 이용한 풀이
# from collections import Counter
#
# # 입력받은 리스트를 바로 카운팅해줌
# counter = Counter(cards)
#
# for t in targets:
#     print(counter[t], end=" ") # 없으면 알아서 0 나옴