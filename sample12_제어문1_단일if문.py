'''
    단일 if문
    - 조건에 따라서 실행되거나 실행되지 않는 문장을 작성할 수 있다.
'''

# print("1")
# if False:  # True나 False 대신에 연산식 사용 (비교연산자, 논리연산자, 멤버쉽연산자)
#     print("2")
#
# print("3")
# print("4")

# 1. 단일 if문
print("1")
if 3==4:
    print("2")
    print("3")
    print("4")
print("5")
print()

# 1. 단일 if 문2
if 3 == 3: print("True")
print("-------------------------")

# # 문제: 키보드로 숫자를 입력 받아서 짝수인 경우에만 출력
# num = int(input("숫자입력:"))
# if num % 2 == 0:
#     print("hello")

# 문제2: xxx리스트 안에 값이 있는지 없는지 확인해서 없을 경우에만 출력
xxx=[]
if len(xxx) != 0:
    print("list에 값 있음")
if xxx:  # True/False가 아닌 값도 사용 가능
    print("list에 값 있음")