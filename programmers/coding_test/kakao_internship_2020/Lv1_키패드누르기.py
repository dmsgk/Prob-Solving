# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    region = [[1,4,7, '*'], [2,5,8,0], [3,6,9, '#']]
    lthumb, rthumb = [3,0], [3,2]  #keypads의 '#' 위치 출력
    for n in numbers:
        if n in region[0]: # 왼손구역
            lthumb = [region[0].index(n), 0]
            answer += 'L'
        elif n in region[2]: # 오른손 구역
            rthumb = [region[2].index(n), 2]
            answer += 'R'
        else:
            location = [region[1].index(n),1]
            ldist, rdist = 0, 0
            for i in range(2):
                ldist += abs(lthumb[i]-location[i])
                rdist += abs(rthumb[i]-location[i])
            if ldist > rdist:
                answer += 'R'
                rthumb = location
            elif ldist < rdist:
                answer += 'L'
                lthumb = location
            else:
                if hand =='right':
                    answer += 'R'
                    rthumb = location
                else:
                    answer += 'L'
                    lthumb = location
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))   # "LRLLLRLLRRL"