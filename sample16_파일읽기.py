'''
    c:\sample.txt 파일 읽기
'''

# 1. 파일 읽기
# mode: r(읽기) w(쓰기, 덮어쓰기) a(쓰기, 추가)

# 가. f.read()는 한번에 str로 반환한다.
with open(r"c:\sample.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)

print("-"*100)

# 나. f.readline()는 첫 줄만 읽는다. ==> 반복적으로 읽기
with open(r"c:\sample.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print(line)
# 일반적으로 파일을 읽는 코드
with open(r"c:\sample.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line: break  #EOF (End Of File)
        print(line, end="")

print("-"*100)
# 다. f.readlines()는 한 번에 list로 반환한다.
with open(r"c:\sample.txt", "r", encoding="utf-8") as f:
    list_line = f.readlines()
    print(list_line)  # ['hello\n', 'world\n']
    for line in list_line:
        print(line, end="")

