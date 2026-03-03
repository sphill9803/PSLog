'''
수들의 합2
https://www.acmicpc.net/problem/2003

투 포인터 알고리즘은 아래와 같은 두 가지 케이스가 존재한다.

1) 2개의 포인터 변수 시작점이 배열의 시작점인 경우

2) 정렬된 배열 안에서 2개의 포인터 변수가 각각 시작점과 끝점(arr.length-1)에 위치한 경우


만약, 정수로 이루어진 배열에서 연속된 부분 배열의 합이 특정 값(Target)을 이루는 부분 배열의 개수를 구하는 문제가 있다고 가정했을 때, 두 포인터 변수의 이동 조건은 다음과 같습니다.

(1) 부분 배열의 합이 Target 값보다 크거나 같으면 Left = Left + 1 해줍니다. (부분 배열의 길이를 줄여 합을 빼준다. )
0
if(sum >= Target) Left++;

(2) 부분 배열의 합이 Target 값보다 작으면 Right = Right + 1 해줍니다. (부분 배열의 길이를 늘려 합을 더한다.)

if(sum < Target) Right++;

(3) 부분 배열의 합이 Target 값과 같다면 결과 값을 +1 해줍니다.

if( sum == Target) count++;

'''

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
list_A = list(map(int, input().split()))

# start: 구간의 시작 인덱스
# end: 구간의 끝 인덱스 (현재 구간에 포함되지 않은, 다음에 더할 인덱스)
start, end = 0, 0
current_sum = 0
ans = 0

while True:
    # 1. 현재 합이 M보다 크거나 같다면 -> 범위를 좁힘 (start 이동)
    if current_sum >= M:
        if current_sum == M:
            ans += 1
        current_sum -= list_A[start]
        start += 1

    # 2. end가 끝까지 갔다면 -> 더 이상 늘릴 수 없으므로 종료
    # (위의 if문 체크 후에도 합이 부족한데 더할 숫자가 없는 경우)
    elif end == N:
        break

    # 3. 현재 합이 M보다 작다면 -> 범위를 늘림 (end 이동)
    else:
        current_sum += list_A[end]
        end += 1

print(ans)