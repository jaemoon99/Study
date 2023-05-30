def solution(id_list, report, k):
    report = list(set(report))
    l = {i: [] for i in id_list}
    d = {i: 0 for i in id_list}
    answer = [0] * len(id_list)

    for i in report:
        # user, report한 사람
        u, r = i.split()

        # d: 신고당한 ID의 누적 횟수 체크
        d[r] += 1

        # user가 신고한 ID 저장
        l[u].append(r)

    for id, n in d.items():
        # 만약 신고 누적 횟수가 k를 넘어간다면
        if n >= k:
            # 정지당할 id에 따른 메일 송신을 위해 각 user별 조사
            for user, rep in l.items():
                if id in rep:
                    answer[id_list.index(user)] += 1

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))




# def solution(id_list, report, k):
#     answer = []
#     result_dict = dict(zip(id_list, [set(" ") for x in range(0, len(id_list))]))
#     print(result_dict)
#     print("\n")

#     report = list(set(report))
#     print(report)
#     print("\n")
#     ban_list = []
#     for x in range(0, len(result_dict)):
#         for y in range(0, len(report)):
#             if report[y].split(" ")[0] == list(result_dict)[x]:
#                 result_dict[list(result_dict)[x]].add(report[y].split(" ")[1])
#                 ban_list.append(report[y].split(" ")[1])
#     print(result_dict)
#     print("\n")
#     print(ban_list)
#     print("\n")
#     count = 0
#     print(list(result_dict.values()))
#     for x in list(result_dict.values()):
#         for y in x:
#             if y in ban_list and ban_list.count(y) >= k:
#                 count += 1
#         answer.append(count)
#         count = 0
#     return answer





# from collections import defaultdict
# def solution2(id_list, report,k):
#     answer = []
#     # 중복 신고 제거
#     report = list(set(report))
#     # user별 신고한 id 저장
#     user = defaultdict(set)
#     # user별 신고당한 횟수 저장
#     cnt = defaultdict(int)
	
#     for r in report:
#         # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
#         a,b = r.split()
#         # 신고자가 신고한 id 추가
#         user[a].add(b)
#         # 신고당한 id의 신고 횟수 추가
#         cnt[b] += 1
    
#     for i in id_list:
#         result = 0
#         # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
#         for u in user[i]:
#             if cnt[u]>=k:
#                 result +=1
#         answer.append(result)
#     print(answer)
#     print(report)
#     print(user)
#     print(cnt)
#     return answer




# a = ["con", "ryan"]
# b = ["ryan con", "ryan con", "ryan con", "ryan con"]
# result_dict = dict(zip(a, [list(" ") for x in range(0, len(a))]))
# b = list(set(b))
# ban_list = []
# result = []
# for x in range(0, len(result_dict)):
#     for y in range(0, len(b)):
#         if b[y].split(" ")[0] == list(result_dict)[x]:
#             result_dict[list(result_dict)[x]].append(b[y].split(" ")[1])
#             ban_list.append(b[y].split(" ")[1])

# print(result_dict)
# print(ban_list)
# count = 0
# for x in result_dict.values():
#     for y in x:
#         if y in ban_list and ban_list.count(y) >= 3:
#             count += 1
#     result.append(count)
#     count = 0
# print(result)

# print(result_dict)

# for x in b:
#     result_dict[x] += 1

# print(result_dict)