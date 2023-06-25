'''

    while 문

    문법:
        초기값
        while 조건식:
            문장
            증감식

'''

n=1
while n<5:
    print("hello")
    n+=1
print("End")

'''

    while 문 이용한 무한루프

    문법:
        while True:
            문장1
            문장2
            if 조건식: break

'''

while True:
    name = input("이름입력(중지 시 Q입력): ")
    print("입력한 이름:", name)
    if name == "Q": break

print("종료")