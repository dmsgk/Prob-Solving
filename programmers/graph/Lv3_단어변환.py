from collections import deque


def solution(begin, target, words):
    visited = {word:0 for word in words}
    visited[begin] = 0
    queue = deque([begin])
    while queue:
        q = queue.popleft()
        if q == target:
            return visited[target]
        for word in words:
            if visited[word] == 0:
                cnt = 0
                for i, char in enumerate(q):
                    if cnt > 1:
                        break
                    elif char != word[i]:
                        cnt += 1
                if cnt == 1:
                    visited[word] = visited[q] + 1
                    queue.append(word)
    return 0



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
