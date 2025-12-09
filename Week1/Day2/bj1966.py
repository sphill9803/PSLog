'''
프린터 큐
https://www.acmicpc.net/problem/1966
'''

import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    print_queue = deque()
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    for i in range(len(docs)):
        print_queue.append((i, docs[i])) # (문서 번호, 우선순위)
    docs.sort(reverse=True)
    # 굳이 docs를 deque로 만들어서 popleft할 필요 없이 idx로 순회하면 됨.
    # count, p_idx = 0, 0
    # count와 p_idx는 같이 움직이기 때문에 count = p_idx로 놓아도 무리없음.
    count = 0
    while print_queue:
        if print_queue[0][1] < docs[count]: # p_idx 대신 count 사용
            '''
            이 부분 최적화 가능 -> rotate!
            print_queue.append(print_queue[0])
            print_queue.popleft()
            '''
            print_queue.rotate(-1) # rotate(-1)은 왼쪽으로 한칸씩 미는 연산임.
        else:
            count += 1
            if print_queue[0][0] == M:
                print(count)
                break
            print_queue.popleft()
            # p_idx += 1