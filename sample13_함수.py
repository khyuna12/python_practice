'''
    함수
'''

# 1. 파라미터 X 리턴값 X

def fun():
    print("fun")
fun()  # 호출
print("end")

# 2. 파라미터 O 리턴값 X
def fun2(n, n2):
    print("fun2", n, n2)
#fun2()  # 에러
fun2([1,2,3], "abc")  # 개수만 맞춰주면 됨

# 3. 파라미터 X 리턴값 O
def fun3():
    print("fun3")
    return "fun"  # 리턴값은 모든 데이터 가능

res = fun3()  # 리턴값을 담을 변수가 필요
print(res)

def fun4():
    print("fun4")
    return 200,100  # 리턴값은 모든 데이터 가능

res = fun4()  # 리턴값을 담을 변수가 필요
print(res)

# 3. 파라미터 O 리턴값 O
def fun5(n1, n2):
    print("fun5")
    return n1+n2

res = fun5(10,20)
print(res)