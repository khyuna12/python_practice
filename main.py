print("Hello")
print("Hello")     # Ctrl + D로 코드 복사 가능
print('Hello')     # 홑따옴표, 쌍따옴표 구분 없음
print(True, False) # 논리값(참, 거짓) - 첫 글자 반드시 대문자
print(10, 3.14)    # Shift + Alt + 화살표: 코드 위치 변경
print(None)        # null값

print([10,20,30])  #list(리스트), 대괄호, [값,...], 순서있음, 중복가능
print((10,20,30))  #tuple(튜플), 소괄호, (값,...), 순서있음, 중복가능, 값 변경 불가
print({10,20,30})  #set(셋), 중괄호, {값,...}, 순서없음, 중복불가
print({ 'p01':30, 'p02':10})          #dict(딕트), {key:value, key:value,...}

 #print({10,20,30, "홍길동", [1,2,3]}) #에러: set은 immutable 값만 저장가능
print({10,20,30, "홍길동"}) #작동