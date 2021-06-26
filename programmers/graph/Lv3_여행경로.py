def solution(tickets):
    tickets.sort(reverse=True)
    stack = [["ICN", []]]
    while stack:
        s, visited = stack.pop()
        if len(visited) == len(tickets):
            answer = ["ICN"]
            for v in visited:
                answer.append(tickets[v][1])
            return answer

        for i, t in enumerate(tickets):
            if t[0] == s and i not in visited:
                stack.append([t[1], visited + [i]])
