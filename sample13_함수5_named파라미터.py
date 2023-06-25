'''
    named 파라미터

    def fun(age, username):
        pass

    fun(10, "홍길동")
    fun(age=10, username='홍길동')
'''

def fun(age, username):
    print(age, username)

fun(10, '홍길동')  # 10 홍길동
fun(age=10, username='홍길동')  # 10 홍길동
fun(username='홍길동', age=10)  # 10 홍길동

# 추가 정리
# 들쭉날쭉한 데이터 dict로 받음
def fun2(**n):
    print(n)

fun2(age=10)  # {'age': 10}
fun2(age=10, username='홍길동')  # {'age': 10, 'username': '홍길동'}
fun2(age=10, username='홍길동', address='서울')  # {'age': 10, 'username': '홍길동', 'address': '서울'}

# 혼합
def fun3(n1,n2,*n3, **n4):
    print(n1,n2,n3,n4)

fun3(10,20,30, age=10, username='홍길동')  # 10 20 (30,) {'age': 10, 'username': '홍길동'}
fun3(10,20,30,40,50, age=10, username='홍길동')  # 10 20 (30, 40, 50) {'age': 10, 'username': '홍길동'}