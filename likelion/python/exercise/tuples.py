# ---------- 튜플 - 튜플의 정의 및 특징 ----------
# 튜플(Tuples)

tup = (1, 20, 40)
# print(tup[0])

# tup[0] = 100 실행이 안되는 이유 튜플은 생성하면 요소 변경이 불가능 하다.
# tup = (100, 30, 4) # 튜플 전체를 재할당하는 것은 가능하다.
# print(tup)
# ---------- 튜플 - 튜플/리스트 변환 ----------
for x in tup:
    print(x)

# 리스트 변환 1
list_1 = list(tup)
print(list_1)

# 리스트 변환 2
list_2 = [x  for x in tup]
print(list_2)

# 리스트 변환 3
list_3 = []

for x in tup:
    list_3.append(x)
print(list_3)