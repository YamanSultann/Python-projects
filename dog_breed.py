class Dog:
    species = "dog"
    def __init__(self,name,age):
        self.name = name
        self.age = age

daisy = Dog("Daisy",10)
cooper = Dog("Cooper",15)

print("Daisy is a {}".format(daisy.species))
print("Cooper is also a {}".format(cooper.species))

print("{} is {} years old".format(daisy.name,daisy.age))
print("{} is {} years old".format(cooper.name,cooper.age))