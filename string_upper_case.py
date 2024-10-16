class s():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter a string: ")

    def print_String(self):
        print("The result is", self.str1.upper())

str1 = s()

str1.get_String()
str1.print_String()