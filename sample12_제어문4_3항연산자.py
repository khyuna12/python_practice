'''
    3항 연산자
    변수 = 참값 if 조건식 else 거짓값
'''

# 4. 3항 연산자
jumsu = int(input('점수-->'))

res = '합격' if jumsu >= 60 else '불합격'
print(res)

# 5. 중첩 3항 연산자
n = 4
m = "Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"
print(m)  # Good day

num = 70
s = "A" if num>=90 else "B" if num>=80 else "C"
print(s)  # C