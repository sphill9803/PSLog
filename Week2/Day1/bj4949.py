'''
균형잡힌 세상
https://www.acmicpc.net/problem/4949
'''
import sys
sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

brackets = {']' : '[', ')' : '('}

while True:
    target_str = sys.stdin.readline().rstrip()  # strip()은 양쪽 공백 다 지우므로 rstrip() 권장 (중간 공백 보존)
    if target_str == ".":
        break

    bracket_stack = []  # 굳이 deque 안 써도 list가 빠름
    is_balanced = True

    for s in target_str:
        if s in '([':
            bracket_stack.append(s)
        elif s in brackets:  # 닫는 괄호라면
            if not bracket_stack:  # 스택이 비어있으면 실패
                is_balanced = False
                break

            if bracket_stack[-1] == brackets[s]:  # 짝이 맞으면 pop
                bracket_stack.pop()
            else:  # 🔥 [중요] 짝이 안 맞으면 바로 실패 처리해야 함!
                is_balanced = False
                break

    # 스택이 비어있고(짝 다 맞음) + 중간에 실패한 적 없어야 True
    if not bracket_stack and is_balanced:
        print("yes")
    else:
        print("no")

