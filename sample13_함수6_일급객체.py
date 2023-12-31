'''
    일급객체(first-class)

    개념: 기능 담당하는 함수를 정수 및 문자열과 같은 데이터로 처리한다.

'''
# 1. 함수는 데이터이기 때문에 변수에 저장 가능하다.
def fun():
    print("fun")

print(fun)  # <function fun at 0x0000023ACC9AC5E0>
n = fun
n()  # fun

# 2. 함수는 데이터이기 때문에 함수 호출 시 인자값으로 사용이 가능하다.
# y 호출했는데 실제 반응은 x 함수이다. ==> 트리거 (y가 방아쇠, x가 총알)

# 콜백함수(callback) 구현이 가능하다.
# 콜백함수는 사용자가 호출한 함수가 아니고 특정 시점에 시스템이 호출하는 함수를 의미한다.
# 콜백함수를 구현하는 방법은 직접 함수명을 알려줘야 한다.
def x():
    print("x")

def y(n):
    n()

y(x)  # x

# 3. 함수는 데이터이기 때문에 함수 리턴값으로 사용이 가능하다.
def k():
    print("k")

def k2():
    return k

res = k2()  # 리턴값이 있으니까
res()  # k
k()  # k
