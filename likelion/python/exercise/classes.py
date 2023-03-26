# ---------- 객체지향 - 클래스(1) ----------
# 클래스(Classes) - 설계

class Student: # 클래스의 첫 글자는 대문자가 와야한다.

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')
# ---------- 객체지향 - 클래스(2) ----------
# 인스턴스 - 실체화된 사물

student_1 = Student('김멋사', '컴퓨터공학과')
# print(student_1)

# student_1_name = student_1.name
# print(student_1_name)

# student_1.study()
# ---------- 객체지향 - 클래스(3) ----------
# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# student_1.major = '기계공학과'

# student_1.edit_major('기계공학과')
# print(student_1.major)

# ---------- 객체지향 - 상속(1) ----------
# 상속(Inheritance)
class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country
# ---------- 객체지향 - 상속(2) ----------
# 오버라이딩 - 부모 클래스의 이름과 같은 함수를 생성하여 내용만 다르게 하는 것
    def study(self):
        print(f'{self.name} is studying now.')

foregin_stud_1 = ForeignStudent('이테킷', '국어국문학과', '미국')
# print(foregin_stud_1.name)
# print(foregin_stud_1.major)
# print(foregin_stud_1.country)
# print(foregin_stud_1.is_graduated)
# foregin_stud_1.study()
