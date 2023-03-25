# ---------- 조건문과 반복문 - 조건문(1) ----------
# 조건문
# if False:
#     print("True")
# else:
#     print("False")

# if 4 > 3:
#     print("a")
# else:
#     print("b")

# 입력 값을 string 타입으로 처리
# value = input("값을 입력해주세요: ")

# if int(value) > 10:
#     print("a")
# else:
#     print("b")

# value = value.upper()

# if value == "INFP": # 대문자, 소문자 구별함
#     print("INFP")
# else:
#     print("nothing")
# ---------- 조건문과 반복문 - 조건문(2) ----------
day = input("요일을 입력해주세요(0~6): ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
else:
    print("정상영업")