def solution(survey, choices):
    # 답안 문자열
    answer = ""

    # 각 유형별 점수
    mbti_dic = {
        'R' : 0,
        'C' : 0,
        'J' : 0,
        'A' : 0,
        'T' : 0,
        'F' : 0,
        'M' : 0,
        'N' : 0
    }

    # 각 위치 집합
    mbti_set = (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N'))

    # choices 길이만큼 순회
    for x in range(len(choices)):
        if choices[x] >= 5:
            mbti_dic[survey[x][1]] += choices[x] - 4
        elif choices[x] == 1:
            mbti_dic[survey[x][0]] += 3
        elif choices[x] == 2:
            mbti_dic[survey[x][0]] += 2
        elif choices[x] == 3:
            mbti_dic[survey[x][0]] += 1

    # 각 위치끼리 점수 비교
    for y in mbti_set:
        if mbti_dic[y[0]] == mbti_dic[y[1]]:
            answer += sorted(y)[0]
        elif mbti_dic[y[0]] > mbti_dic[y[1]]:
            answer += y[0]
        elif mbti_dic[y[0]] < mbti_dic[y[1]]:
            answer += y[1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))

'''
고인물의 답변

def solution(survey, choices):
    mbti={'R': 0,'T': 0,'C': 0,'F': 0,'J': 0,'M': 0,'A': 0,'N': 0}
    for i in range(len(choices)):
        if 1<=choices[i]<=3:
            mbti[survey[i][0]]+=4-choices[i]
        elif 5<=choices[i]<=7:
            mbti[survey[i][1]]+=choices[i]-4
    return ('R' if mbti['R']>=mbti['T'] else 'T')+('C' if mbti['C']>=mbti['F'] else 'F')+('J' if mbti['J']>=mbti['M'] else 'M')+('A' if mbti['A']>=mbti['N'] else 'N')

'''





# def solution(survey, choices):
#     answer = ""
#     cha = ["R", "C", "J", "A", "T", "F", "M", "N"]
#     point = [0] * len(cha)
#     for l_index in range(0, len(survey)):
#         if choices[l_index] == 1:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][0]:
#                     point[cha.index(survey[l_index][0])] += 3
#         elif choices[l_index] == 2:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][0]:
#                     point[cha.index(survey[l_index][0])] += 2
#         elif choices[l_index] == 3:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][0]:
#                     point[cha.index(survey[l_index][0])] += 1
#         elif choices[l_index] == 5:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][1]:
#                     point[cha.index(survey[l_index][1])] += 1
#         elif choices[l_index] == 6:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][1]:
#                     point[cha.index(survey[l_index][1])] += 2
#         elif choices[l_index] == 7:
#             for l_cha in cha:
#                 if l_cha == survey[l_index][1]:
#                     point[cha.index(survey[l_index][1])] += 3

#     if point[cha.index("R")] > point[cha.index("T")]:
#         answer += 'R'
#     elif point[cha.index("R")] < point[cha.index("T")]:
#         answer += 'T'
#     elif point[cha.index("R")] == point[cha.index("T")]:
#         answer += 'R'

#     if point[cha.index("C")] > point[cha.index("F")]:
#         answer += 'C'
#     elif point[cha.index("C")] < point[cha.index("F")]:
#         answer += 'F'
#     elif point[cha.index("C")] == point[cha.index("F")]:
#         answer += 'C'

#     if point[cha.index("J")] > point[cha.index("M")]:
#         answer += 'J'
#     elif point[cha.index("J")] < point[cha.index("M")]:
#         answer += 'M'
#     elif point[cha.index("J")] == point[cha.index("M")]:
#         answer += 'J'

#     if point[cha.index("A")] > point[cha.index("N")]:
#         answer += 'A'
#     elif point[cha.index("A")] < point[cha.index("N")]:
#         answer += 'N'
#     elif point[cha.index("A")] == point[cha.index("N")]:
#         answer += 'A'
#     return answer