def solution2(name, yearning, photo):
    answer = []
    total_score = 0
    score_dic = dict(zip(name, yearning))
    for x in range(len(photo)):
        for y in photo[x]:
            if y in name:
                total_score += score_dic[y]
        answer.append(total_score)
        total_score = 0
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution2(name, yearning, photo))

'''

모범답안

def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]

'''