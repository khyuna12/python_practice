'''
    JSON 변환

    1. json --> 문자열
        import json

        json.dumps(json)

    2. 문자열 --> json

        json.loads(문자열)
'''

import json

# 1. 문자열 --> json

s = '{"username":"홍길동", "age":20}'
print(s, type(s))  # {"username":"홍길동", "age":20} <class 'str'>

s_json = json.loads(s)
print(s_json, type(s_json))  # {'username': '홍길동', 'age': 20} <class 'dict'>
print(s_json["username"], s_json["age"])  # 홍길동 20

l_s = "[10,20,30]"
print(l_s, type(l_s))  # [10,20,30] <class 'str'>

l_json = json.loads(l_s)
print(l_json, type(l_json))  # [10, 20, 30] <class 'list'>
print(l_json[0], l_json[1], l_json[2])  # 10 20 30

# 2. json --> 문자열
s_json = {"username":"홍길동", "age":20}
print(s_json, type(s_json))
s = json.dumps(s_json)
print(s, type(s))