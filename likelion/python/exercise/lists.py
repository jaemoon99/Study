# ---------- 리스트 - 리스트의 정의 및 선언 ----------
# 리스트(list)

# mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']

# print(mbti)
# print(mbti[0])

# mbti[0] = 'INFJ'

# print(mbti)
# print(mbti[0])

# my_list = [123, 'apple'] # 파이썬은 다른 언어와 다르게 다른 자료형을 하나의 리스트에 넣을 수 있다.
# print(my_list)
# ---------- 리스트 - 리스트 데이터 접근 및 조작 ----------
# colors = ['red', 'blue','green']

# # 수정
# # colors[2] = 'black'
# # print(colors)

# # 추가 1
# colors.append('purple') # append는 추가할 요소를 맨 마지막에 추가한다.
# print(colors)

# # 추가 2
# colors.insert(1, 'yellow') # insert는 추가할 요소를 원하는 인덱스에 추가하고 기존에 있던 요소들은 한 칸씩 밀려난다.
# print(colors)

# # 제거 1
# del colors[0] # del은 원하는 인덱스에 있는 값을 영구 삭제한다. (값 재사용 불가)
# print(colors)

# # 제거 2
# color = colors.pop(0) # pop는 인덱스를 넣어 삭제 할 수도 있지만 생략할 경우 맨 뒤에 있는 요소를 제거한다. and 값을 반환해서 사용할 수 있다.
# print(colors)
# print(color)

# # 제거 3
# colors.remove('blue') # remove는 입력한 값을 삭제한다.
# print(colors)
# # ---------- 리스트 - 리스트 정렬 ----------
# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# # 정렬 1
# colors.sort()
# print(colors)

# colors.sort(reverse=True) # 역순
# print(colors)

# # 정렬 2
# sorted(colors) # 정렬을 하고 다시 원래 상태로 돌아감 (적용 x)
# print(colors)
# print(sorted(colors))

# # 길이 - 요소의 개수
# print(len(colors))

# print(colors[-1]) # 마지막 인덱스는 -1
# ---------- 리스트 - 리스트 슬라이싱 및 복사 ----------
# 리스트 슬라이싱
# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# colors_2 = colors[:]
# colors_2.pop()
# print(colors)
# print(colors_2)

# colors_3 = colors # 인덱스 없이 할당 한 경우 같은 주소를 바라보고 있기 때문에 colors_3에 pop을 진행하더라도 colors에 영향을 준다.
# colors_3.pop()
# print(colors)
# print(colors_3)

# # 양수 인덱스 (앞부터)
# print(colors[1:5])
# print(colors[:4])
# print(colors[2:])

# # 음수 인덱스 (뒤부터)
# print(colors[-5:])
# ---------- 리스트 - 리스트와 흐름 제어 ----------
scores = [88, 100, 96, 43, 65, 78]
# scores.sort(reverse=True)
# # print(scores)

# for score in scores:
#     if score >= 80:
#         print(score)
#     else:
#         print("Fail")
# ---------- 리스트 - 리스트와 최댓값/최솟값/총합 ----------
max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores)
avg_val = sum(scores) / len(scores)
print(max_val, min_val, sum_val, avg_val)