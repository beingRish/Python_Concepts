class Person:
    name = "annonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Rishabh"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rishabh Kumar")
print(p1.name)
print(Person.name)