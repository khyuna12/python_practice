'''
    packing 파라미터

    def 함수명(n, *n2):
        pass
'''

# 변수 선언
n, *n2 = 1,2,3,4,5
print(n, n2)  # 1 [2, 3, 4, 5]

def fun(n, *n2):
    print(n, n2)

fun(10,20)  # 10 (20,)
fun(10,20,30,40)  # 10 (20, 30, 40)

def fun2(n,x, *n2):
    print(n,x, n2)

fun2(10,20)  # 10 20 ()
fun2(10,20,30,40)  # 10 20 (30, 40)

# default + packing 혼합 가능

def fun3(n=10,x=20, *n2):
    print(n,x, n2)

fun3()  # 10 20 ()
fun3(1,2,3,3,4,5)  # 1 2 (3, 3, 4, 5)