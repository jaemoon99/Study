# ---------- 파일 다루기와 예외 처리 - 예외 처리(1) ----------
# Exceptions(예외)

# a = 10
# b = 0
# a / b

fruits = ['apple', 'banana', 'strawberry']
# ---------- 파일 다루기와 예외 처리 - 예외 처리(2) ----------
# try:
#     fruits[2]
# except:
#     print("인덱스를 참조할 수 없습니다.")
# else:
#     print("정상 수행")

try:
    fruits[3]
except:
    print("인덱스를 참조할 수 없습니다.")
finally:
    print("명령 수행")

print(fruits)

''' else 와 finally의 차이점
else - try문이 오류없이 끝나야 실행됨
finally -  try문에 오류가 있든 없든 실행됨
'''