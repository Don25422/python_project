class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name,"is speaking")

person1 = Person("John", 22, "Teacher")
print(person1.name)
person1.speak()

person2 = Person("Martha", 22, "Doctor")
print(person2.name)
person2.speak()