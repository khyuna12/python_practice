'''
    예외처리
'''

print("1")
print("2")

try:
    n = 0
    result = 10 / n  #여기서 멈춤
    print("결과값:", result)
except ZeroDivisionError as e:
    print("0으로 나눠 예외발생")

print("3")
print("end. 정상종료")