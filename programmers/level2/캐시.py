from collections import deque


def solution(cacheSize, cities):
    cache, answer = deque(), 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
        elif len(cache) == cacheSize:
            cache.popleft()
            answer += 5
        else:
            answer += 5
        cache.append(city)
    return answer
