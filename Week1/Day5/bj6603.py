'''
로또
https://www.acmicpc.net/problem/6603
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def dfs(idx, picked):
    # [종료 조건] 6개를 다 뽑았으면 출력하고 리턴
    if len(picked) == 6:
        print(*picked)  # 리스트 요소 공백 두고 출력
        return

    # [탐색] 현재 인덱스부터 끝까지 하나씩 골라서 담아봄
    for i in range(idx, k):
        picked.append(S[i])  # 1. 담고
        dfs(i + 1, picked)  # 2. 다음 단계로 (재귀)
        picked.pop()  # 3. 갔다 와서는 뺌 (백트래킹 핵심!)


while True:
    line = list(map(int, input().split()))
    if line[0] == 0:  # 0이면 종료
        break

    k = line[0]
    S = line[1:]

    dfs(0, [])
    print()  # 테스트 케이스 사이 빈 줄