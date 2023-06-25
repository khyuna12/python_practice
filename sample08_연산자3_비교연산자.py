# 3) 비교 연산자
k = 10
k2 = 5
print( k == k2 )  # SQL에서는 = 임, False
print( k != k2 )  # True
print( k > k2 )  # True
print( k >= k2 )  # True
print( k < k2 )  # False
print( k <= k2 )  # False

# None 비교
xyz = None
print( xyz is None ) # 권장, True

# n값이 5보다 크고 20보다 작은지
n = 10

result = (n > 5) and (n < 20)  # 일반적인 프로그램 언어에서 사용하는 방식(권장)
print(result)  # True

result = 5 < n < 20  # python만 가능
print(result)  # True
