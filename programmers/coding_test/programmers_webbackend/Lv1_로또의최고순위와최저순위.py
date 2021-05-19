# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    lotto = set(lottos) - {0}
    win_nums = set(win_nums)
    min_case = len(win_nums & lotto)
    max_case = min_case + min(6-len(lotto), len(win_nums-lotto))
    score_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = [score_dict[max_case], score_dict[min_case]]
    return answer

"""
	당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	
"""

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
