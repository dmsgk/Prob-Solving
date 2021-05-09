def solution(code, day, data):
    answer = []
    for i in data:
        i_price, i_code, i_time = i.strip().split()
        if i_code == "code=%s" % code and i_time[:-2] == "time=%s" % day:
            answer.append((i.split()))
    answer.sort(key = lambda time : time[2])
    result = []
    for i in answer:
        p,c,t = i
        result.append(int(p[6:]))
    return result

print(solution("012345", "20190620", ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014", "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"]))