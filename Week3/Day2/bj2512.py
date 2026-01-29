'''
예산
https://www.acmicpc.net/problem/2512
'''
import sys

sys.stdin = open("../../input.txt", "r")

input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

def decide_budget(start, end):
    if sum(budgets) <= M:
        return end

    ans = 0
    while start <= end:
        t_budget = 0

        mid = (start + end) // 2

        for b in budgets:
            if b > mid:
                t_budget += mid
            else:
                t_budget += b
        if t_budget <= M:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(decide_budget(0, max(budgets)))