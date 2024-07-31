class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class desig:
    def __init__(self, name, age, desig):
        self.desig= desig

person1 = person('john', 32)
person2 = desig('Peter', 34, 'Developer')

print(person1.name)
print(person2.desig)