from collections import defaultdict


def solution(record):
    user_dict = defaultdict(str)
    for rec in record:
        if rec.startswith('Leave'):
            continue
        cmd, uid, nickname = rec.split()
        user_dict[uid] = nickname

    answer = []
    for rec in record:
        if rec.startswith('Change'):
            continue

        message = ""
        if rec.startswith('Enter'):
            _, uid, _ = rec.split()
            message += user_dict[uid]
            message += "님이 들어왔습니다."
        else:
            _, uid= rec.split()
            message += user_dict[uid]
            message += '님이 나갔습니다.'
        answer.append(message)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]