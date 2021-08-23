def solution(table, languages, preference):
    pref_dict = dict()
    for i in range(len(languages)):
        pref_dict[languages[i]] = preference[i]

    num_li = []
    for row in table:
        num = 0
        row_li = row.split()
        work_part = row_li.pop(0)
        for lan in languages:
            if lan not in row_li:
                continue
            score = 5 - row_li.index(lan)
            num += score * pref_dict[lan]
        num_li.append([work_part, num])

    num_li.sort(key= lambda x : (-x[1], x[0]))
    max_num = num_li.pop(0)
    return max_num[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))  # HARDWARE
