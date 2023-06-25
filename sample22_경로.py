'''
    경로
'''

import os

# 1. 현재 작업 경로 출력
print(os.getcwd())  # C:\Users\kha98\PycharmProjects\pythonProject

# 2. 경로 생성하기 c:\users\xxx
print(os.path.join("c:\\", "Users", "xxx"))  # c:\Users\xxx

# 현재 작업 경로에 aaa.txt 파일 경로 추가
print(os.path.join(os.getcwd(), 'aaa.txt'))  # C:\Users\kha98\PycharmProjects\pythonProject\aaa.txt

# 3. 특정 경로에서 디렉토리 경로 얻기
p = r"C:\Users\kha98\PycharmProjects\pythonProject\aaa.txt"
print(os.path.dirname(p))  # C:\Users\kha98\PycharmProjects\pythonProject

# 4. 특정 경로에서 파일명 얻기
p = r"C:\Users\kha98\PycharmProjects\pythonProject\aaa.txt"
print(os.path.basename(p))  # aaa.txt

# 5. 특정 경로에서 디렉토리와 파일명 한꺼번에 분리하기
p = r"C:\Users\kha98\PycharmProjects\pythonProject\aaa.txt"
dir, file = os.path.split(p)
print(dir, file)  # C:\Users\kha98\PycharmProjects\pythonProject aaa.txt

# 6. 파일에서 파일명과 확장자 분리
p = r"C:\Users\kha98\PycharmProjects\pythonProject\aaa.txt"
file = os.path.basename(p)  # aaa.txt
file_name, extend_name = os.path.splitext(file)
print(file_name, extend_name)  # aaa .txt

# 7. 특정 디렉토리 목록 보기
dir_list = os.listdir(os.getcwd())
print(dir_list)  # 현 디렉토리(폴더)의 파일 다나옴