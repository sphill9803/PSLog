'''
프로그래머스 Lv.2 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_trucks = len(truck_weights)
    trucks = deque(truck_weights)
    curr_weight = trucks.popleft()
    bridge = deque([0 for _ in range(bridge_length - 1)] + [curr_weight])
    answer, curr_trucks, end_trucks = 1, 1, 0
    while end_trucks < total_trucks:
        ended = bridge.popleft()
        answer += 1
        if ended > 0:
            curr_weight -= ended
            end_trucks += 1
            curr_trucks -= 1
        if trucks:
            if curr_weight + trucks[0] <= weight:  # 새로운 트럭 추가
                curr_trucks += 1
                curr_weight += trucks[0]
                bridge.append(trucks.popleft())
            else:  # 기존 트럭 한 칸 전진
                bridge.append(0)
        else:
            bridge.append(0)

    return answer

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))