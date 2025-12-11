'''
의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
'''

def solution(clothes):
    closet = {}
    for cloth in clothes:
        closet[cloth[1]] = closet.get(cloth[1], 0) + 1
    answer = 1
    for cloth_type in closet.keys():
        answer = answer * (closet[cloth_type] + 1)
    return answer - 1