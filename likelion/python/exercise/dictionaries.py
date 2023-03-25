# ---------- 딕셔너리 - 딕셔너리 정의 및 선언 ----------
# 딕셔너리(Dictionaries)

# student = {
#     "student_no" : "202301234",
#     "major" : "English",
#     "grade" : 1
# }

# print(student["student_no"])

# student["student_no"] = "202301235"

# print(student)
# print(student["student_no"])
# ---------- 딕셔너리 - 딕셔너리 데이터 조작 ----------
# 추가
# student["gpa"] = 4.5
# print(student)

# # 수정
# student["gpa"] = 4.3
# print(student)

# # 삭제
# del student["grade"]
# print(student)
# ---------- 딕셔너리 - 딕셔너리 함수 ----------
# 데이터 접근
# print(student.get("major"))
# print(student.get("gpa", "해당 키-값 쌍이 없습니다."))

# # 딕셔너리의 키를 반환
# print(student.keys())
# print(list(student.keys())) # 키를 리스트 형식으로 반환

# # 딕셔너리의 값을 반환
# print(student.values())
# print(list(student.values()))
# ---------- 딕셔너리 - 딕셔너리와 반복문 ----------
# tech = {
#     "HTML" : "Advanced",
#     "JavaScript" : "Intermediate",
#     "Python" : "Expert",
#     "Go" : "Novice"
# }

# for i in tech: # 그냥 사용할 경우 키값만 나온다
#     print(i)

# for key in tech.keys():
#     print(key)

# for value in tech.values():
#     print(value)

# for key, value in tech.items():
#     print(f'{key} - {value}')
# ---------- 딕셔너리 - 딕셔너리 중첩 ----------
# 중첩(Nesting)

# student_1 = {
#     "student_no" : "1",
#     "gpa" : "4.3"
# }

# student_2 = {
#     "student_no" : "2",
#     "gpa" : "3.8"
# }

# students = [student_1, student_2]

# for student in students:
#     print(student['student_no'])

# for student in students:
#     student['graduated'] = False
#     print(student)

# student = {
#     "subjects" : ["회계원리", "중국어회화"]
# }

# print(student["subjects"])

# subjects_list = student["subjects"]

# for subject in subjects_list:
#     print(subject)

student = {
    "scholarship" : {
        "name" : "국가장학금",
        "amount" : "1000000"
    }
}

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)
    for value_2 in value.values():
        print(value_2)