'''
풍선 터뜨리기
https://www.acmicpc.net/problem/2346
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())
papers = list(map(int, input().split()))
balloons = deque(range(N))

while balloons:
    idx = balloons.popleft()  # 풍선 터뜨리기
    print(idx + 1, end=" ")  # 번호 출력 (1부터 시작하므로 +1)

    if not balloons:  # 다 터졌으면 종료
        break

    gap = papers[idx]  # 종이에 적힌 값

    if gap > 0:
        # 양수 이동: 이미 1개 빠졌으므로 1칸 덜 이동해야 함 (왼쪽으로 회전)
        # rotate(-1)이 왼쪽 회전이므로 음수 부호 붙임
        balloons.rotate(-(gap - 1))
    else:
        # 음수 이동: 오른쪽으로 회전 (rotate는 양수가 오른쪽)
        # gap이 음수이므로 -gap은 양수
        balloons.rotate(-gap)