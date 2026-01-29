'''
입국심사
https://www.acmicpc.net/problem/3079
'''
import sys

sys.stdin = open("../../input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

times = [] # 심사대별로 걸리는 시간
for _ in range(N):
    times.append(int(input()))

def calculate_time(start, end):
    ans = 0

    while start <= end:
        ppls = 0

        mid = (start + end) // 2

        for t in times:
            ppls += mid // t
            # 최적화 코드... 목표 인원 넘겼으면 for문 탈출해서 확인.
            if ppls >= M:
                break

        if ppls >= M:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

print(calculate_time(1, min(times) * M))