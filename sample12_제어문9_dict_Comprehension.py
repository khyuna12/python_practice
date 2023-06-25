'''

    dict Comprehension
    => dict로부터 가공하여 새로운 dict로 반환

    가. 변수 = { k:v for k,v in dict.items()}
    나. 변수 = { k:v for k,v in dict.items() if 조건}
    다. 변수 = { 3항연산자 k:v for k,v in dict.items()}

'''

# 가.
d = {"대한민국":"서울", "미국":"워싱턴", "일본":"도쿄"}
new_d = {v:k for k,v in d.items()}  # key와 value 바꾸기
new_d2 = {k:len(v) for k,v in d.items()}
print(new_d)  # {'서울': '대한민국', '워싱턴': '미국', '도쿄': '일본'}
print(new_d2)  # {'대한민국': 2, '미국': 3, '일본': 2}

# 나. 국가명(key)이 2글자인 경우에만 반환
new_d = {v:k for k,v in d.items() if len(k)==2}
print(new_d)  # {'워싱턴': '미국', '도쿄': '일본'}

# 다. 국가명 중에서 대한민국은 korea로 표시
new_d = {"korea" if k=="대한민국" else k for k,v in d.items()}
print(new_d)  # {'미국', '일본', 'korea'}