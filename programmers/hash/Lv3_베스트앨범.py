import operator

def solution(genres, plays):
    answer = []
    dict = {}
    total_dict = {}

    for i, v in enumerate(plays):
        if genres[i] not in dict:
            dict[genres[i]] = {i : v}
            total_dict[genres[i]] = v
        else:
            dict[genres[i]][i] = v
            total_dict[genres[i]] += v

    arr = sorted(total_dict.items(), key = operator.itemgetter(1), reverse = True)
    for a in arr:
        li = sorted(dict[a[0]].items(),  key = operator.itemgetter(1), reverse = True)
        for i, j in enumerate(li):
            if i < 2:
               answer.append(j[0])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4,1,3,0]