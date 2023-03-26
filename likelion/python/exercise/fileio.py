# ---------- 파일 다루기와 예외 처리 - 파일 읽기 ----------
# 파일 읽기 쓰기

# f  = open('literature/poem.txt', 'r', encoding='UTF-8') # 파일 열기

# # print(f.read()) # 파일 전체를 읽어옴
# print(f.readline()) # 한 줄만 읽어옴
# print(f.readlines()) # 각각의 줄을 리스트의 요소로 읽어옴

# f.close() # 파일 닫기

# with open('literature/poem.txt', 'r', encoding='UTF-8') as f: # .close() 없어도 알아서 파일이 닫힘
#     print(f.read())
# ---------- 파일 다루기와 예외 처리 - 파일 쓰기 ----------
f = open('literature/poem.txt', 'a', encoding='UTF-8') #옵션 w = 새로쓰기(기존 파일의 내용을 지우고 새로씀), a = 기존에 파일에 연결해서 쓰기

f.write("\n새로운 글이 작성되었습니다.")

f.close()