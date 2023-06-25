'''

    generator Comprehension

    1) 문법:
        변수 = (표현식 for 변수 in 집합형)


'''

list_x = [n for n in [1,2,3]]
generator_x = (n for n in [1,2,3])

print(list_x)  # [1, 2, 3]
print(generator_x)  # <generator object <genexpr> at 0x000002850DC55C10>

# data개수만큼 호출 가능
print(next(generator_x))  # 1
print(next(generator_x))  # 2
print(next(generator_x))  # 3
# next후 다시 가져와서 작업해야 함
generator_x = (n for n in [1,2,3])  # 없으면
print(list(generator_x))  # 오류남
