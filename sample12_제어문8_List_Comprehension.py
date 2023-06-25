'''

    List Comprehension
    => list로부터 가공한 새로운 리스트 반환

    가. 변수 = [ 표현식  for 변수 in 집합형]
    나. 변수 = [ 표현식  for 변수 in 집합형 if 조건식]
    다. 변수 = [ 3항연산자 표현식 for 변수 in 집합형]
        변수 = [ 참 if 조건식 else 거짓 표현식 for 변수 in 집합형]
'''

# 가.
x = [n+1 for n in [1,2,3]]
y = [n > 2 for n in [1,2,3]]
z = [n.upper() for n in ["A","b","C"]]  # ['A', 'B', 'C']
print(z)
'''
m = ["A","b","C"]
k = []
for m2 in m:
    m3 = m2.upper()
    k.append(m3)
print(k)  # ['A', 'B', 'C']
'''

# 나.
x = [n for n in range(1, 11) if n%2==0]
print(x)  # [2, 4, 6, 8, 10]

# 다.
x = [ 0 if n%2==0 else 1 for n in range(1,11)]
print(x)