# 리스트 균등분할 함수
def listsplit(score, n):
    list = []
    for x in range(0, len(score), n):
        list.append(score[x:x+n])
    return list

def solution(k, m, score):
    answer = 0
    # 리스트 균등 분할
    chunk = listsplit(sorted(score, reverse=True), m)
    # 분할한 각각의 부분 리스트 순회
    for x in chunk:
        # 각 부분리스트의 원소의 개수가 m개인지 판단
        if len(x) == m:
            answer += x[-1] * m
    return answer

print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

'''

고인물 답안 1

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

고인물 답안 2

solution = lambda _, m, s: sum(sorted(s)[-m::-m]) * m

'''