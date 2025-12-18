'''
카드2
https://www.acmicpc.net/problem/2164
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
cards = deque([i + 1 for i in range(N)])

# 기존 코드
# idx = 0
#
# while cards:
#     if len(cards) == 1:
#         print(cards.popleft())
#     else:
#         if idx % 2 == 0:
#             cards.popleft()
#         else:
#             cards.append(cards.popleft())
#     idx += 1

# 피드백한 코드
while len(cards) > 1:
    cards.popleft() # 1. 버린다 (무조건 먼저 수행)
    cards.append(cards.popleft()) # 2. 옮긴다 (그 다음 수행)

print(cards[0]) # 남은 하나 출력