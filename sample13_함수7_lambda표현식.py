'''
    lambda 표현식(익명함수)
    - def 함수명() 문법을 이용한 함수 작성의 또다른 표현식
    - 단일 문장인 경우에만 람다 표현식이 가능함
    - 익명함수이기 때문에 변수에 저장해서 호출해서 사용함 (일급객체이기 때문에 가능)

'''

# 1. 파라미터 X, 리턴값 X
def fun():
    print("fun")

# lambda 표현식
fun = lambda : print("lambda fun")
fun()  # lambda fun

# 2. 파라미터 O, 리턴값 X
def fun2(n, n2):
    print("fun2", n, n2)

# lambda 표현식
fun2 = lambda n=10, n2=20, *n3, **n4 : print("lambda fun2", n, n2, n3, n4)
fun2()  # lambda fun2 10 20
fun2(10, 20)  # lambda fun2 10 20
fun2(10, 23, 4, 5, 6, 5, age=20, addr="서울")  # lambda fun2 10 23 (4, 5, 6, 5) {'age': 20, 'addr': '서울'}

# 3. 파라미터 X, 리턴값 O
def fun3():
    return 100

# lambda 표현식
fun3=lambda :100
res = fun3()
print("lambda fun3", res)  # lambda fun3 100

# 4. 파라미터 O, 리턴값 O
def fun4(n,n2):
    return n+n2

# lambda 표현식
fun4=lambda n,n2:n+n2
res = fun4(10, 20)
print("lambda fun4", res)  # lambda fun4 30