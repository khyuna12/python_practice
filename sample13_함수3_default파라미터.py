'''
    default 파라미터

    def 함수명(n=기본값, n2=기본값):
        pass
'''

def fun(n=10, n2=20):
    print(n, n2)

fun()  # 10 20
fun(100)  # 100 20
fun(100,200)  # 100 200