'''
    반복문

    for 변수 in 집합형:
        문장

    집합형: 리스트, 문자열, range(n)
'''

# 1) 특정 문장 반복 처리하는 기본 코드
for n in range(3):
    print("happy", n)

# 2) 집합형에 저장된 데이터 얻기
for n in [1, 2, 3]:
    print(n)

for s in 'abcde':
    print(s)

for n in (10, 20, 30):
    print(n, end=" ")

for n in {100, 200, 300, 300}:
    print(n)

# 반복할 때 idx값 얻기
for n in enumerate([10, 20, 30]):
    print(n)

for idx, n in enumerate("abcde"):
    print(idx, n)

for idx, n in enumerate([10, 20, 30], 1):
    print(idx, n)

# 1. 일정횟수만큼만 반복처리
for _ in "hello":
    print("A", end=" ")
print()

for _ in range(5) :
    print("A", end=" ")
print()

# 2. 집합형 데이터값 반복처리
# 1) 문자열 반복
for x in "Hello":
    print(x, end= " ") # H e l l o
print()

# 2) list 반복
for x in [10,20,30,40]:
    print(x, end=" ") # 10 20 30 40
print()

# 3) 반복횟수 조회
datas = ['a', 'b', 'c']
for idx, value in enumerate(datas):
    print(idx, value, end=" ")         # 0 a 1 b 2 c , 순서와 값이 차례대로 출력됨
print()

# 4) dict 반복
soft = {'java':'웹용', 'python':'만능언어', 'oracle':'db처리'}
for key, value in soft.items():
    print(key + ':  ' + value)
print()

for key in soft.keys():
    print(key, end=" ")
print()

for value in soft.values():
    print(value, end=" ")
print()