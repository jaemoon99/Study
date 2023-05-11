def listsplit(score, n):
    list = []
    for x in range(0, len(score), n):
        list.append(score[x:x+n])
    return list

def solution(k, m, score):
    answer = 0
    chunk = listsplit(sorted(score, reverse=True), m)
    for x in chunk:
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