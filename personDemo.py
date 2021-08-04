class Person:
    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()
girl = Person()

boy.who_am_i('john', 15, '123-1234', 'toronto')
girl.who_am_i('alice', 13, '321-3213', 'new york')

print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

print(girl.name)
print(girl.age)
print(girl.tel)
print(girl.address)