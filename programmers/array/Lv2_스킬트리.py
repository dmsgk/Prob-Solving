def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        curr_idx = 0  # 배워야하는 스킬의 인덱스
        for s in skill_tree:
            if s in set(skill):
                if s == skill[curr_idx]:
                    curr_idx += 1
                else:
                    break
        else:
            answer += 1

    return answer