'''
그룹 단어 체커
https://www.acmicpc.net/problem/1316
'''

import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

def isGroup(word):
    alpha_set = set()
    curr_char = word[0]
    alpha_set.add(curr_char)
    for c in word:
        if c != curr_char and c in alpha_set:
            return False
        alpha_set.add(c)
        curr_char = c
    return True

N = int(input())
group_count = 0
for i in range(N):
    word = input()
    if isGroup(word):
        group_count += 1

print(group_count)