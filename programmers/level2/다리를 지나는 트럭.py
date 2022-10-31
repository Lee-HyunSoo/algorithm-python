from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer, total = 0, 0
    bridge = deque([0] * bridge_length)
    while len(bridge):
        answer += 1
        total -= bridge.popleft()

        if truck_weights:
            if total + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total += truck
            else:
                bridge.append(0)
    return answer
