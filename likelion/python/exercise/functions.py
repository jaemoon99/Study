# ---------- 함수 - 함수(1) ----------
# 함수(functions)
# 매개변수(파라미터), 인자(인수)

# 'name' => 파라미터
def print_name(name):
    print(f'이름은 {name}입니다.')

# "김멋사", "이멋사" => 인자
print_name("김멋사")
print_name("이멋사")


def print_name_age(name, age):
    print(f'이름은 {name}이고 {age}살 입니다.')

print_name_age("김멋사", "28")

def print_ex_string():
    print('예시 문자열입니다.')

print_ex_string()
# ---------- 함수 - 함수(2) ----------
def order_coffee(qty, option="hot"): # deflaut값이 있는 매개변수는 항상 마지막에 있어야 한다.(안그럼 오류남)
    print(f'{qty}잔 / {option}')

order_coffee(3, 'iced')
order_coffee(3)
order_coffee(option='iced', qty=5) # 인자에 직접 값을 달아주면 순서는 상관이 없어진다.
# ---------- 함수 - 함수(3) ----------
def get_id(email):

    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id

    else:
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@test.com')
print(user_id)

user_id = get_id('user@example.com')
print(user_id)
# ---------- 함수 - 모듈 ----------
