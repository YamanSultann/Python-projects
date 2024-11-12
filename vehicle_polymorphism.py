class BMW():
    def origin(self):
        print("BMW is from Germany")

    def type(self):
        print("BMW is one of the biggest supercar manufacturers")

    def age(self):
        print("BMW was founded in 1916")

class Ferrari():
    def origin(self):
        print("Ferrari is from Italy")

    def type(self):
        print("Ferrari makes top of the range supercars")

    def age(self):
        print("Ferrari was founded in 1939")

obj_BMW = BMW()
obj_Ferrari = Ferrari()

for company in (obj_BMW,obj_Ferrari):
    company.origin()
    company.type()
    company.age()