'''
    sample6.csv 파일 읽기
'''

import csv
# 가. 한 줄 작성
with open(r"c:\sample6.csv", mode="w", encoding="utf-8") as f:
    data = csv.writer(f)
    data.writerow(["홍길동", 20, "대전"])  # 집합형만 가능

# 나. 여러줄 작성
with open(r"c:\sample7.csv", mode="w", newline="", encoding="utf-8") as f:  # 개행 없애기
    data = csv.writer(f)
    data.writerows([["홍길동1", 20, "대전"], ["홍길동2", 20, "춘천"]])

print("정상종료")