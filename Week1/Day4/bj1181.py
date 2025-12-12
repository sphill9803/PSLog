'''
단어 정렬
https://www.acmicpc.net/problem/1181
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N = int(input())

words = set()
for _ in range(N):
    word = input().strip()
    words.add(word)

words = list(words)

# words.sort()
# words.sort(key=len)

# (1순위: 길이, 2순위: 단어 자체)
# 파이썬의 sort는 Stable Sort라서, 길이 순으로 정렬할 때 길이가 같으면 기존 순서(사전 순)가 유지된다.
words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)