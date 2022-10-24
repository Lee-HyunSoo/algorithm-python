from collections import deque
from collections import defaultdict


def solution(msg):
    queue, words = deque(msg), defaultdict(int)
    answer = []
    for i in range(ord('A'), ord('Z') + 1):
        words[chr(i)] = i - 64
    index = len(words)

    while queue:
        word = queue.popleft()

        for q in queue:
            word = word + q
            if not words[word]:
                index += 1
                words[word] = index
                word = word[:-1]
                break

        for _ in range(1, len(word)):
            queue.popleft()
        answer.append(words[word])
    return answer
