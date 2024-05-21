class Animal:
    def say_hello(self,count):
        for i in range(0, 7):
          print("Hello")

class Cat(Animal):
    def say_hello(self, count):
        for i in range(0, count):
           print("may")

class Dog(Animal):

    def say_hello(self, count):
        hello = 'gaf'
        for i in range(0, count):
            print(hello)
        
cat = Cat()
dog = Dog()

cat.say_hello(count=44) 
dog.say_hello(count=11)