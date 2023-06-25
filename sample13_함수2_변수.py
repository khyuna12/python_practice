'''
    python의 변수는 함수 scope를 따른다.
    ==> 함수안에서 선언된 변수는 함수 안에서만 사용 가능하다.
'''

n = 10  # 전역 변수 (global variable)
def fun():
    n2 = 20  # 지역 변수 (local variable)
    print("n:", n)
    print("n2:", n2)

fun()  # n, n2값 모두 나옴
'''
n: 10
n2: 20
'''
print("n:", n)  # n: 10
print("n2:", n2)  # error