### 연산자 ###

# 1) 산술 연산자
a = 10
b = 3
print(a+b)    # 13
print(a-b)    # 7
print(a*b)    # 30
print("h"*10) # hhhhhhhhhh
print(a/b)    # 3.3333333333333335 나누기할 때 소수점까지 출력됨.
print(a % b)  # 1  ,  Modulus 나머지
print(a//b)   # 3  ,  Floor Division   소수점 버림
print(a**b)   # 1000, square ( 제곱 )

# 몫과 나머지를 한꺼번에 반환 ( tuple로 반환 )
result = divmod(10, 3)
x, y = divmod(10, 3)  # 일반적(갯수가 일치해야) ex. name, age, address = ("홍길동", 20, "서울")
print(result)  # (3, 1)
print(x, y)    # 3 1