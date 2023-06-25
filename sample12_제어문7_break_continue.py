'''

    break: 반복문 빠져나올 때
    continue: 특정 회차에서 일부분의 문장을 skip 할 때

'''

# break, continue , else 문
print("-------------------------------------")
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 3: continue
    # if i == 4: break
    print(i, end=' ')
print("end")

print("-------------------------------------")
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 4: break
    print(i, end=' ')
else:   # 정상적인 반복문 종료시 실행됨
    print("정상종료")
print("end")