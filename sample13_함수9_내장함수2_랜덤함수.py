'''
    랜덤함수

    import random 필수
'''

# 랜덤함수
import random

# help(random)
print(dir(random))

#1. randint(a, b)  # a <= N <= b. Alias for randrange(a, b+1).
n = random.randint(1, 7)
print("1. randint:", n)  # 1부터 7까지

# 2. random()  # 0 ~ 1 사이의 랜덤 실수
n = random.random()
print("2. random:", n)

# 3. randrange(a, b)  #a <= N < b
n = random.randrange(1,7)
print("3. randrange:", n)  # 1부터 6까지

# 4. shuffle(x)
random.seed(42)  # seed값을 고정하면 항상 동일한 값을 반환한다.
# n = random.randint(1, 7)
# print(n)
x = ['a','b','c']
random.shuffle(x)
print("4. shuffle:", x)  # ['b', 'a', 'c'] 항상 같은 값

# 5. choice(x)
print("5. choice:", random.choice(x))