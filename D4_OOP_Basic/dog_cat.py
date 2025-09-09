class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

def mulRun(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()

print('A is Animal ? ',isinstance(a,Animal))
print('B is Dog ?',isinstance(b,Dog))

mulRun(a)
mulRun(b)