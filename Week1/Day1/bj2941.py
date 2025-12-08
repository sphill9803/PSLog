'''
크로아티아 알파벳
https://www.acmicpc.net/problem/2941
'''


import sys
# sys.stdin = open("../../input.txt", "r")  # 제출할 땐 주석 처리
input = sys.stdin.readline

# 1. 크로아티아 알파벳 목록 (순서 중요! 3글자인 dz=가 z=보다 먼저 체크되어야 안전)
croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input().strip()  # 2. strip()으로 개행문자(\n) 제거 필수 -> readline은 개행문자 제거가 필수다.

# 3. 목록에 있는 문자가 발견되면 전부 한 글자('*')로 치환 -> 이게 포인트
for char in croatian_alphabet:
    word = word.replace(char, '*')

# 4. 그냥 길이만 재면 됨 (*도 1글자, 안 바뀐 일반 문자도 1글자)
print(len(word))

#내가 처음 작성한 코드
'''
import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

croatian_alphabet = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}

word = input().strip()
croatian_count = 0
word_index = 0

while word_index < len(word):
    if (word[word_index] == "c" or word[word_index] == "l" or word[word_index] == "n" or word[word_index] == "s" or word[word_index] == "z") and word_index < len(word)-1:
        if word[word_index : word_index + 2] in croatian_alphabet:
            croatian_count += 1
            word_index += 1
        else:
            croatian_count += 1
    elif word[word_index] == "d":
        if word_index < len(word)-2:
            if word[word_index : word_index + 2] in croatian_alphabet:
                croatian_count += 1
                word_index += 1
            elif word[word_index : word_index + 3] in croatian_alphabet:
                croatian_count += 1
                word_index += 2
            else:
                croatian_count += 1
        elif word_index < len(word)-1:
            if word[word_index : word_index + 2] in croatian_alphabet:
                croatian_count += 1
                word_index += 1
            else:
                croatian_count += 1
        else:
            croatian_count += 1
    else:
        croatian_count += 1
    word_index += 1

print(croatian_count)
'''