def solution(name, yearning, photo):
    answer = [] # 답안 배열
    total_score = 0 # 사진 당 총 점수
    score_dic = dict(zip(name, yearning)) # 이름과 그리움 점수 배열을 딕셔너리로 병합
    for x in range(len(photo)): # 사진 루프
        for y in photo[x]: # 사진 속 사람 루프
            if y in name: # 사진 속 사람이 이름 배열에 있는지 확인
                total_score += score_dic[y] # 있으면 총 점수에 덧셈
        answer.append(total_score) # 이름 배열에 있는 사람들의 총 그리움 점수를 답안 배열에 저장
        total_score = 0 # 다음 사진을 위해 총 점수 초기화

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution(name, yearning, photo))

'''

모범답안

def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]

'''