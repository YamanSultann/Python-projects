from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    print("I can walk and run")

class Crow(Animal):
    print("I can fly")

class Whale(Animal):
    print("I can swim")

class Cheetah(Animal):
    print("I can sprint very fast")

A = Human()
A.move()

B = Crow()
B.move()

C = Whale()
C.move()

D = Cheetah()
D.move()