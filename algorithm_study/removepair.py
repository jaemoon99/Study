def solution(s):
    # 체크 리스트
    check_list = []

    # s 길이만큼 순회
    for x in range(0, len(s)):

        #체크리스트가 비어있을 경우 삽입
        if len(check_list) == 0:
            check_list.append(s[x])

        # 현재 문자와 체크리스트의 맨 끝이 같을 경우
        elif s[x] == check_list[-1]:

            # 맨 끝값 제거
            check_list.pop()

        # 다를 경우
        else:
            # 체크 리스트에 삽입
            check_list.append(s[x])
    
    # 길이가 0이면 1 0이 아니면 0을 반환
    if len(check_list) == 0:
        return 1
    else:
        return 0

s = 'baabaa'

print(solution(s))