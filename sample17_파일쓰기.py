'''
    c:\sample2.txt 파일 쓰기
    => 파일이 없으면 자동으로 생성해준다.
'''
# 가. 파일 쓰기, mode: w(덮어쓰기) a(추가)
with open(r"c:\sample2.txt", "w", encoding="utf-8") as f:
    f.write("이름,나이,주소\n")
    f.write("홍길동1,40,서울1\n")
with open(r"c:\sample2.txt", "a", encoding="utf-8") as f:
    f.write("홍길동2,20,서울2\n")
with open(r"c:\sample2.txt", "a", encoding="utf-8") as f:
    f.write("홍길동3,20,서울3")
print("정상종료")