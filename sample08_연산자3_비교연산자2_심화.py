# 동등 비교

'''
a == b : a와 b의 실제값 비교
a is b : a와 b의 주솟값 비교(id(a) == id(b)와 동일)
'''

a = [1,2,3,4,5]
b = a
print(a, id(a))  # [1, 2, 3, 4, 5] 1726700707456
print(b, id(b))  # [1, 2, 3, 4, 5] 1726700707456

print(a==b)  # True
print(a is b, id(a)==id(b))  # True True


c = a[:]  # a 복사본 생성
print(c, id(c))  # [1,2,3,4,5] 2197726534016 다른 주솟값

print(a==c)  # True
print(a is c)  # False