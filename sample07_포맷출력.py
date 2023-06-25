# 2) 포맷지정 출력

# 1. 문자열 데이터 표현
mesg = "이름:{}".format('홍길동')
print(mesg)

mesg = '이름:{0}'.format('홍길동')  # 0: 순서
print(mesg)

mesg = '이름:{0}, 나이:{1}'.format('홍길동',20)
print(mesg)  # 이름:홍길동, 나이:20
mesg = '이름:{1}, 나이:{0}'.format('홍길동',20)
print(mesg)  # 이름:20, 나이:홍길동
mesg = '이름:{}, 나이:{}'.format('홍길동',20)
print(mesg)  # 이름:홍길동, 나이:20
mesg = '이름:{0:5s}, 나이:{1}'.format('홍길동',20)  # 이름을 5글자로
print(mesg)  # 이름:홍길동  , 나이:20

# 2. 수치 데이터 표현
mesg = '{0}'.format(123456789)
print(mesg)  # 123456789

mesg = '{0:f}'.format(123456789)  # 실수로 표현
print(mesg)  # 123456789.000000

mesg = '{0:.3f},{0:.9f}'.format(123.4567)
print(mesg)  # 123.457,123.456700000

mesg = '{0:,}'.format(123456789)
print(mesg)  # 123,456,789

# 3. key 사용 (중요)
mesg = '이름: {username}, 나이: {age}'.format(username='홍길동', age=20)
print(mesg)

# 4. unpacking - 집합형 데이터 풀어헤치기 (문자열/리스트/튜플/셋/딕트)
mesg = '{0}:{1}:{2}'.format(*'홍길동')
print(mesg)  # 홍:길:동

mesg = '{0}:{1}:{2}'.format(*['홍길동', '이순신', '강감찬'])
print(mesg)  # 홍길동:이순신:강감찬

# 4. unpacking - dict
person = {'username': '홍길동', 'age': 20}  # ==> username=홍길동, age=20
mesg = '이름: {username}, 나이: {age}'.format(**person)
print(mesg)  # 이름: 홍길동, 나이: 20

# 정렬, 채우기, ...
help('FORMATTING')
'''
Aligning the text and specifying a width:

   >>> '{:<30}'.format('left aligned')
   'left aligned                  '
   >>> '{:>30}'.format('right aligned')
   '                 right aligned'
   >>> '{:^30}'.format('centered')
   '           centered           '
   >>> '{:*^30}'.format('centered')  # use '*' as a fill char
   '***********centered***********'
'''

# 5. % 지정 방식 ( 고전방식 )
print("이름: %s 나이: %d 신장: %.2f 결혼여부:%s 성별:%c" % ("홍길동", 200, 178.5987, True, '남'))

# 6. format string 방식
name = "KyIN"
age = 20

print("이름:{name} 나이:{age}")  # 이름:{name} 나이:{age}
print(f"이름:{name} 나이:{age}")  # 이름:KyIN 나이:20
print(f"이름:{name} 나이:{age+1}")  # 산술 연산 가능, 이름:KyIN 나이:21
print(f"이름:{name} 나이:{age > 30}")  # 비교 연산 가능, 이름:KyIN 나이:False
print(f"이름:{name.lower()} 나이:{age > 30}")  # 이름:kyin 나이:False