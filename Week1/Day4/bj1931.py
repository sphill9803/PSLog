'''
회의실 배정
https://www.acmicpc.net/problem/1931
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    start_time, end_time = map(int, input().split())
    meetings.append([start_time, end_time])

meetings.sort(key=lambda x: (x[1], x[0]))

end_pivot = -1

meeting_count = 0

for m in meetings:
    if m[0] >= end_pivot:
        end_pivot = m[1]
        meeting_count += 1

print(meeting_count)