class Korean:

    country = 'korea'            #서로가 공유하는 변수: class 변수

    # def __init__(self, name, age, address):
    #     self.name = name         # 객체 변수
    #     self.age = age
    #     self.address = address

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print("domestic")
        else:
            print('abroad')

Korean.trip('korea')
Korean.trip('usa')


# man = Korean('Hong', 35, 'seoul')
# woman = Korean('Julie', 47, 'seoul')

# # Koeran.name
# print(man.name)         
# print(Korean.country)           # Koeran이라는 클래스에 있는 country 변수. 클래스 Korean을 통한 클래스 변수 접근
# print(man.country)          # instance man을 통한 클래스 변수  접근
# print(woman.country)