'''
AC
https://www.acmicpc.net/problem/5430
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = input().strip()
    N = int(input())
    arr_input = input().strip()
    # 여기서 N을 체크!
    if N == 0:
        ac_queue = deque()  # 빈 큐 생성
    else:
        # 괄호 떼고 split
        ac_queue = deque(list(map(int, arr_input[1:-1].split(','))))
    is_reversed, errored = 0, False
    for c in cmd:
        if c == "R":
            is_reversed += 1
        else:
            if ac_queue and is_reversed % 2 == 1:
                ac_queue.pop()
            elif ac_queue and is_reversed % 2 == 0:
                ac_queue.popleft()
            else:
                errored = True
                break
    if errored:
        print("error")
    else:
        if is_reversed % 2 == 1:
            ac_queue.reverse()
        print("[" + ",".join(map(str, ac_queue)) + "]")



