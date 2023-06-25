'''
    클래스 변수 및 메서드
'''

class Person:

    address = "서울"  # 클래스 변수, 단 한 번 생성

    def __init__(self, n, a):
        # 인스턴스 변수, 객체 생성 시마다 매번 생성
        self.username = n
        self.age = a

    def info(self):
        return self.username, self.age, Person.address

    # 클래스 메서드 / 목적: 객체 생성없이 사용하기 위해서
    @classmethod
    def get_address(cls):
        return Person.address

Person.address = "제주"  # 한번에 모든 address 변경이 된다
print(Person.get_address())
p = Person("홍길동", 20)
p2 = Person("이순신", 40)

print("p1:", p.info(), Person.get_address())
print("p2:", p2.info(), Person.get_address())
