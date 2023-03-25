# ---------- 변수와 자료형 - 문자열(1) ----------
# # 문자열(Strings) = 문자열 나열

# city = "seoul" # Seoul, SEOUL, SEOul
# print(city)

# city.upper() # city에 함수가 적용된 것이 아니기 때문에
# print(city)
# print(city.upper()) # 전체를 다 적어줘야 한다

# city = city.upper() # 재할당을 해준 경우는
# print(city) # 변수 이름만 적어줘도 된다

# city.lower()
# print(city)
# print(city.lower)

# city = city.lower()
# print(city)

# occupation = "   developer   "
# print(occupation)

# occupation.rstrip()
# print(occupation.rstrip()) # 오른쪽 공백 제거
# print(occupation.lstrip()) # 왼쪽 공백 제거
# print(occupation.strip()) # 양쪽 공백 제거

# print("INFP\nENFP\nISTJ\nESTJ") # \n = enter
# print("INFP\tENFP\tISTJ\tESTJ") # \t = tab

# ---------- 변수와 자료형 - 문자열(2) ----------
# score = "점수:90"
# print(score.removeprefix("점수:")) # 문자열의 왼쪽 부분 삭제

# score_2 = "75점"
# print(score_2.removesuffix("점")) # 문자열의 오른쪽 부분 삭제

# city = "서울 중구"
# print(city.replace("서울", "서울시")) # 문자 변경

# ---------- 변수와 자료형 - 문자열(3) ----------
si_1 = "용인"
gu_1 = "기흥"

si_2 = "서울"
gu_2 = "종로"

# 서울시 종로구
# 용인시 기흥구
# (시의 이름)시 (구의 이름)구
print(f"{si_1}시 {gu_1}구") # fstring(문자열 사이에 변수사용 가능)
print(f"{si_2}시 {gu_2}구")

address_1 = f"{si_1}시 {gu_1}구" #fstring 형식으로 변수에 대입 가능
print(address_1)
