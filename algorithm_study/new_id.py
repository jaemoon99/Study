def solution(new_id):
    remove_string = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    # step 1
    step1 = new_id.lower()
    # step 2
    step2 = list(step1)
    for x in range(0, len(step2)):
        if step2[x] in remove_string:
            step2[x] = ""
    # step 3
    step3 = list("".join(step2))
    for x in range(0, len(step3)):
        if x == len(step3) - 1:
            break
        elif step3[x] == '.' and step3[x + 1] == '.':
            step3[x] = ""
    # step 4
    step4 = "".join(step3).strip('.')
    # step 5
    step5 = list("".join(step4).strip('.'))
    if step5 == []:
        step5.append('a')
    for x in range(0, len(step5)):
        if step5[x] == ' ':
            step5[x] = 'a'
    # step 6
    if len(step5) >= 16:
        step6 = list("".join(step5[:15]).strip('.'))
    else:
        step6 = list("".join(step5).strip('.'))
    # step 7
    step7 = "".join(step6)
    while 1:
        if len(step7) >= 3:
            return step7
        else:
            step7 += step7[-1]

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

# aaa = ['!', '@', '#', '*']
# a = '...!@BaT#*..y.abcdefghijklm'
# a = a.lower()
# a_a = list(a)
# for x in range (0, len(a_a)):
#     if a_a[x] in aaa:
#         a_a[x] = ""
# print(a_a)
# for x in range (0, len(a_a)):
#     if a_a[x] == '.' and a_a[x + 1] == '.':
#         a_a[x] = ""
# print("".join(a_a))
# a = list("".join(a_a).strip('.'))
# print(a)
# for x in range(0, len(a)):
#     if a[x] == " ":
#         a[x] = 'a'
# print(a)
# if len(a) >= 16:
#     a = a[:15]
#     a = "".join(a).strip('.')
# while 1:
#     if len(a) >= 3:
#         break
#     else:
#         a += a[-1]
# print(a)