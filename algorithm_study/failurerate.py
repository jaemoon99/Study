def solution(N, stages):
    dic = dict(zip([x for x in range(1, N + 2)], [x * 0 for x in range(1, N + 2)]))
    for x in stages:
        for y in range(1, N + 2):
            if x == y:
                dic[x] += 1
    values = []
    total = 0
    for x in range(1, N + 2):
        values.append(dic[x] / (len(stages) - total))
        total += dic[x]
    sort_value = sorted(values[0:len(values) - 1], reverse=True)
    dic_keys = list(dic.keys())
    answer = []
    for x in range(0, len(sort_value)):
        for y in range(0, len(sort_value)):
            print(sort_value, dic[dic_keys[y]])
            # if sort_value[x] == dic[dic_keys[y]]:
            #     answer.append(dic_keys[y])
            #     dic[dic_keys[y]] == 0


    return answer


def solution2(N, stages):
    answer = []
    dic = dict(zip([x for x in range(1, N + 2)], [x * 0 for x in range(1, N + 2)]))
    for x in stages:
        for y in range(1, N + 2):
            if x == y:
                dic[x] += 1
    values = []
    total = 0
    for x in range(1, N + 2):
        if len(stages) - total == 0:
            total += 0
        else:
            total += dic[x]
            values.append(dic[x] / (len(stages) - total))
    sort_values = sorted(values[:len(values) - 1], reverse=True)
    dic_keys = list(dic.keys())
    mid_dic = list(zip(values[:len(values) - 1], dic_keys[:len(dic_keys) - 1]))
    result_dic = []
    for x in mid_dic:
        result_dic.append(list(x))
    for x in range(0, len(sort_values)):
        for y in range(0, len(result_dic)):
            if (sort_values[x] == max(sort_values)) and (sort_values[x] == result_dic[y][0]):
                answer.append(result_dic[y][1])
                sort_values[x] = 0
                result_dic[y][0] = -1
                break
    return answer

def solution3(N, stages):
    answer = []
    stages_dic = dict(zip([x for x in range(1, N + 2)], [x * 0 for x in range(1, N + 2)]))
    for x in stages:
        stages_dic[x] += 1
    total = 0
    for x in range(1, N + 1):
        try:
            if len(stages) - total == 0:
                total += 0
                stages_dic[x] = 0
            else:
                total += stages_dic[x]
                stages_dic[x] = stages_dic[x] / int((len(stages) - total))
        except:
            continue
    answer_keys = list(stages_dic.keys())
    answer_values = list(stages_dic.values())
    for i in range(0, N):
        for j in range(0, N):
            if answer_values[j] == max(answer_values[:N]):
                answer.append(answer_keys[j])
                answer_values[j] = -1
    return answer[:N]

def solution4(N, stages):
    answer = {}
    answer2 = []
    people = len(stages)
    for x in range(1, N+1):
        # 인원이 0이 아닌 경우
        if people != 0:
            # 각 스테이지에 막힌 사람의 수
            count = stages.count(x)
            # 각 스테이지의 인원 - 실패율을 answer 딕셔너리에 추가
            answer[x] = count / people
            # 다음 스테이지에 사람은 현재 스테이지를 성공했기 때문에 현재 스테이지 인원을 총 스테이지 인원에서 감소
            people -= count
        else:
            # 인원이 0인 경우
            answer[x] = 0
    answer_keys = list(answer.keys())
    answer_values = list(answer.values())
    for x in range(0, N):
        for y in range(0, N):
            if answer_values[y] == max(answer_values):
                answer2.append(answer_keys[y])
                answer_values[y] = -1
    return answer2[:N]
print(solution4(4, [4,4,4,4,4]))