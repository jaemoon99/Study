def solution(n, m, section): # n은 총 개수, m은 롤러 길이, section은 칠해야 할 번지 수
    roller_range = section[0] + m - 1 # 첫 롤러(첫 인덱스 + 롤러길이 - 1)
    count = 1 # 롤러 횟수 카운트
    for x in section: # 칠해야 할 번지 순서대로
        if x > roller_range: # 번지가 현재 롤러 길이보다 크면
            roller_range = (x + m - 1) # 새로운 롤러 지정
            count += 1 # 롤러 개수 추가
    return count